import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(override=True)

model = init_chat_model(
    model="deepseek-v4-pro",
    api_key=os.getenv("deepseek_API_KEY"),
    base_url="https://api.deepseek.com"
)

print(model.invoke("你是谁？").content)