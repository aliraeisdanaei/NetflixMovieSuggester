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

        # making a copy to keep as original
        self.__movieListOg = list(self.__movieList)
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

            if (int(crntUser.getMinRlsYr()) <= releaseYr and releaseYr <= int(crntUser.getMaxRlsYr())):
                if (int(crntUser.getMinRunTm()) <= runTime and runTime <= int(crntUser.getMaxRunTm())):
                    if (not(genre in crntUser.getRejGen())):
                        return movie

    def reset(self):
        print(len(self.__movieList), len(self.__movieListOg))

        # copying the original
        self.__movieList = list(self.__movieListOg)
        random.shuffle(self.__movieList)

    @classmethod
    def getMovieFromCode(cls, movieCode) -> movie.Movie:
        all_td = movieCode.findAll("td")
        # All of the movie titles are in <b> tags
        title = all_td[0].get_text()
        rlsyr = int(all_td[1].get_text())
        runTime = int(all_td[2].get_text())
        genre = all_td[3].get_text()
        # the link on the website is routed through itself, it needs to be split
        # link = movieCode.find('a')['href'].split('=')[1] # sadly the website no longer provides a link -- I have lazily depricated the link to this wikipedia article about the number 404
        link = 'https://en.wikipedia.org/wiki/400_(number)#404'

        return movie.Movie(title, rlsyr, runTime, genre, link)
