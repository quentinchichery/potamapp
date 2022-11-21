import json
from flask import Flask, jsonify, request
import pymongo
from bson.json_util import dumps
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
app.secret_key = "define secret key of your own choice"

connexion_string = ''

client = pymongo.MongoClient(
    connexion_string)
db = client.test
collection = db["potamDB"]
print('connected')

def get_data(data):
    data['_id'] = str(data['_id'])
    return data

@app.route("/", methods=['POST'])
def get_places():
    data = request.get_json()
    print(data['Type'])
    print(data['Ville'])

    if data['Type'] == []:
        data['Type'] = ["neobistrot","moyen_orient","brasserie","crepes","italien","brunch","asiatique","burger","gastronomique","boulangerie","bar","coffee_shop","primeurs","poissonerie","boucherie","cremerie","epicerie_fine","patisserie","vins","epices","sur_le_pouce","glace","vege","africain","indien","grec","chocolatier"]
    if data['Ville'] == []:
        data['Ville'] = ["75001","75002","75003","75004","75005","75006","75007","75008","75009","75010","75011","75012","75013","75014","75015","75016","75017","75018","75019","75020"]
    print(data['Type'])
    print(data['Ville'])

    if "75018" in data['Ville']:
        data['Ville'].extend(["93400", "92110"])
    if "75017" in data['Ville']:
        data['Ville'].extend(["92300", "92110"])
    if "75020" in data['Ville']:
        data['Ville'].append("93100")
    if "75012" in data['Ville']:
        data['Ville'].append("94300")
    if "75016" in data['Ville']:
        data['Ville'].extend(["75116", "92800"])

    if "sur le pouce" in data['Type']:
        data['Type'].append("sur_le_pouce")
    if "coffee shop" in data['Type']:
        data['Type'].append("coffee_shop")
    if "epicerie fine" in data['Type']:
        data['Type'].append("epicerie_fine")
    if "moyen orient" in data['Type']:
        data['Type'].append("moyen_orient")


    r = {"$and": [ {"Type": { "$in": data['Type'] } }, {"Ville": { "$in": data['Ville'] } }]}
    # {"Ville": {'$regex':'^75'}}
    places = [get_data(i) for i in collection.find( r )]

    # for place in places:
    #     print(place['numero'])
    #     if place['numero'] > 647:
    #         try:
    #             img_data = requests.get(place['photo']).content
    #             with open('./pictures/' + str(place['numero']) +'.jpg', 'wb') as handler:
    #                 handler.write(img_data)
    #         except:
    #             print(place['numero'])
    #     else:
    #         continue

    return jsonify(places) 

