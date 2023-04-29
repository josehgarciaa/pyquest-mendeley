import requests

url = "https://api.mendeley.com/oauth/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "scope": "all",
    "client_id": "15173",
    "client_secret": "fAmpTBEcnTMCWTtp"
}cp

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.text)

#from mendeley import Mendeley
#SECRET WOKnzJMLKhQ37XPG

# Reemplaza YOUR_CLIENT_ID y YOUR_CLIENT_SECRET con tus credenciales
#mendeley = Mendeley("15173", "WOKnzJMLKhQ37XPG")
#session = mendeley.start_client_credentials_flow().authenticate()

#def search_documents(query):
#    search_results = session.catalog.search(query).list(page_size=10)

#    for result in search_results.items:
#        print("Título: ", result.title)
#        print("Autores: ", ", ".join([author.last_name + ", " + author.first_name for author in result.authors]))
#        print("Año de publicación: ", result.year)
#        print("")

# Reemplaza "your_search_query" con la consulta que desees buscar
#search_documents("your_search_query")