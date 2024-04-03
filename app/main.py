from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from settings import settings
from routes.scrape import router as scraping_router

app = FastAPI()

# Include scraping routes
app.include_router(scraping_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
