# Firewall for AI API Sample Code

## Overview

Firewall for AI enables rapid identification and anonymization to protect sensitive data from disclosure through GenAI prompts, models, analytics pipelines, and automated workflows.

## Key Features

- **Comprehensive Coverage:** Supports over 100 entity types in text, files, and images, including names, addresses, Social Security numbers, credit card details, credit card images, banking account numbers, and protected health information. For a full list, refer to the [detector glossary](https://help.nightfall.ai/nightfall-ai/detection-engine/nightfall-detector-glossary).
- **Enhanced Accuracy:** Delivers up to twice the precision and recall compared to leading solutions like Google DLP, Microsoft Presidio, and AWS Guardrails. Benchmarks are available upon request at [support@nightfall.ai](mailto:support@nightfall.ai).
- **Low Latency:** ≤100ms P99
- **High Throughput:** >= 1000 rps

## Repository Contents

This repository contains sample code demonstrating how to use Firewall for AI APIs to sanitize GenAI prompts within popular LLM services and frameworks using Python.
1. **OpenAI ChatGPT**
2. **Anthropic Claude**
3. **LangChain / Anthropic Claude**

## Prerequisites

1. If you still need to get a Nightfall account, get one [here](https://firewallforai.com).

2. Create a Nightfall key and add it to your .env file. Here are some [instructions](https://help.nightfall.ai/nightfall-firewall-for-ai/key-concepts/setting-up-nightfall/creating-api-key) if you get tripped up.   

2. Ensure you have the following packages installed:

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
