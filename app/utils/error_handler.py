from fastapi import HTTPException

def handle_api_error(response):
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data from external API.")