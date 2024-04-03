from fastapi import APIRouter, HTTPException, Header
from scraping import Scraper
from storage import JsonStorage
from settings import settings

router = APIRouter()
scraper = Scraper()  

@router.get("/scrape/")
def scrape_and_store_data(page_limit: int = 1, proxy: str = None, authorization: str = Header(None)):
    try:
        # Extract token from the authorization header
        if authorization is None:
            raise HTTPException(status_code=401, detail="Unauthorized")
        token = authorization.split(" ")[1]  # Assuming Bearer token format
        if token != settings.SECRET_TOKEN:
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        # Scraping products
        products = scraper.scrape_product_info(page_limit=page_limit, proxy=proxy)

        # Storing the scraped data using JSON storage
        json_storage = JsonStorage()
        json_storage.save(products, "scraped_data.json")

        return {"message": f"Scraped {len(products)} products and stored in scraped_data.json"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
