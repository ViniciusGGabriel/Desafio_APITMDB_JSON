# Importações
import pandas as pd
import requests as rq

# Constantes
API_KEY = "7f4cdcf564250599b852eca228dd9044"
URL_POPULAR = "https://api.themoviedb.org/3/person/popular?api_key=" + \
    API_KEY + "&language=en-US&page=1"

# Função que retorna o json da requisição


def get_popular_people():
    # Variável = lib.requisição tipo get(url)
    response = rq.get(URL_POPULAR)
    if response.status_code == 200:
        return response.json()
    else:
        return None

#   Função que retorna o dataframe da requisição


def get_popular_people_df():
    json = get_popular_people()
    if json is not None:
        df = pd.DataFrame(json['results'])
        return df
    else:
        return None


# Coloca o retorno da função dentro de um variável
data = get_popular_people_df()
# Cria o arquivo json com o nome popular_people
with open('popular_movies.csv', 'w') as f:
    f.write(data.to_json(orient='records', lines=True))
