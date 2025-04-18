import requests
from bs4 import BeautifulSoup

keyword = 'Sabonete-natura'
url = f"https://lista.mercadolivre.com.br/{keyword}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos os blocos de produto
    Layout = soup.find_all("ol", class_="ui-search-layout ui-search-layout--grid")

    products = soup.find_all("li", class_="ui-search-layout__item")

    data = []
    for product in Layout:
        item = products

        for product in item:

            title_tag = product.find("a", class_="poly-component__title")
            price_fraction = product.find("span", class_="andes-money-amount andes-money-amount--cents-superscript")
            brand_tag = product.find("span", class_="poly-component__brand")

            title = title_tag.text.strip() if title_tag else "Título não disponível"
            href = title_tag.get("href") if title_tag else "Link não disponível"
            price = price_fraction.text.strip() if price_fraction else "Preço não disponível"
            brand = brand_tag.text.strip() if brand_tag else "Marca não disponível"

            data.append({
                "Title": title,
                "Link": href,
                "Price": price,
                "Brand": brand
            })

    print(data[:1])  
else:
    print("Erro ao acessar a página.")
