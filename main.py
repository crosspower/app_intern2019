from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import services
import os
from importlib import import_module

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
    # servicesディレクトリにあるサービス一覧を取得
    service_names_with_py = list(filter(lambda file_name: not ("__" in file_name), os.listdir('services')))
    service_names = [service.replace(".py","") for service in service_names_with_py]

    result = []
    for service_name in service_names:
        service_module = import_module("services."+service_name)
        
        result.extend(service_module.get_product_info(search.search_word))
    # 価格が安い順にソート
    return sorted(result, key=lambda product: product['price'])

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
