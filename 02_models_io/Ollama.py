import os

from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage

load_dotenv(override=True)

chatLLM = ChatTongyi(
    model="qwen-plus",
    api_key=os.getenv("aliQwen_API_KEY"),
    streaming=True,
)

print(chatLLM.invoke("你是谁？"))
res = chatLLM.stream([HumanMessage(content="你是谁？")], streaming=True)
for r in res:
    print("chat resp:", r.content)