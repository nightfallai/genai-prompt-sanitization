# Firewall for AI APIs: Sanitizing GenAI Prompts 

## Overview
Firewall for AI prevents sensitive data disclosure in GenAI applications, data pipelines, and automated workflows. It sanitizes PII, PCI, banking information, PHI, and intellectual property using state-of-the-art DLP models and fine-tuned LLMs. This results in up to twice the precision and recall compared to leading solutions like Google DLP, Microsoft Presidio, and AWS Guardrails.

This repository provides examples of using Firewall for AI APIs to sanitize GenAI prompts for popular LLM services and frameworks using Python. 

## Examples

The repository includes three examples:
1. **OpenAI ChatGPT**
2. **Anthropic Claude**
3. **LangChain / Anthropic Claude**

## Prerequisites

Ensure you have the following packages installed:

    pip install -r requirements.txt 

## Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the Apache 2 license.

## Formatting and style

To sort imports run:

    isort .

To format code run:

    black .

To check code style run:

    pylint examples/
