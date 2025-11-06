from chat_model import get_chat_model
from core.lightning_service import LightningService
from services.default_lightning_service import DefaultLightningService
from .models.house import House
from .house_data_provider import get_house
from langchain_core.language_models import BaseChatModel

class Container:

    def __init__(self) -> None:
        self.house: House = get_house()
        self.chat_model: BaseChatModel = get_chat_model()
        self.lightning_service: LightningService = DefaultLightningService(house=self.house)


container = Container()
