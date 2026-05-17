import logging
import os

from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.exceptions import LangChainException

load_dotenv()

# config log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def init_llm_client() -> ChatOpenAI:
    """
    init llm client
    :return: llm client
    """

    # get configurations
    api_key = os.getenv("deepseek_API_KEY")
    if not api_key:
        raise ValueError("DeepSeek API key is required")

    # init chat client
    llm = ChatOpenAI(
        model="deepseek-v4-pro",
        api_key=api_key,
        base_url="https://api.deepseek.com",
        temperature=0.7,
        max_tokens=2048
    )
    return llm

def main():
    try:
        llm = init_llm_client()
        logger.info("LLM client initialized")

        # question = "Who are you?"
        # response = llm.invoke(question)
        #
        # logger.info(f"Question: {question}")

        # streaming invoke
        print("===========================streaming invoke=======")
        print("*" * 50)
        respStream = llm.stream("Can you introduce LanfChain within 300 characters?")
        for chunk in respStream:
            print(chunk.content, end="")
    except ValueError as e:
        logger.error(f"配置错误：{str(e)}")
    except LangChainException as e:
        logger.error(f"模型调用失败：{str(e)}")
    except Exception as e:
        logger.error(f"未知错误：{str(e)}")



# main entrance
if __name__ == "__main__":
    main()