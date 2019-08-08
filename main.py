from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import get
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Search(BaseModel):
    search_word: str

@app.post("/")
async def root(search: Search):
    return get.services_scrape(search.search_word)

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
