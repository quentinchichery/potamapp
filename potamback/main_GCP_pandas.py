import pandas as pd
from flask import jsonify, Request

def filter_data(df, selected_types, selected_cities):
    # Convert type from list with / to array
    df['type'] = df['type'].apply(lambda x: x.split('/'))
    # Filter the DataFrame based on selected types and cities
    mask = (df['type'].apply(lambda x: any(item in x for item in selected_types)) &
            df['ville'].apply(lambda x: any(item in x for item in selected_cities)))
    filtered_df = df[mask]
    return filtered_df

def check_type(types):
    all_types = ["neobistrot","orient","brasserie","crepes","italien","brunch","asiatique","burger","gastronomique","boulangerie","bar","coffee","primeur","poissonerie","boucherie","cremerie","epicerie","patisserie","vins","epices","pouce","glace","vege","africain","indien","grec","chocolatier", "coeur", "the", "latino"]
    for typ in types:
        if typ not in all_types:
            print(f'Wrong type: {typ}')

def unitest_df(df):
    df['type'] = df['type'].apply(lambda x: x.split('/'))
    unit = df['type'].apply(lambda x: check_type(x))
    # to do
    return True

def load_df(csv_path):
    df = pd.read_csv(csv_path)
    # unitest_df(df)
    return df

def get_places(df, request):
    data = request.get_json()
    selected_types = data['type']
    selected_cities = data['ville']
    print(selected_types)
    print(selected_cities)

    if selected_types == []:
        selected_types = ["neobistrot",
                        "orient",
                        "brasserie",
                        "crepes",
                        "italien",
                        "brunch",
                        "asiatique",
                        "burger",
                        "gastronomique",
                        "boulangerie",
                        "bar",
                        "coffee",
                        "primeur",
                        "poissonerie",
                        "boucherie",
                        "cremerie",
                        "epicerie",
                        "patisserie",
                        "vins",
                        "epices",
                        "pouce",
                        "glace",
                        "vege",
                        "africain",
                        "indien",
                        "grec",
                        "chocolatier",
                        "latino",
                        "the",
                        "coeur"]
    if selected_cities == []:
        selected_cities = ["75001","75002","75003","75004","75005","75006","75007","75008","75009","75010","75011","75012","75013","75014","75015","75016","75017","75018","75019","75020"]

    if "75018" in selected_cities:
        selected_cities.extend(["93400", "92110"])
    if "75017" in selected_cities:
        selected_cities.extend(["92300", "92110"])
    if "75020" in selected_cities:
        selected_cities.append("93100")
    if "75012" in selected_cities:
        selected_cities.append("94300")
    if "75016" in selected_cities:
        selected_cities.extend(["75116", "92800"])
    
    filtered_df = filter_data(df, selected_types, selected_cities)
    json_data = filtered_df.to_json(orient='records')
    return json_data

def potam_api(request):
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
  data = request.get_json()
  print(data)
  df = load_df('data-20240305.csv')
  print("successfully load csv")
  json_data = get_places(df, request)
  return (jsonify(json_data), 200, headers)

if __name__ == "__main__":
    df = load_df('data-20240305.csv')
    request = Request({
        "ville": ["75017", "75018"],
        "type": ["coeur", "orient"]
    }, headers = {'Content-Type': 'application/json', 'charset': 'utf-8'})
    json_data = get_places(df, request)
    print(json_data)