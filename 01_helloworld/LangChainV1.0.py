import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()


# model = init_chat_model(
#     model="qwen-plus",
#     model_provider="openai",
#     api_key=os.getenv("aliQwen_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )
#
# print(model.invoke("你是谁？"))

# model = init_chat_model(
#     model="deepseek-v4-pro",
#     model_provider="openai",
#     api_key=os.getenv("aliQwen_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )
#
# print(model.invoke("你是谁？"))

model = init_chat_model(
    model="deepseek-v4-pro",
    model_provider="deepseek",
    api_key=os.getenv("deepseek_API_KEY"),
    base_url="https://api.deepseek.com"
)

print(model.invoke(" "))