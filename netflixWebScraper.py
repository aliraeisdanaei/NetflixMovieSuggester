from bs4 import BeautifulSoup
import requests
import random
import movie

recursionCounter = 0


class WebScraper:

    URL = 'https://www.finder.com/ca/netflix-movies'

    def __init__(self):
        response = requests.get(WebScraper.URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        self.__movieList = soup.find(class_='luna-table__body').findAll('tr')
        #print(len(self.__movieList), 'movies were found.')

        self.__movieListOg = self.__movieList
        random.shuffle(self.__movieList)

    def findNextMovie(self, crntUser):
        while True:
            if(len(self.__movieList) == 0):
                # break case no movies on the list. we have exhasted the list
                return None

            movie = WebScraper.getMovieFromCode(self.__movieList.pop())

            releaseYr = movie.getRlsYr()
            runTime = movie.getRunTm()
            genre = movie.getGenre()

            if (crntUser.getMinRlsYr() <= releaseYr and releaseYr <= crntUser.getMaxRlsYr()):
                if (crntUser.getMinRunTm() <= runTime and runTime <= crntUser.getMaxRunTm()):
                    if (not(genre in crntUser.getRejGen())):
                        return movie

    def reset(self):
        self.__movieList = self.__movieListOg
        random.shuffle(self.__movieList)

    @classmethod
    def getMovieFromCode(cls, movieCode) -> movie.Movie:
        # All of the movie titles are in <b> tags
        title = movieCode.find('b').get_text()
        rlsyr = int(movieCode.find(
            'td', {"data-title": "Year of release"}).get_text())
        runTime = int(movieCode.find(
            'td', {"data-title": "Runtime (mins)"}).get_text())
        genre = movieCode.find(
            'td', {"data-title": "Genres"}).get_text()
        # the link on the website is routed through itself, it needs to be split
        link = movieCode.find('a')['href'].split('=')[1]

        return movie.Movie(title, rlsyr, runTime, genre, link)
