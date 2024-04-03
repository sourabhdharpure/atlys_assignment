import json
from abc import ABC, abstractmethod
from typing import List
from product import Product

class Storage(ABC):
    @abstractmethod
    def save(self, products: List[Product]):
        pass

class JsonStorage(Storage):
    _instance = None  # Class attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def save(self, products: List[Product], filename: str):
        data = [{"product_title": product.title, "product_price": product.price, "path_to_image": product.image_path} for product in products]
        with open(filename, 'w') as f:
            json.dump(data, f)

class DatabaseStorage(Storage):
    def save(self, products: List[Product]):
        # Implement database storage logic here
        pass
