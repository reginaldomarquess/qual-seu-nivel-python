from fastapi import FastAPI

app = FastAPI(
    title="Qual seu Nível em Python",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"Status": "OK"}
