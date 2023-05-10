# Prompt-Engineering-DeepLearningAI

This repo contains notebooks inspired by the [Prompt Engineering](https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/1/introduction) course by [DeepLearning.AI](https://www.deeplearning.ai/). You can find many examples of how to prompt engineer ChatGPT using the OPENAI API in order to optimally perform the desired functionality; eg sentiment analysis, translation, summarization, etc.

The notebooks from the course have been worked out and enriched. An additional notebook for code debugging has been produced.

Each notebook describes a functionality of ChatGPT and how to engineer the ideal Prompt in order to leverage it.

The following notebooks are included in the "src" folder:
- guidelines.ipynb
- chatbot.ipynb
- summarizing.ipynb
- expanding.ipynb
- code_debugging.ipynb
- chatbot.ipynb
- inferring.ipynb
- transforming.ipynb

## Installation

Install the required packages:

```
python -m pip install -r requirements.txt
```

Include your personal OPENAI API KEY in the .env folder (.env folder added to .gitignore), to avoid sharing publicly.

## Example

Example of prompting ChatGPT using the OPENAI API to debug code.

-   Code cell:

```
code="""
import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
 """

name_error="""NameError: name 'openai' is not defined"""

jupyter="""
import helper_function
print(openai.api_key)
 """

prompt = f""" Your task is to debug code that is supposed to prompt OPENAIN API to execute a random task. 

The Python module given below in delimiters is imported into the Jupyter notebook with the code given below in angled brackets. /
When attempting to run the code cell an error is returned. The error is given below in hash marks.

Python module: ```{code}```
Jupyter notebook code: <{jupyter}>
Error: ###{name_error}###
                    
"""

response = get_completion(prompt)
print(response)
```

- Output response by ChatGPT:

    ...
    
    To fix the error, we need to make sure that the openai module is imported in the Jupyter notebook code. We can do this by adding the line "import openai" before the print statement. The corrected code is given below:

    ```
    import openai
    import helper_function
    print(openai.api_key)
    ```
    This should resolve the NameError and allow the code to execute properly.

    ...



## Resources

[The art of prompt design](https://towardsdatascience.com/the-art-of-prompt-design-use-clear-syntax-4fc846c1ebd5)

[Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering#tutorials)