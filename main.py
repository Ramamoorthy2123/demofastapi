from fastapi import FastAPI;

app = FastAPI();

@app.get("/")
def index():
    return{
        "msg": "Fastapi"
    }
@app.get("/about")
def index():
    return{
        "msg": "about"
    }
@app.get("/contact")
def index():
    return{
        "msg": "contact"
    }