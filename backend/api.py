from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
from datetime import datetime as dt

from data.operations import *

class Prop(BaseModel):
	TITLE: str
	DATETIME_POSTED: dt
	TITLE: str
	PROPERTY_TYPE: str
	ADDRESS: str
	LOCATION_L1: str
	LOCATION_L2: str
	LOCATION_L3: str
	PRICE_RM_MIN: int
	PRICE_RM_MAX: int
	FEATURES: str
	FACILITIES: str
	BEDROOM: int
	BATHROOM: int
	BUILT_UP_SQFT: int
	CARPARK: int
	FURNISHING: str
	LAND_TITLE_TYPE: str
	TENURE: str

app = FastAPI()

origins = ["http://localhost:8080"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
	)

@app.get("/")
async def status():
	return { "status": "running"}

@app.get("/property")
async def get_properties():
	res = find_all()
	return Response(res)

@app.get("/property/{prop_id}")
async def get_property(prop_id:str = Path(None, description="Get property ID, show details")):
	res = find_by_id(prop_id)
	return Response(res)

@app.get("/property/name/{title}")
async def get_property_by_name(title:str = Path(None, description="Get property name, show details")):
	res = search_by_title(title)
	print(f"searching by title {title}")
	return Response(res)

@app.post("/property/")
async def add_property(prop: Prop):
	res = insert_single(prop)
	return Response(res)

@app.put("/property/{prop_id}")
async def update_property(prop_id:str):
	res = update_single(prop_id)
	return Response(res)

@app.delete("/property/{prop_id}")
async def delete_property(prop_id:str):
	res = delete_single(prop_id)
	return Response(res)
