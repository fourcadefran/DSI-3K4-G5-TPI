from fastapi import FastAPI

app = FastAPI()

# todo: database model ? endpoints? clases?


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
