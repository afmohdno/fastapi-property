from data.operations import *
import json

# with open("data/property_listing.json") as file:
# 	properties = json.load(file)
# print(insert_many(properties))

# for item in db.properties.find():
# 	if "b'" in item["TITLE"]:
# 		fixed_title = item["TITLE"].replace("b'","").rstrip("'")
# 	elif '"b"' in item["TITLE"]:
# 		fixed_title = item["TITLE"].replace('"b""',"").rstrip('"')		
# 	else:
# 		print("no issue")
# 	db.properties.update_one(item, { "$set":{ "TITLE": fixed_title } } )

# for item in db.properties.find():
# 	if "b'" in item["ADDRESS"]:
# 		fixed_addr = item["ADDRESS"].replace("b'","").rstrip("'")
# 	elif '"b"' in item["ADDRESS"]:
# 		fixed_addr = item["ADDRESS"].replace('"b""',"").rstrip('"')		
# 	else:
# 		print("no issue")
# 	print(fixed_addr)
# 	db.properties.update_one(item, { "$set":{ "ADDRESS": fixed_addr } } )

# print(db.properties.distinct("BEDROOM"))
# print(db.properties.distinct("BATHROOM"))
# print(db.properties.distinct("BUILT_UP_SQFT"))

# for item in db.properties.find():
# 	BUILT_UP_SQFT = item["BUILT_UP_SQFT"].replace(",","")
# 	if BUILT_UP_SQFT == "":
# 		BUILT_UP_SQFT = 0
# 	else:
# 		BUILT_UP_SQFT = int(BUILT_UP_SQFT)
# 	print(BUILT_UP_SQFT)
# 	db.properties.update_one(item, {"$set": {"BUILT_UP_SQFT": BUILT_UP_SQFT}})