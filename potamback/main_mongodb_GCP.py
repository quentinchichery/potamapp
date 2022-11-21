from flask import jsonify
import pymongo
import os

password = os.environ.get('atlas_password')

def hello_http(request):

  if request.method == 'OPTIONS':
    headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '3600'
    }
    return ('', 204, headers)

  headers = {
    'Access-Control-Allow-Origin': '*'
  }

  print(request)
  print(request.method)

  client = pymongo.MongoClient(
      f'mongodb+srv://Quentin:{password}@cluster0.k3273.mongodb.net/?retryWrites=true&w=majority')
  db = client.test
  collection = db["potamDB"]
  print('connected')

  def get_data(data):
      data['_id'] = str(data['_id'])
      return data

  data = request.get_json()
  print(data)
  
  if data['Type'] == []:
    data['Type'] = ["neobistrot","moyen_orient","brasserie","crepes","italien","brunch","asiatique","burger","gastronomique","boulangerie","bar","coffee_shop","primeurs","poissonerie","boucherie","cremerie","epicerie_fine","patisserie","vins","epices","sur_le_pouce","glace","vege","africain","indien","grec","chocolatier"]
  if data['Ville'] == []:
    data['Ville'] = ["75001","75002","75003","75004","75005","75006","75007","75008","75009","75010","75011","75012","75013","75014","75015","75016","75017","75018","75019","75020"]

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
  places = [get_data(i) for i in collection.find( r )]

  return (jsonify(places), 200, headers)