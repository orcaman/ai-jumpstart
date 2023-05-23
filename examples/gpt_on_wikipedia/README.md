# GPT on Wikipedia

This example shows how to use GPT to answer questions about a Wikipedia articles.

## Setup
Create a virtual environment and install the requirements:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make sure you set up the `OPENAI_API_KEY` environment variable, either with a .env file in the directory of this script or in your shell.

## Usage
Run the script specifying the Wikipedia search terms and the question:

```
python main.py "Oded Menashe" "when was Oded Menashe, the Israeli TV presenter, born? Who is he married to?"
```

```
-----------------
wikipedia search terms: Oded Menashe
question: when was Oded Menashe, the Israeli TV presenter, born? Who is he married to?
answer:  Oded Menashe was born on September 29, 1969. He is married to Israeli actress and former MTV Europe VJ Eden Harel.
-----------------

```
