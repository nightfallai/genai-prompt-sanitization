# Firewall for AI APIs: Sanitizing GenAI Prompts 

## Overview

LLMs like ChatGPT and Claude can inadvertently receive sensitive information from user inputs, posing significant privacy concerns (OWASP LLM06). Without content filtering, these AI platforms can process and retain confidential data such as health records, financial details, and personal identifying information. 

This repository includes examples demonstrating using Firewall for AI APIs to sanitize GenAI prompts for popular LLM services and frameworks using Python. 

### Real-world Scenarios

**Support Chatbots:** 
Using LLMs to power a level-1 support chatbot can result in users oversharing sensitive information like credit card and Social Security numbers. Without content filtering, this information would be transmitted to Anthropic and added to your support ticketing system.

**Healthcare Apps:** 
Using LLMs to moderate content sent by patients or doctors may include sensitive protected health information (PHI), which could be unnecessarily transmitted to Anthropic.

Implementing robust content filtering mechanisms is crucial to protect sensitive data and comply with data protection regulations.

## Examples

The repository includes three examples:
1. **OpenAI ChatGPT**
2. **Anthropic Claude**
3. **LangChain / Anthropic Claude**

## Prerequisites

Ensure you have the following packages installed:

pip install openai anthropic langchain nightfall python-dotenv pydantic

## Contributing
Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the Apache 2 license.
