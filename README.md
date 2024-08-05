# Firewall for AI APIs: Sanitizing GenAI Prompts 

## Overview
Firewall for AI prevents sensitive data disclosure in GenAI applications, data pipelines, and autoamted workflows. It sanitizes PII, PCI, banking info, PHI, and intellectual property using state-of-the-art DLP models and fine-tuned LLMs, offering superior accuracy and speed over traditional regex and heuristic methods.

This repository provides examples of using Firewall for AI APIs to sanitize GenAI prompts for popular LLM services and frameworks using Python.

Implementing robust content filtering is crucial for data protection and regulatory compliance.

### Real-world Scenario
Each of the following cases, users tend to overshare and this information must be removed to prevent sensitive data disclosure. 

**Chatbots:** 
Users may overshare sensitive information like credit card numbers, bank account numbers, healthcare information with LLM chatbots. 

**RAG Datasets:** 
Resolved support tickets used to create RAG datasets may contain sensitive information like images of driver's licenses, passports, and credit cards.

**Healthcare Applications:** 
Health provider applications using LLMs to automate workflows will often include sensitive health information.

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
