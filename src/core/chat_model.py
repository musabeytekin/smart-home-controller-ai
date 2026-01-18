from functools import lru_cache

from langchain_core.language_models import BaseChatModel

from langchain_ollama import ChatOllama

@lru_cache
def get_chat_model() -> BaseChatModel:
    """Initialize and return the chat model."""


    llm = ChatOllama(
        model="gpt-oss:20b",
        temperature=0,
    )

    return llm

    
  