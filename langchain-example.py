import os
from typing import Dict, List

from dotenv import load_dotenv
from langchain.chains.base import Chain
from langchain.prompts import PromptTemplate
from langchain.schema.language_model import BaseLanguageModel
from langchain.schema.prompt_template import BasePromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence
from langchain_anthropic import ChatAnthropic
from nightfall import (Confidence, DetectionRule, Detector, MaskConfig,
                       Nightfall, RedactionConfig)
from pydantic import Field

# Load environment variables
load_dotenv()

# Initialize Nightfall client
nightfall = Nightfall()

# Define Nightfall detection rule
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

class NightfallSanitizationChain(Chain):
    input_key: str = "input"
    output_key: str = "sanitized_input"

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]

    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]

    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        text = inputs[self.input_key]
        payload = [text]
        try:
            findings, redacted_payload = nightfall.scan_text(
                payload,
                detection_rules=detection_rule
            )
            sanitized_text = redacted_payload[0] if redacted_payload[0] else text
            print(f"\nsanitized input:\n {sanitized_text}")
        except Exception as e:
            print(f"Error in sanitizing input: {e}")
            sanitized_text = text
        return {self.output_key: sanitized_text}

# Initialize the Anthropic LLM
llm = ChatAnthropic(model="claude-2.1")

# Create a prompt template
template = "The customer said: '{customer_input}' How should I respond to the customer?"
prompt = PromptTemplate(template=template, input_variables=["customer_input"])

# Create the sanitization chain
sanitization_chain = NightfallSanitizationChain()

# Create the full chain using RunnableSequence
full_chain = (
    RunnablePassthrough() |
    sanitization_chain |
    (lambda x: {"customer_input": x["sanitized_input"]}) |
    prompt |
    llm
)

# Use the combined chain
customer_input = "My credit card number is 4916-6734-7572-5015, and the card is getting declined."
print(f"\ncustomer input:\n {customer_input}")
try:
    response = full_chain.invoke({"input": customer_input})
    print("\model reponse:\n", response.content)
except Exception as e:
    print("An error occurred:", e)