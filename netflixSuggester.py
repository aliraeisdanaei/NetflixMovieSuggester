from bs4 import BeautifulSoup
import requests
import random
import datetime


class User:
    def __init__(self):
        self.minRunTm = 0
        self.maxRunTm = 10
        self.minRlsYr = 1890
        self.maxRlsYR = datetime.datetime.now().year


response = requests.get('https://www.finder.com/ca/netflix-movies')

soup = BeautifulSoup(response.text, 'html.parser')

movieList = soup.findAll('tr')


movieIndex = random.randint(0, len(movieList))
movie = movieList[movieIndex]

# to see the full code of movie entry uncomment the line bellow
# print(movie)

# All of the movie titles are in <b> tags
movieTitle = movie.find('b').get_text()
releaseYr = movie.find('td', {"data-title": "Year of release"}).get_text()
runTime = movie.find('td', {"data-title": "Runtime (mins)"}).get_text()
genre = movie.find('td', {"data-title": "Genres"}).get_text()
# the link on the website is routed through itself, it needs to be split
link = movie.find('a')['href'].split('=')[1]

print('Movie Title: ', movieTitle)
print('Release Year: ', releaseYr)
print('Runtime: ', runTime, ' mins')
print('Genre: ', genre)
print('Link: ', link)
