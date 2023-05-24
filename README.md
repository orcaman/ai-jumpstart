# AI Jumpstart

Welcome to AI Jumpstart - a collection of practical examples showcasing how large language models (LLMs) can be utilized to perform different tasks in Natural Language Processing, Data Extraction, and Data Analysis. This repository contains various examples with OpenAI's GPT and LangChain's tools.

Each example is housed in its own directory under the "examples" folder, and they each come with their own `README.md` file which provides detailed instructions on how to use them. 

Here's a brief summary of each example:

## Examples

### [GPT on PDF](./examples/gpt_on_pdf/README.md)
This example demonstrates how to search inside a PDF file using natural language with LangChain's unstructured file loader and a retrieval Q&A chain.

### [GPT on Wikipedia](./examples/gpt_on_wikipedia/README.md)
This example demonstrates how to enable GPT to answer questions about Wikipedia search terms that GPT otherwise does not know about. It uses LangChain's Wikipedia loader and a retrieval Q&A chain.

### [GPT Scraper](./examples/gpt_scraper/README.md)
This example shows how to use OpenAI's vanilla Completion API to extract data points from HTML content. The demonstration focuses on the usage of a system prompt role and a user prompt role.

### [Pandas Agent Data Analysis](examples/pandas_agent_data_analysis/README.md)
This example shows how to use the LangChain pandas agent to perform data analysis on data read from a CSV file. This goes to show how LLMs can be used to orchestrate calculations using agents.

## License

MIT