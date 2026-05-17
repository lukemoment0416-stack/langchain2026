import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

llm = ChatOpenAI(
    model="qwen-plus",
    api_key=os.getenv("aliQwen_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"}]

response = llm.invoke(messages)

print(response)