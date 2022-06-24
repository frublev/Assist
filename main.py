import json
from requests import get, post, patch, delete


def product_create(count):
    url_django = 'http://127.0.0.1:8000/api/v1/products/'
    data_ = {
        "title": f'Title{count}',
        "description": f'Description{count}'
    }
    return post(url_django, data=data_)


def product_upd(count):
    url_django = 'http://127.0.0.1:8000/api/v1/products/' + str(count) + '/'
    data_ = {
        "description": f'NewDescription{count}'
    }
    return patch(url_django, data=data_)


def product_delete(count):
    url_django = 'http://127.0.0.1:8000/api/v1/products/' + str(count) + '/'
    return delete(url_django)


def product_search(text):
    url_django = f'http://127.0.0.1:8000/api/v1/products/?search={str(text)}/'
    return get(url_django)


def stock_create(count):
    url_django = 'http://127.0.0.1:8000/api/v1/stocks/'
    data_ = {
        'address': f'address{count}',
        'positions': [
            {
                'product': 1,
                'quantity': 150
            }
        ]
    }
    return post(url_django, data=data_)


def measurement(sensor_, temperature):
    url_django = 'http://127.0.0.1:8000/api/measurements/'
    data_ = {
        "id_sensor": sensor_,
        "temperature": temperature
    }
    files = {'file': ('syn3.jpg', open('syn3.jpg', 'rb'), 'image/jpg')}
    return post(url_django, data=data_, files=files)


# product_create(9)
# product_upd(7)
product_delete(7)
# product_search(1)
# stock_create(2)

# measurement(18, 25.2)
