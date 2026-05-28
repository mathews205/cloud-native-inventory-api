from fastapi import FastAPI

from app.routes import products


app = FastAPI()

app.include_router(products.router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
