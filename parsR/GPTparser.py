#!/usr/bin/env python3

# !pip install -q newspaper3k python-dotenv
# pip install langchain==0.1.4 deeplake openai==1.10.0 tiktoken

import sys
import warnings
import requests
from newspaper import Article
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI
import json

#wrapping script in main() for SETUPTOOLS entrypoint

def main():
    # Suppress UserWarnings
    warnings.filterwarnings("ignore")
   
    # Command line arguments handling
    if len(sys.argv) < 2:
        print("Usage: python parsR.py <URL> [output_file]")
        sys.exit(1)

    article_url = sys.argv[1]  # The URL from command line
    output_file = sys.argv[2] if len(sys.argv) > 2 else None  # Optional output file

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    session = requests.Session()

    try:
        response = session.get(article_url, headers=headers, timeout=10)
        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()
        else:
            print(f"Failed to fetch article at {article_url}")
            sys.exit(1)
    except Exception as e:
        print(f"Error occurred while fetching article at {article_url}: {e}")
        sys.exit(1)

    #####listing examples

    # Previously defined parts of the script remain unchanged

    # Define your examples as actual Python objects
    examples = [
        {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
        {"role": "user", "content": "What's the capital of France?"},
        {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}
    ]

    # Convert the examples list to a JSON string for inclusion in the prompt
    examples_json = json.dumps(examples, indent=4)

    # Preparing the prompt without using .format() for the examples
    prompt_start = "You are a very good assistant that parses each article's text into OpenAI fine-tune JSON format by adding a messages array at the beginning, along with roles and content  for System, User, and Assistant. Example 1 & 2 = correct format. \n\nExample 1 and 2:\n"
    prompt_end = f"\n\nHere's the article you want to summarize.\n\n==================\nTitle: {article.title}\n\n{article.text}\n==================\n\nParse previous article into OpenAI finetune format that is conversational. Without referencing the article, use the text to create realistic User questions, Assistant answers, and System messages. Assistant messages in the data = ideal responses. User messages in data = create questions a human may ask about the article's text. System messages in data = background information, never quoted directly as part of assistant responses, used to elevate data comprehension, response relevancy and quality."

    # Combining parts of the prompt with the examples_json string
    prompt = prompt_start + examples_json + prompt_end


    #####listing examples

    # Prepare the prompt with the article data
    prompt = """You are a very good assistant that parses each article's text into OpenAI fine-tune JSON format by adding a messages array at the beginning, along with  creating roles and content for System, User, and Assistant. Example 1 & 2 = correct format.


    Example 1 and 2:


    Here's the article you want to summarize.

    ==================
    Title: {article_title}

    {article_text}
    ==================

    Parse previous article into OpenAI finetune format: each message has a role (system, user, assistant), and content. Use article's text to create User questions, and Assistant answers in the dataset as they should be part a conversation. Assistant messages in the data = ideal responses. User messages in data = likely questions. System messages in data = background information, never quoted directly as part of assistant  responses, used to elevate data comprehension, response relevancy and quality.
    """.format(article_title=article.title, article_text=article.text)

    messages = [HumanMessage(content=prompt)]

    # Load the model and generate summary
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    summary = chat(messages)

    # Output handling
    if output_file:
        with open(output_file, 'w') as f:
            f.write(summary.content)
    else:
        print(summary.content)

# end of def main(): wrapper for entry point.
if __name__ == "__main__":
    main()
