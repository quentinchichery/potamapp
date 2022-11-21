
import pandas as pd
import json
from flask import Flask
import pymongo

connexion_string = ''

client = pymongo.MongoClient(
    connexion_string,
    connect=False)
db = client.test
db.drop_collection("potamDB")
collection = db["potamDB"]
print('connected')

def read_csv(filename):
    return pd.read_csv(filename, keep_default_na=False, converters={'Type': lambda x: x.split('/')}).to_dict('records')

# print(json.dumps(a, sort_keys=True, indent=4))

for item in read_csv('data - GOOGLE DRIVE.csv'):
    collection.insert_one(item).inserted_id

print('inserted')
