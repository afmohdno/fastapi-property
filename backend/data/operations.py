from .mongodb_config import *
from bson import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
	def default(self,o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self,o)

def test_db():
	print(db)
	return "Test works"

def insert_many(datalist):
	op = db.properties.insert_many(datalist)
	if op.inserted_ids:
		return len(op.inserted_ids)
	else:
		return { "status": "failed", "message": "Properties not added"}

def insert_single(data):
	data = dict(data)
	result = db.properties.insert_one(data)
	if result.inserted_id:
		return "Property added"
	else:
		return { "status": "failed", "message": "Property not added"}

def find_all():
	if db.properties.count_documents():
		cursor = db.properties.find()
		data = JSONEncoder().encode(list(cursor))
		return data
	else:
		return { "status": "failed", "message": "None found"}

def search_by_title(title):
	search_regex = f"{title}"
	search_query = {
									"$or": [
										{"TITLE": {"$regex":search_regex, "$options": "i"}},
										{"ADDRESS" :{"$regex": search_regex, "$options": "i"}},
										{"LOCATION_L3" :{"$regex": search_regex, "$options": "i"}},
										]
									}
	if db.properties.count_documents(search_query):
		cursor = db.properties.find(search_query)
		data = JSONEncoder().encode(list(cursor))
		return data
	else:
		return { "status": "failed", "message": "None found"}

def find_by_id(item_id):
	_id = ObjectId(item_id)
	result = db.properties.find_one({"_id":_id})
	if result:
		data = JSONEncoder().encode(result)
		return data
	else:
		return { "status": "failed", "message": "None found"}

def update_single(item_id,data):
	_id = ObjectId(item_id)
	result = db.properties.update_one({"_id":_id}, {"$set": data})
	if result.matched_count > 0:
		data = JSONEncoder().encode(result)
		return { "message": "Data updated" }
	else:
		return { "status": "failed", "message": "None found"}

def delete_single(item_id):
	_id = ObjectId(item_id)
	result = db.properties.delete_one({"_id":_id})
	if result.deleted_count > 0:
		return "Property deleted"
	else:
		return { "status": "failed", "message": "Property not deleted"}