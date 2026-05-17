from langchain_ollama import ChatOllama

model = ChatOllama(
    base_url="http://localhost:11434",
    model="qwen:4b",
    reasoning=False
)

print(model.invoke("什么是langchain"))