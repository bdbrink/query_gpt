# Query GPT

## Description

`main.py` is a Python script that utilizes the OpenAI GPT-3.5 language model to generate responses based on user queries. It serves as a basic example of how to interact with the GPT-3.5 API using the OpenAI Python library.

## Prerequisites

To use this script, you need to have the following:

- Python 3.x installed on your system
- OpenAI Python library (you can install it using `pip install openai`)

Additionally, you need an OpenAI API key to authenticate your requests. You can obtain the API key by signing up for OpenAI's GPT-3.5 API.

## Usage

1. Clone the repository and navigate to the project directory.
- git clone https://github.com/bdbrink/query_gpt.git
- cd query_gpt

2. Install the required dependencies.
- `pip3 install -r requirements.txt`


3. Set up your OpenAI API key as an environment variable. Replace `YOUR_API_KEY` with your actual API key.
- `export OPENAI_API_KEY=YOUR_API_KEY`


4. Open `main.py` in a text editor and modify the `query` variable with your desired query text.

```python
# Example configuration
query = "What is the capital of France?"
temperature = 0.5
max_tokens = 50
```