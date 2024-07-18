import os

from nightfall import (
    Confidence,
    DetectionRule,
    Detector,
    MaskConfig,
    Nightfall,
    RedactionConfig,
)
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

nightfall = (
    Nightfall()
)  # By default Nightfall will read the NIGHTFALL_API_KEY environment variable

# The message you intend to send
user_input = """
The customer said: 'My credit card number is 4916-6734-7572-5015
and the card is getting declined. My transaction number is
4916-6734-7572-5015.' How should I respond to the customer?"""
payload = [user_input]

print("\nHere's the user's question before sanitization:\n", user_input)

# Define an inline detection rule that looks for Likely Credit Card Numbers
# and redacts them
detection_rule = [
    DetectionRule(
        [
            Detector(
                min_confidence=Confidence.VERY_LIKELY,
                nightfall_detector="CREDIT_CARD_NUMBER",
                display_name="Credit Card Number",
                redaction_config=RedactionConfig(
                    remove_finding=False,
                    mask_config=MaskConfig(
                        masking_char="X",
                        num_chars_to_leave_unmasked=4,
                        mask_right_to_left=True,
                        chars_to_ignore=["-"],
                    ),
                ),
            )
        ]
    )
]

# Send the message to Nightfall to scan it for sensitive data
# Nightfall returns the sensitive findings and a copy of your input payload with
# sensitive data redacted
findings, redacted_payload = nightfall.scan_text(
    payload, detection_rules=detection_rule
)

# If the message has sensitive data, use the redacted version, otherwise use the
# original message
if redacted_payload[0]:
    user_input_sanitized = redacted_payload[0]
else:
    user_input_sanitized = payload[0]

print("\nHere's the user's question after sanitization:\n", user_input_sanitized)

# Send prompt to OpenAI model for AI-generated response
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input_sanitized},
    ],
    max_tokens=1024,
)

print(
    "\nHere's a generated response you can send the customer:\n",
    completion.choices[0].message.content,
)
