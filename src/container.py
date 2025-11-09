from core.security_service import SecurityService
from services.default_security_service import DefaultSecurityService
from core.chat_model import get_chat_model
from core.climate_service import ClimateService
from core.lightning_service import LightningService
from services.default_climate_service import DefaultClimateService
from services.default_lightning_service import DefaultLightningService
from core.models.house import House
from core.house_data_provider import get_house
from langchain_core.language_models import BaseChatModel

class Container:

    def __init__(self) -> None:
        self.house: House = get_house()
        self.chat_model: BaseChatModel = get_chat_model()
        self.lightning_service: LightningService = DefaultLightningService(house=self.house)
        self.climate_service: ClimateService = DefaultClimateService(house=self.house)
        self.security_service: SecurityService = DefaultSecurityService(house=self.house)


container = Container()
