import math
import os
import asyncio
from importlib import import_module
from time import sleep, time
from functools import reduce

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

import services

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


class Search(BaseModel):
    search_word: str


@app.post("/")
async def root(search: Search):
    async_get_product_funcs = []
    loop = asyncio.get_event_loop()
    # サービス毎にモジュールをimport
    for service_name in services.__all__:
        service_module = import_module("services." + service_name)
        async_get_product_funcs.append(loop.run_in_executor(None, service_module.get_product_info, search.search_word))
    # 非同期で商品情報を取得
    # [[],[],[]...]内の配列を一つに連結
    result = reduce(lambda x,y:x+y, await asyncio.gather(*async_get_product_funcs))
    
    # 価格が安い順にソート
    return sorted(result,
                  key=lambda product: product['price']
                  if product['price'] != None else math.inf)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug='true')

