import fastapi

app = fastapi.FastAPI()

@app.get("/")
def mainPage():
    return "Hello, World!"