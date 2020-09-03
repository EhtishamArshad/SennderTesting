import requests


# function to hit Films API, get response and return Python List object
def get_films_list():
    try:
        return requests.get('https://ghibliapi.herokuapp.com/films').json()
    except requests.exceptions.RequestException as e:
        raise Exception(e)


# function to hit People API, get response and return Python List object
def get_people_list():
    try:
        return requests.get('https://ghibliapi.herokuapp.com/people').json()
    except requests.exceptions.RequestException as e:
        raise Exception(e)
