# atlys_assignment

This application Scrapes the Contents of a website and stores them locally in our System

Steps to run the Application

    pip install -r requirements.txt
    cd app
    python3 main.py



Application will start on localhost:8000

API/cURL to Scrape website and store results

`curl --location 'http://localhost:8000/scrape/?page_limit=1&proxy=null' \
--header 'Authorization: Bearer token'`

