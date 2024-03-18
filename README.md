### GPTparser for OPENAI fine-tune ###
- GPTparser is a tool for dataset creation to be used with OpenAI fine-tuning.
- OpenAI Fine-Tune API requires data to be in valid JSON, Chat Completions API format, with a .jsonl dataset where each line represents a unique JSON object containing a topic within a message array.

### GPTparser ###
- GPTparser works great for scraping / parsing text content directly from any website into individual JSON files.
- GPTparser is very simple to use:
	1. Recommended: Activate Miniconda Environment
	2. Recommended: export API within Miniconda Session
	3. To use EX: GPTparser https://url.com output_file.json
- GPTparser script utilizes 'Few Shot Prompting', to adjust output format adjust the examples & prompt.
	- Current prompt is carefully curated to accurately parse text into Chat Completions, JSON API.
 - I suggest utilizing Miniconda Envrionments for version / dependency control. This also makes it more secure to utilize your API key.
 	- For beginners this isn't required, and if you choose not to use these virutal environments then be sure to:
  		1. Install #1 & #2 dependencies below before using GPTparser
    		2. Securely activate your OpenAI API Key, and store it.

After you have used GPTparser to parse your webpages into documents, utilize the scripts in /scripts to turn them into a usable dataset.
	- See directions below at ### /scripts ###

This was built using Linux Ubuntu, please adjust the below directions per your OS.
*GPTparser shares no professional affiliation with OpenAI.*

### Why ###
I created GPTparser because I couldn't find a tool that enabled me to efficiently scrape and parse content directly from URL's into an output file.
I also created this with the goal and strategy of utilizing cost effective and quality control measures.
	- GPTparser enables you to create a large 60k word dataset and finetune via OpenAI API for <$5.
GPTparser enables you to work directly from your Linux CLI, and having individual control over the files maximizes your ability to edit the content which = maximal quality.
See the /scripts directory for further tools to help you format, validate, and combine these files into one dataset in proper Chat Completions JSON API format.


### GPTparser Installation ###
# Ubuntu Directions: # 

Clone repo and install the package:
$ git clone https://github.com/dtflare/GPTparser.git
Create a new Miniconda environment, & apply the following settings:
$ conda create --name GPTparser python=3.8
Activate environment
$ conda activate GPTparser
Go into your cloned repo directory
$ cd GPTparser
Once in /GPTparser install the package/dependencies:
	- Must be installed within activated Miniconda Environment (does not specifically require Miniconda)
$ pip install .
Export your OpenAI API Key within your Miniconda environment - will expire when session ends.
	- Must be done everytime you start Miniconda session / start using GPTparser
$ export OPENAI_API_KEY=<enter_api_key>
Use GPTparser, create and cd into directory that will host your parsed files, then:
$ GPTparser https://url.com output_file.json

- Anytime in the future where you use GPTparser, all you have to do is activate the correct Miniconda env, and export your API key.



### For those modifying the script for local use, follow directions below ###
Adjust prompts as needed, currently it will output OPENAI's Chat Completions JSON format for Fine-Tuning.
For those planning on editing the examples/prompt for different output, and/or create a new Miniconda Env.

Once changes are applied add GPTparser to $PATH, either in your .bashrc file, or include within a file in your $PATH
Active Miniconda Env
Launch both #1 & #2 dependencies everytime with a new GPTparser session.
Dependency #1:
$ pip install langchain==0.1.4 deeplake openai==1.10.0 tiktoken
Dependency #2, Langchain's newspaper module:
$ !pip install -q newspaper3k python-dotenv
Add API KEY:
$ export OpenAI_API_KEY
mkdir & cd into parsed files host directory, then with GPTparser in $PATH:
$ GPTparser https://url.com output_file.json
IF GPTparser is not in $PATH, simply use:
$ ./GPTparser https://url.com output_file.json


 
 
### Reminder ###
To run GPTparser after installation, or once added to your global path:
$ GPTparser website_url.com file_name.json
OR
$ GPTparser website_url.com

### /Scripts ###
# See individual scripts for use #
j_val = JSON validator for individual .json files within Directory
msg_array = adds Message array as needed to .json individual files
combine = combines all individual files into 1 .jsonl dataset
