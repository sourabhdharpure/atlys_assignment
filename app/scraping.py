from bs4 import BeautifulSoup
import requests
import os
from typing import List
from product import Product
from settings import settings

class Scraper:
    _instance = None  # Class attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.base_url = settings.WEBSITE_BASE_URL
            self.images_folder = settings.IMAGES_FOLDER_NAME
            if not os.path.exists(self.images_folder):
                os.makedirs(self.images_folder)

    def scrape_product_info(self, page_limit: int = None, proxy: str = None) -> List[Product]:
        # Scrapes product information from the website.
        products = []
        page = 1
        while page <= page_limit:
            url = f"{self.base_url}{page}/"
            response = requests.get(url, proxies={"http": proxy, "https": proxy} if proxy else None)
            response.raise_for_status()  
            soup = BeautifulSoup(response.content, 'html.parser')
            product_cards = soup.find_all('li', class_='product')
            if not product_cards:
                print(f"No product cards found on page {page}")
                break
            for product in product_cards:
                try:
                    product_info = self.extract_product_info(product)
                    products.append(product_info)
                except Exception as e:
                    print(f"Error extracting product information: {str(e)}")
            page += 1
        return products

    def extract_product_info(self, product) -> Product:
        # Extracts product information from a product card.
        title = product.find('h2', class_='woo-loop-product__title').text.strip()
        price_element = product.find('span', class_='woocommerce-Price-amount')
        price_text = price_element.bdi.get_text()
        price = float(price_text.strip('₹'))
        image_url = product.img['data-lazy-src']
        image_name = title.replace(' ', '_') + '.jpg'
        image_path = os.path.join(self.images_folder, image_name)
        with open(image_path, 'wb') as f:
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            f.write(image_response.content)
        return Product(title=title, price=price, image_path=image_path)
