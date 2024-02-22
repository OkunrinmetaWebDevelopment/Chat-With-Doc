from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from ingest import get_vectorstore_from_url



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

@app.get("/page-crawler")
def crawler():
    # Example usage:
    subpages = get_vectorstore_from_url('https://go2cam.scrollhelp.site/en/go2cam/V610/online-help-presentation')

    return  subpages


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




