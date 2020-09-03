import requests


def get_films_list():
    try:
        return requests.get('https://ghibliapi.herokuapp.com/films').json()
    except requests.exceptions.RequestException as e:
        raise Exception(e)


def get_people_list():
    try:
        return requests.get('https://ghibliapi.herokuapp.com/people').json()
    except requests.exceptions.RequestException as e:
        raise Exception(e)
