import requests
from datetime import datetime
from geopy import distance


logging = open('log.txt', 'w')


def get_location_destiny(destination):
    """
    :param destination: Set a location to find
    :return: Position of location
    """
    key = '47ec0d7d-ea0a-4a20-bcee-66b897ea33bb'  # Set your API Key
    url_api = f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode={destination}&format=json&lang=en_US'
    try:
        data_request = requests.get(url_api).json()
        pos_destiny = data_request['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        logging.write(f'{datetime.now} - Position: {pos_destiny}')
        return pos_destiny
    except IndexError:
        logging.write(f'{datetime.now} - ERROR: Address {destination} not find ')
    finally:
        pass


def validations_mkad(destination):
    key = '47ec0d7d-ea0a-4a20-bcee-66b897ea33bb'  # Set your API Key
    url_api = f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode={destination}' \
              f'&bbox=37.578,55.773~37.669,55.760&format=json&lang=en_US&rspn=1&kind=locality'
    data_request = requests.get(url_api).json()
    founds = data_request['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found']
    logging.write(f'founds')
    return int(founds)


def get_distance(destination):
    if validations_mkad(destination) != 0:
        return 'The specified address is located inside the MKAD'
    else:
        return distance.distance(get_location_destiny('Moscow Ring Road'), get_location_destiny(destination)).km
