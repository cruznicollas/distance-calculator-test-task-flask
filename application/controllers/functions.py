import requests
from geopy import distance
import logging

log_format = '%(asctime)s:%(filename)s:%(message)s'

logging.basicConfig(filename='distance_result.log',
                    filemode='w',
                    level=logging.INFO,
                    format=log_format)
logger = logging.getLogger('root')

key = '47ec0d7d-ea0a-4a20-bcee-66b897ea33bb'  # Set your API Key


def get_location_destiny(destination):
    """
    :param destination: Set a location to find
    :return: Position of location in coordinates
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
        logger.warning('ERROR: Address not find')
        return 'ERROR: Address not find'
    finally:
        pass


def validations_mkad(destination):  # Function to validate if destination is in inside MKAD
    url_api = f'https://geocode-maps.yandex.ru/1.x/?apikey={key}&geocode={destination}' \
              f'&bbox=37.578,55.773~37.669,55.760&format=json&lang=en_US&rspn=1'
    data_request = requests.get(url_api).json()
    founds = data_request['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData'][
        'found']
    return int(founds)


def get_distance(destination):
    """
    :param destination: Value received for web interface, for calculate the distance between point.
    :return: Distance in kilometers
    """
    coord1 = (37.623429, 55.766557)
    coord2 = get_location_destiny(destination)
    result = distance.distance(coord1, coord2).km
    logger.info(f'The distance between the coordinates {coord1} and {coord2} is {result:.2f}')
    return result
