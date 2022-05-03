from bs4 import BeautifulSoup
import requests
import json
import firebase_admin
from firebase_admin import credentials, firestore

# initialize sdk
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# initialize firestore instance
firestore_db = firestore.client()

# add data
#firestore_db.collection(u'beers').add({'name': 'Cerveza', 'price': '$1.000'})


website = 'https://www.jumbo.cl/vinos-cervezas-y-licores/cervezas'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify())

#box = soup.find('a', class_='shelf-product-title')
#title = box.find('h2').get_text()
#print(title)

data = {}

products = soup.find_all('div', class_='shelf-product-island')

for p in products:
    titleBox = p.find('h2', class_='shelf-product-title-text')
    title = titleBox.get_text()
    priceBox = soup.find('div', class_='prices-product')
    price = priceBox.find('span').get_text()
    #print(title + ' ' + price)
    data['name'] = title
    data['price'] = price
    json_data = json.dumps(data)
    print(json_data)
    #firestore_db.collection(u'beers').add({'name': title, 'price': price})

