# GPTparser for OPENAI fine-tune #
- GPTparser is a dataset creation tool to be used with OpenAI Fine-Tuning.
- OpenAI Fine-Tune API requires data to be in valid JSON, Chat Completions API format, with a .jsonl dataset where each line represents a unique JSON object containing a topic within a message array.

# GPTparser Overview #
- GPTparser works great for scraping / parsing text content directly from any website into individual JSON files.
- GPTparser is very simple to use:
	1. Recommended: Activate Miniconda Environment
	2. Recommended: export API within Miniconda Session
	3. To use i.e.: GPTparser https://url.com output_file.json
- GPTparser script utilizes 'Few Shot Prompting', to adjust data output, adjust the examples & prompt (follow 'modifying for local use' directions).
	- Current prompt is carefully curated to accurately parse text into Chat Completions, JSON API.
 - I suggest utilizing Miniconda Envrionments for security & version / dependency control.
 	- FYI, for beginners this isn't required, and if you choose not to use these virutal environments then be sure to:
  		1. Install Dependency(1) & Dependency(2) below before using GPTparser
    		2. Securely activate your OpenAI API Key, and store it.


## After you have used GPTparser to parse your webpages into documents, utilize the scripts in /scripts to turn them into a usable dataset. ##

- This was built using Linux Ubuntu, please adjust the below directions per your OS.
- *GPTparser shares no professional affiliation with OpenAI.*

# Why #
- I created GPTparser because I couldn't find a tool that enabled me to efficiently scrape and parse content directly from URL's into an output file.
- GPTparser was created for ease of use, to be cost effective, and to enable effective quality control.
	1. GPTparser enables you to create a large 60k+ token dataset and finetune via OpenAI API for <$5.
- GPTparser enables you to work directly from your Linux CLI, and having individual control over the files maximizes your ability to edit the content which = maximal quality.
- See the /scripts directory for further tools to help you format, validate, and combine these files into one dataset in proper Chat Completions JSON API format.


# GPTparser Installation #
## Ubuntu Directions: ## 

- Clone repo and install the package:
	1. $ git clone git@github.com:dtflare/GPTparser.git
- Create a new Miniconda environment, & apply the following settings:
  	1. $ conda create --name GPTparser python=3.8
- Activate environment
  	1. $ conda activate GPTparser
- Go into your cloned repo directory
  	1. $ cd GPTparser
- Once in /GPTparser install the package/dependencies (Miniconda env recommended but not required)
	1. $ pip install .
- Export your OpenAI API Key within your Miniconda environment - will expire when session ends.
	- Must be done everytime you start Miniconda session / start using GPTparser
	1. $ export OPENAI_API_KEY=<enter_api_key>
- T use GPTparser - first create and cd into directory that will host your parsed files - then:
	1. $ GPTparser https://url.com output_file.json

- Anytime in the future where you use GPTparser, all you have to do is activate the correct Miniconda env, and export your API key.



### For those modifying the GPTparser for local use, follow directions below ###
- Adjust prompts as needed, currently it will output OPENAI's Chat Completions JSON format for Fine-Tuning.
- For those planning on editing the examples/prompt for different output, and/or create a new Miniconda Env.

### Once changes are applied add GPTparser to $PATH. ###
- Active Miniconda Env.
- Once GPTparser Miniconda session is activated, launch both 1 & 2 dependencies everytime.
- Dependency(1)
	1. $ pip install langchain==0.1.4 deeplake openai==1.10.0 tiktoken
- Dependency(2), Langchain's newspaper module:
	1. $ !pip install -q newspaper3k python-dotenv
-Add API KEY:
	1. $ export OpenAI_API_KEY
-mkdir & cd into parsed files host directory, then with GPTparser in $PATH:
	1. $ GPTparser https://url.com output_file.json
-IF GPTparser is not in $PATH, simply use:
	1. $ ./GPTparser https://url.com output_file.json


 
 
### Reminder ###
- To run GPTparser after installation, or once added to your global path:
	1. $ GPTparser website_url.com file_name.json
- OR:
	1. $ GPTparser website_url.com

### /Scripts ###
# View individual scripts for use #
- j_val = JSON validator for individual .json files within Directory
- combinR = combines all individual files into 1 .jsonl dataset
- wordcount = use to get accurate word count of your combined dataset

### Contributions ###
Please feel free to contribute! Whether it's code, directions etc. credit will always be given.

To contribute:

    Open a new issue to start a discussion around a feature idea or a bug.
    Fork the repo and start making your changes to a new branch.
    Include a test showing the fix & features working properly.
    Send a pull request!
    

Submit feature requests via the issues tab.

### If you use GPTparser for your dataset please share it - or your experience - with the community! ###

### Citation ###
If you use GPTparser or associated tools to create a dataset or wish to refer to the baseline results published here, please use the following citation:

@dtflare{GPTparser,
author = {Daniel Flaherty},
title = {GPTparser},
year = {2024},
publisher = {GitHub},
journal = {GitHub repository},
howpublished = {\url{https://github.com/dtflare/GPTparser}}
}
