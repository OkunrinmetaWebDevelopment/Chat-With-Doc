from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from crawling import get_all_subpages,get_vectorstore_from_url



def get_application():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = get_application()

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.get("/blockchain")
def get_blockchain_data():
    url = 'https://blockchain.info/latestblock'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch blockchain data.")
        return None


@app.get("/bitcoin")
def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
        return data
    else:
        print("Failed to fetch data.")
        return None

@app.get("/page-crawler")
def crawler():
    # Example usage:
    subpages = get_vectorstore_from_url('https://go2cam.scrollhelp.site/en/go2cam/V610/online-help-presentation')

    return  subpages


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




