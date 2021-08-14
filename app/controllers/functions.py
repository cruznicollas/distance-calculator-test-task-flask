import requests
from datetime import datetime
from geopy import distance

logging = open('log.txt', 'w')
key = '47ec0d7d-ea0a-4a20-bcee-66b897ea33bb'  # Set your API Key


def get_location_destiny(destination):
    """
    :param destination: Set a location to find
    :return: Position of location
    """
    url_api = f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode={destination}&format=json&sco=longlat'
    try:
        coord = []
        data_request = requests.get(url_api).json()
        pos_destiny = data_request['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        pos_destiny = pos_destiny.split(' ')
        coord1 = float(pos_destiny[0])
        coord2 = float(pos_destiny[1])
        coord.append(coord1)
        coord.append(coord2)
        return tuple(coord)
    except:
        return 'ERROR: Address not find'
    finally:
        pass


def validations_mkad(destination):
    url_api = f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode={destination}' \
              f'&bbox=37.578,55.773~37.669,55.760&format=json&lang=en_US&rspn=1'
    data_request = requests.get(url_api).json()
    founds = data_request['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData'][
        'found']
    return int(founds)


def get_distance(destination):
    result = distance.distance(get_location_destiny('Moscow Ring Road'), get_location_destiny(destination)).km
    print(result)
    return result


print(validations_mkad(get_location_destiny('Moscow Ring Road')))