import os

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv(override=True)

model = ChatDeepSeek(
    model="deepseek-v4-pro",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=os.getenv("deepseek_API_KEY"),
)

print(model.invoke("什么是langchain"))