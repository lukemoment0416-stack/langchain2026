import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# llm = ChatOpenAI(
#     model="qwen-plus",
#     api_key="sk-b6df0a42ceb049688a4ea1f5cb7e0145",
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )

llm = ChatOpenAI(
    model="deepseek-v4-pro",
    api_key=os.getenv("aliQwen_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response = llm.invoke("你是谁")

print(response)
print()
print(response.content)