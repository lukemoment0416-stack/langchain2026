import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="qwen-plus",
    api_key="sk-74304dab35e2488e8c0a24c54a79ca84",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# llm = ChatOpenAI(
#     model="deepseek-v4-pro",
#     api_key=os.getenv("aliQwen_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )

response = llm.invoke("你是谁")

print(response)
print()
print(response.content)