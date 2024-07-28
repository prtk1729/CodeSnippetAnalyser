# CodeSnippetAnalyser
An end-to-end project leveraging LLMs, RAGs for source code analysis; enabling users to ask questions about the input repository:- analyze different files, and understand particular code snippets for improved code quality, bug detection, and optimization.


## STEP-01 Clone the repo
```bash
git clone https://github.com/prtk1729/CodeSnippetAnalyser.git
```

## STEP-02 Create a conda environment
```bash
conda create -n snip python=3.10 -y
```
```bash
conda activate snip
```

## STEP-03 Install all the required packages
```bash
pip3 install -r requirements.txt
```

## STEP-04 Create .env file and put the creds
Create a .env file in the root directory and add your OPENAI_API_KEY credentials as follows:
OPENAI_API_KEY = "xxxxxxxxx"

## STEP-05 Finally run the following command
python3 app.py

#### open up localhost:

### Techstack Used:
- Python
- LangChain
- Flask
- OpenAI
- GPT 3.5 Turbo
- ChoromaDB