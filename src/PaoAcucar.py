import requests
import json

url = "https://api.vendas.gpa.digital/pa/search/search"
headers = {
    "Content-Type": "application/json"
}

all_products = []
page = 1
total_pages = None

while True:
    payload = {
        "terms": "azeite",
        "page": page,
        "sortBy": "relevance",
        "resultsPerPage": 12,  #Dentro de payload. Neste caso o site ja retorna uma api
        "allowRedirect": True,
        "storeId": 461,
        "customerPlus": True,
        "department": "ecom",
        "partner": "linx"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    if total_pages is None:
        total_pages = data.get("totalPages", 1)

    products = data.get("products", [])
    if not products:
        break

    all_products.extend(products)
    print(f"Página {page} de {total_pages} carregada com {len(products)} produtos.")

    if page >= total_pages:
        break
    page += 1

with open("produtos_azeite_pao_acucar.json", "w", encoding="utf-8") as f:
    json.dump(all_products, f, ensure_ascii=False, indent=2)

print(f"\nTotal de produtos coletados: {len(all_products)}")
print("Arquivo 'produtos_azeite_pao_acucar.json' salvo com sucesso!")
