from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating  import Jinja2Templates 

templates  = Jinja2Templates(directory="templates")

app = FastAPI() 


@app.get("/" ) 
async def Index():
    return {
        "name": "Emma",
        "age":30,
        "sex":"Female"
        } 


@app.get("/home", response_class=HTMLResponse) 
async def Home(request:Request): 
    return templates.TemplateResponse("index.html", {"request":request})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="0000")