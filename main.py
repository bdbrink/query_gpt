import openai
import json
import os
import yfinance as yf

# use export command to generate
openai.api_key = os.environ['OPEN_API_KEY']


def run_conversation(user_message):
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "user", "content": user_message}]
    functions = [
        {
            "name": "get_stock_price",
            "description": "Get the stock price for a given ticket symbol",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "The ticker symbol for the company (eg. MSFT is microsoft)",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["ticker"],
            },
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_stock_price": get_stock_price,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            ticker=function_args.get("ticker")
        )

        # Step 4: send the info on the function call and function response to GPT
        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  # extend conversation with function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        return second_response

def get_stock_price(ticker):
    return str(yf.Ticker(ticker).history(period="1mo").iloc[-1].Close)

print(run_conversation("Give me the stock price for the best car company on the market"))
