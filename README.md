### GPTparser for OPENAI fine-tune ###
GPTparser is a tool for dataset creation to be used with OpenAI fine-tuning.
OpenAI Fine-Tune API requires data to be in valid JSON, Chat Completions API format, with a .jsonl dataset where each line represents a unique JSON object containing a topic within a message array.

### GPTparser ###
GPTparser works great for scraping / parsing text content directly from any website into individual JSON files.
GPTparser is very simple to use:
	1. Recommended: Activate Miniconda Environment
	2. Recommended: Install both pip dependencies each time before use, see below
	3. To use EX: GPTparser https://url.com output_file.json
GPTparser script utilizes 'Few Shot Prompting', to adjust output format adjust the examples & prompt.
	- Current prompt is carefully curated to accurately parse text into Chat Completions, JSON API.

After you have used GPTparser to parse your webpages into documents, utilize the scripts in /scripts to turn them into a usable dataset.
	- See directions below at ### /scripts ###

This was built using Linux Ubuntu, please adjust the below directions per your OS.
GPTparser shares no professional affiliation with OpenAI.

### Why ###
I created GPTparser because I couldn't find a tool that enabled me to efficiently scrape and parse content directly from URL's into an output file.
I also created this with cost effective and quality control strategies in mind.
	- Enables you to create a large 60k word dataset and finetune for <$5
GPTparser enables you to work directly from your Linux CLI, and having individual control over the files at first maximizes quality and your ability to edit the content.
See the /scripts directory for further tools to help you format, validate, and combine these files into one dataset in proper Chat Completions JSON API format.


### GPTparser Installation ###
Directions Ubuntu: First - Clone repo and install the package:

$ git clone https://github.com/dtflare/GPTparser.git
$ cd GPTparser
Create a new Miniconda environment, & apply the following settings:
$ conda create --name myenv python=3.8
$ pip install .

Once Installed / Active Miniconda Env:
Launch both dependencies everytime with a new GPTparser session.
Dependency #1
$ pip install langchain==0.1.4 deeplake openai==1.10.0 tiktoken
Dependency #2 Langchain's newspaper module:
$ !pip install -q newspaper3k python-dotenv

Export your OpenAI API Key within your Miniconda environment - will expire when session ends.
	- Must be done everytime you start Miniconda session / start using GPTparser
$ export OPENAI_API_KEY=<enter_api_key>

Adjust prompts as needed, currently it will output OPENAI's Chat Completions JSON format for Fine-Tuning.

Optional: add GPTparser to $PATH, either in your .bashrc file, or include it within a file in your $PATH
 


To run GPTparser after installation or  once added to your global path:
$ GPTparser website_url.com file_name.json
OR
$ GPTparser website_url.com
