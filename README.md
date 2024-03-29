# GPTparser for OPENAI Fine-Tune API #
- GPTparser is a dataset creation tool to be used for OpenAI Fine-Tuning prep.
- GPTparser allows you to scrape and parse webpage text into formatted JSON Chat Completions files.
- OpenAI Fine-Tune API requires data to be in valid JSON, Chat Completions API format, with a .jsonl dataset where each line represents a unique JSON object containing a topic within a message array.

# GPTparser Overview #
- GPTparser works great for scraping / parsing text content directly from any website into individual JSON files.
- GPTparser is very simple to use:
	1. Recommended: Activate Miniconda Environment
	2. Recommended: export OpenAI API within Miniconda Session
	3. To use i.e.: GPTparser https://url.com output_file.json
- GPTparser script utilizes 'Few Shot Prompting', to adjust data output, adjust the examples & prompt (follow 'modifying for local use' directions).
	- Current prompt is carefully curated to accurately parse text into Chat Completions, JSON API.
 - I suggest utilizing Miniconda Envrionments for security & version / dependency control.
 	- FYI, for beginners this isn't required, and if you choose not to use these virutal environments then be sure to:
  		1. Install Dependency(1) & Dependency(2) below before using GPTparser
    		2. Securely activate your OpenAI API Key, and store it.



- **This was built using Linux Ubuntu, please adjust the below directions per your OS.**
- *GPTparser shares no professional affiliation with OpenAI.*

# Why #
- I created GPTparser because I couldn't find a tool that enabled me to efficiently scrape and parse content directly from URL's into structured JSON files.
- Working directly from your Linux CLI with individually parsed files allows for more granular control over the data.
- GPTparser was created for ease of use, to be cost effective, and to enable effective quality control to enhance access to OpenAI's Fine-tuning service and dataset curation techniques.
	1. GPTparser enables you to create a large 50k+ token dataset and finetune via OpenAI API for <$5.
- See the /scripts directory for further tools to help you format, validate, and combine these files into one dataset in proper Chat Completions JSON API format.
- I'd like to gather a small community of people interested in making complex AI workflows more accessible, & in the near future I'll be designing a website / UI to host this project.
	- If you're interested connecting, reach out! -- websitegithub.happily959@passinbox.com

# GPTparser Installation #
## Ubuntu Directions: ## 

- Clone repo and install the package:
	1. $ git clone git@github.com:dtflare/GPTparser.git
- Navigate into your cloned repo directory
  	1. $ cd GPTparser
- Choose **one of the two** below options to create a new Miniconda environment (Conda Env not required, but highly recommended):
  	1. $ conda env create -f environment.yml
  	2. $ conda create --name GPTparser python=3.8
- Activate environment
  	1. $ conda activate GPTparser
- Once in /GPTparser install the package/dependencies (Miniconda env recommended but not required)
	1. $ pip install .
- Export your OpenAI API Key within your Miniconda environment - will expire when session ends.
	- Must be done everytime you start Miniconda session / start using GPTparser
	1. $ export OPENAI_API_KEY=<enter_api_key>
- To use GPTparser - first create and cd into directory that will host your parsed files - then:
	1. $ GPTparser https://url.com output_file.json

- Anytime in the future where you use GPTparser, all you have to do is activate the correct Miniconda env, and export your API key.



### For those modifying the GPTparser for local use, follow directions below ###
- Adjust prompts as needed, currently it will output OPENAI's Chat Completions JSON format for Fine-Tuning.
	1. For those planning on editing the examples/prompt for different output, and/or create a new Miniconda Env.
- **Once changes are applied add GPTparser to $PATH.**
- Active Miniconda Environment
  	1. With YAML file in GPTparser repo:
  		- $ conda env create -f environment.yml
  	2. Create your own:
		- $ conda create --name GPTparser python=3.8
- Once GPTparser Miniconda session is activated, launch the below 1 & 2 dependencies.
  	1. If you use other Python tools within your Cona Env, launch the dependencies everytime at start of every session.
  	   	- For best results only don't use other tools within your GPTparser Conda Env.
	3. Dependency(1)
		- $ pip install langchain==0.1.4 deeplake openai==1.10.0 tiktoken
	4. Dependency(2), Langchain's newspaper module:
		- $ !pip install -q newspaper3k python-dotenv
- Add API KEY:
	1. $ export OpenAI_API_KEY
- mkdir & cd into parsed files host directory, then with GPTparser in $PATH:
	1. $ GPTparser https://url.com output_file.json
- IF GPTparser is not in $PATH, simply use:
	1. $ ./GPTparser https://url.com output_file.json


 
### Reminder ###
- To run GPTparser after installation, or once added to your global path:
	1. $ GPTparser website_url.com file_name.json
- OR:
	1. $ GPTparser website_url.com


## After you have used GPTparser to parse your webpages into documents, utilize the scripts in /scripts to turn them into a usable dataset. ##
**View comments inside individual scripts in /scripts for use directions**
- j_val = JSON validator for individual .json files within Directory
- combinR = combines all individual files into 1 .jsonl dataset
- wordcount = use to get accurate word count of your combined dataset

### Contributions ###
Please feel free to contribute! Whether it's code, directions etc. credit will always be given.
I'd like to create a small community of people interested in this line of work.

To contribute:

    Open a new issue to start a discussion around a feature idea or a bug.
    Fork the repo and start making your changes to a new branch.
    Include a test showing the fix & features working properly.
    Send a pull request!
    

Submit feature requests via the issues tab.
Submit Security Issues directly to my email: websitegithub.happily959@passinbox.com

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
