from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


def main():
    load_dotenv()

    # test our api key
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set. Please add your key to .env")
        exit(1)
    else:
        print("API Key set.")
        
    chat = ChatOpenAI(temperature=0.9)
    
    messages = [
        SystemMessage(content="You are a helpful assistant")
    ]
    
    print("Hello, I am ChatGPT CLI!")
    
    while True:
        user_input = input("> ")
        
        messages.append(HumanMessage(content=user_input))
        
        ai_response = chat(messages)
        
        messages.append(AIMessage(content=ai_response.content))
        
        print("\nAssistant:\n", ai_response.content)
        
        print("history: ", messages)
        
if __name__ == '__main__':
    main()