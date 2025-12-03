from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
KEY= os.environ["API_KEY"]


while True:

    # create a client
    client = OpenAI(api_key=KEY)

    question =input("Ask me anything: ")

    if question !='bye':


        response =client.chat.completions.create(
            model="gpt-3.5-turbo", 
            max_tokens=50, # limit the response to 50 tokens
            n=1,  # number of responses to generate
            temperature=0, # creativity of the response 
            messages=[
                {"role": "user", "content": question}
            ]   
        )
        # print(response)

        for choice in response.choices:
            print(choice.message.content)
    else:
        print("Goodbye!")
        break