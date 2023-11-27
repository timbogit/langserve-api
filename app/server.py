#!/usr/bin/env python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
add_routes(
    app,
    prompt | model,
    path="/joke",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

# to Start the server:
# uvicorn --port 8000 --host 127.0.0.1 app.server:app --reload
# or: heroku local --port 8000