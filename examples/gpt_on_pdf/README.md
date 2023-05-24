# GPT on PDF

This example shows how to use GPT to answer questions about a PDF document.

## Setup
Create a virtual environment and install the requirements:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make sure you set up the `OPENAI_API_KEY` environment variable, either with a .env file in the directory of this script or in your shell.

## Usage
Run the script with the path to the PDF file and the question:

```
python main.py data/us_gov_budget.pdf "what are some metrics of labor market health?"
```

```
-----------------
question: what are some metrics of labor market health?
answer:  Some metrics of labor market health include the unemployment rate, the median duration of unemployment, the long-term unemployment rate (U1), the number of workers who identify as marginally attached to the labor force, the number of discouraged workers, and the number of workers working part-time for economic reasons.
-----------------
```

```
python main.py data/us_gov_budget.pdf "what the hell is BBEDCA?"
```

```
-----------------
question: what the hell is BBEDCA?
answer:  BBEDCA stands for the Balanced Budget and Emergency Deficit Control Act of 1985.
-----------------
```
