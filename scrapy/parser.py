import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://www.chitai-gorod.ru/"
HOST2 = "https://kaktus.media/?lable=8&date=2022-05-07&order=time"




HEADESRS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}
@csrf_exempt
def get_html(url, params=''):
    reg = requests.get(url, headers=HEADESRS, params=params)
    return reg

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="product-card js_product js__product_card js__slider_item")
    book = []

    for item in items:
        book.append(
            {
                "title": item.find("div", class_="product-card__title js-analytic-product-title").get_text(strip=True),
                "image": item.find('div', class_="img-product-block js__img-product-block").find('img').get('src')
                # "image": item.find('a').find('img').get('svg')
            }
        )
    return book




@csrf_exempt
def parser_func():
     html = get_html(HOST)
     if html.status_code == 200:
         book = []
         for page in range(2, 3):
             html = get_html(HOST)
             book.extend(get_data(html.text))
         return book





@csrf_exempt
def get_html(url, params=''):
    r = requests.get(url, headers=HEADESRS, params=params)
    return r

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="ArticleItem")
    new = []

    for item in items:
        new.append(
            {
                "title": item.find("a", class_="ArticleItem--name").get_text(),
                "image": item.find('a', class_="ArticleItem--image").find('img').get('src')

            }
        )
    return new

@csrf_exempt
def parser_func2():
    html = get_html(HOST2)
    if html.status_code == 200:
         ranobe = []
         for page in range(2, 3):
             html = get_html(HOST2)
             ranobe.extend(get_data(html.text))
         return ranobe

