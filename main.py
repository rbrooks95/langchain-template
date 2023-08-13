import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI()


def main():
    result = llm.predict("Give me all cities in NYC")
    print(result)


if __name__ == "__main__":
    main()
