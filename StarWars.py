import requests

def findMovies():
    dataPeople = requests.get('https://swapi.py4e.com/api/people/1')
    people = dataPeople.json()['films']
    names = []
    for film_url in films:
        dataFilm = requests.get(film_url)
        film = dataFilm.json()['title']
        names.append(film)
    return names