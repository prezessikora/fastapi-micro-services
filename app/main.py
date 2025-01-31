import os
from typing import Annotated

from bson import ObjectId
from fastapi import FastAPI, Path, Response, Depends

from pymongo import MongoClient
from rich import status

from app.warehouse.domain.MusicRecord import MusicRecord

# set nu default in docker-compose URL or at container level
MONGO_DB_URL = os.environ.get("MONGO_DB_URL")
# default to localhost
if MONGO_DB_URL is None:
    MONGO_DB_URL = 'mongodb://localhost:27017'

client = MongoClient(MONGO_DB_URL)
db = client.test

app = FastAPI()

import pprint


# Products service
class MusicRecordsService:
    def find_music_record_by_id(self, product_id):
        collection = db.movie
        m = collection.find_one({"_id": ObjectId(product_id)})
        if m is None:
            return None
        else:
            return MusicRecord(str(m['_id']), m['title'], m['artist'], m['stock'], m['location'])


@app.get("/products/sku/{product_id}")
def get_product_by_sku(product_id: Annotated[str, Path(min_length=24, max_length=24)], response: Response, service: Annotated[MusicRecordsService, Depends(MusicRecordsService)]):
    m = service.find_music_record_by_id(product_id)
    if m is None:
        response.status_code = 404
        return {'message': f"Product not found"}
    else:  # we are returning internal domain object!
        return m


@app.get("/products/version")
async def version():
    return {"version": "1.0"}


# Customer service
@app.post("/customer")
async def create_customer():
    return {"message": "Customer Created"}


# Finance service

@app.get("/finance/reports/sales")
async def create_sales_report(name: str):
    return {"message": f"Hello {name}"}


# Orders service
@app.post("/orders/")
async def create_order():
    return {"message": "Order Created"}


# Called by payment service provider
# updates the order status and emits event to pick up by warehouse

@app.post("/orders/paid/{order_id}")
async def order_paid(order_id: str):
    return {"message": "Order paid"}

# Warehouse service

# Ship order that will listen for order paid message on rabbit MQ
