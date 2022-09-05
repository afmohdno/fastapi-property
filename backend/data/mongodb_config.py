from datetime import datetime
import pymongo
from pymongo import MongoClient
from time import mktime
import json

cluster = MongoClient(
	"mongodb+srv://tempuser:temppw@cluster0.ogoyfre.mongodb.net/?retryWrites=true&w=majority",
	tls=True,
	tlsAllowInvalidCertificates=True
	)

db = cluster["testdb"]