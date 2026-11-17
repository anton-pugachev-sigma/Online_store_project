from abc import ABC, abstractmethod
from typing import Any

class BaseProduct(ABC):
    """Абстрактный класс для общего представления продуктов"""

    @abstractmethod
    def __init__(self):
        super().__init__()
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product: dict[str, Any]):
        pass
