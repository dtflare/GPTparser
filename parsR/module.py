
import warnings
import requests
from newspaper import Article
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI
import json

# Suppress UserWarnings
warnings.filterwarnings("ignore")

def fetch_and_process_article(article_url, output_file=None):
    """
    Fetches an article from the given URL, processes it using LangChain, and either
    prints the result or saves it to a specified output file.

    Parameters:
    - article_url: URL of the article to process.
    - output_file: Optional; filename to save the processed output. If None, prints output.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    try:
        response = requests.get(article_url, headers=headers, timeout=10)
        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()
        else:
            print(f"Failed to fetch article at {article_url}")
            return
    except Exception as e:
        print(f"Error occurred while fetching article at {article_url}: {e}")
        return

    # Prepare the prompt with the article data
    prompt = generate_prompt(article)

    # Load the model and generate summary
    # Assuming the OPENAI_API_KEY is set in the environment or passed to the ChatOpenAI constructor
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    summary = chat([HumanMessage(content=prompt)])

    # Output handling
    if output_file:
        with open(output_file, 'w') as f:
            f.write(summary.content)
    else:
        print(summary.content)

def generate_prompt(article):
    """
    Generates a prompt for LangChain processing based on the provided article.

    Parameters:
    - article: The newspaper.article.Article object containing the fetched article.

    Returns:
    - A string representing the prompt to be used with LangChain.
    """
    examples = [
        {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
        {"role": "user", "content": "What's the capital of France?"},
        {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}
    ]
    examples_json = json.dumps(examples, indent=4)
    prompt_start = "You are a very good assistant that parses each article's message as a role, content, and optional name.\n\nExample 1 and 2:\n"
    prompt_end = f"\n\nHere's the article you want to summarize.\n\n==================\nTitle: {article.title}\n\n{article.text}\n==================\n\nParse previous article into OpenAI finetune format: each message has a role, content, and optional name. Each example in the dataset should be a conversation. Assistant messages in the data = ideal responses. User messages in data = likely questions. System messages in data = background information, never quoted directly as part of assistant responses, used to elevate data comprehension, response relevancy and quality."
    return prompt_start + examples_json + prompt_end
