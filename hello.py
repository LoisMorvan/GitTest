import requests

def hello(name):
    if (name == ''):
        raise Exception("The name can not be empty !")
    if (len(name) > 30):
        raise Exception("The name can not have more than 30 characters !")
    return "Hello " + name

def findMovies():
    urlPeople = 'https://swapi.py4e.com/api/people/?search=Luke'
    dataPeople = requests.get(urlPeople)
    people = dataPeople.json()
    films = people['results'][0]['films']
    names = []
    for i in range(len(films)):
        urlFilm = people['results'][0]['films'][i]
        dataFilm = requests.get(urlFilm)
        film = dataFilm.json()
        names.append(film['title'])
    return names