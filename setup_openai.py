import openai
import os

# Load your personal OPENAI API KEY from the .env file. 
# Don't forget to include the .env file in the .gitignore file to avoid sharing it.
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define a function that takes a prompt and returns the model's completion
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]