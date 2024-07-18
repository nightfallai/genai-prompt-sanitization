from dotenv import load_dotenv
from nightfall import (
    Confidence,
    DetectionRule,
    Detector,
    MaskConfig,
    Nightfall,
    RedactionConfig,
)
from openai import OpenAI

# Load environment variables
# To run this script you must have a NIGHTFALL_API_KEY and OPENAI_API_KEY
load_dotenv()

# By default Nightfall will read the NIGHTFALL_API_KEY environment variable
nf_client = Nightfall()

# By default OpenAI will read the OPENAI_API_KEY environment variable
oai_client = OpenAI()

# The prompt you intend to send to OpenAI
user_input = """The customer said: 'My credit card number is 
4916-6734-7572-5015 and the card is getting declined.' 
How should I respond to the customer?"""
payload = [user_input]

print(f"\nHere's the user's question before sanitization:\n{user_input}")

# Define an inline Nightfall detection rule that looks for 
# Credit Card Numbers and redacts them with a string of "X"s
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

# Send the message to Nightfall to scan it for sensitive data.
# Nightfall returns the sensitive findings and a copy of your input payload with
# sensitive data redacted.
findings, redacted_payload = nf_client.scan_text(
    payload, detection_rules=detection_rule
)

# If the message has sensitive data, use the redacted version, otherwise use the
# original message.
if redacted_payload[0]:
    user_input_sanitized = redacted_payload[0]
else:
    user_input_sanitized = payload[0]

print(f"\nHere's the user's question after sanitization:\n{user_input_sanitized}")

# Send the sanitized prompt to OpenAI model for AI-generated response.
completion = oai_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input_sanitized},
    ],
    max_tokens=1024,
)

generated_response = completion.choices[0].message.content
print(f"\nHere's a generated response you can send the customer:\n{generated_response}")
