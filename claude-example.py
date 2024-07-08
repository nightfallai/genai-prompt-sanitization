import os

from anthropic import Anthropic
from dotenv import load_dotenv
from nightfall import (Confidence, DetectionRule, Detector, MaskConfig,
                       Nightfall, RedactionConfig)

# Load environment variables
load_dotenv()

# Initialize clients
try:
    # By default Nightfall will read the NIGHTFALL_API_KEY environment variable
    nightfall = Nightfall()  

    # Initialize the Anthropic client with your API key
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

except Exception as e:
    print(f"Error initializing clients: {e}")
    exit(1)

# The message you intend to send. Notice 1) the credit card number in the message and 2) conincidently the transaction number is the same as the credit card number. It's not senstive. Will the ML model get confused and redact it too?
user_input = "The customer said: 'My credit card number is 4916-6734-7572-5015 and the card is getting declined. My transaction number is 4916-6734-7572-5015.' How should I respond to the customer?"
payload = [user_input]

print("\nHere's the user's question before sanitization:\n", user_input)

# Define an inline detection rule that looks for Likely Credit Card Numbers and redacts them
detection_rule = [DetectionRule(
    [Detector(
        min_confidence=Confidence.VERY_LIKELY,
        nightfall_detector="CREDIT_CARD_NUMBER",
        display_name="Credit Card Number",
        redaction_config=RedactionConfig(
            remove_finding=False,
            mask_config=MaskConfig(
                masking_char="X",
                num_chars_to_leave_unmasked=4,
                mask_right_to_left=True,
                chars_to_ignore=["-"])
        )
    )]
)]

try:
    # Send the message to Nightfall to scan it for sensitive data
    findings, redacted_payload = nightfall.scan_text(
        payload,
        detection_rules=detection_rule
    )

    # If the message has sensitive data, use the redacted version, otherwise use the original message
    user_input_sanitized = redacted_payload[0] if redacted_payload[0] else payload[0]

    print("\nHere's the user's question after sanitization:\n", user_input_sanitized)

    # Define your prompt, ensuring it starts with "\n\nHuman:" and ending with "\n\nAssistant:"
    prompt = "\nYou are a level 1 support bot. Your role is to assist users with common issues and provide helpful information. \n\nHuman: " + user_input_sanitized + "\n\nAssistant:"

    # Send prompt to Anthropic model for AI-generated response
    response = client.completions.create(
        model="claude-2.1",
        prompt=prompt,
        max_tokens_to_sample=1024,
        temperature=0.7,
        top_p=1.0
    )

    print("\nHere's a generated response you can send the customer:\n", response.completion)

except Exception as e:
    print(f"An error occurred: {e}")
