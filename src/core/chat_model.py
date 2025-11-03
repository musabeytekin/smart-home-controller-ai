from functools import lru_cache
from langchain_openai import ChatOpenAI
from langchain_core.language_models import BaseChatModel

@lru_cache
def get_chat_model() -> BaseChatModel:
    """Initialize and return the chat model."""
    return ChatOpenAI(model="gpt-4.1")

    
  