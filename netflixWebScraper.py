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

    def findNextMovie(self, user):
        while True:
            if(len(self.__movieList) == 0):
                # break case no movies on the list. we have exhasted the list
                return None

            movie = WebScraper.getMovieFromCode(self.__movieList.pop())

            releaseYr = movie.getRlsYr()
            runTime = movie.getRunTm()
            genre = movie.getGenre()

            if (user.getMinRlsYr() <= releaseYr and releaseYr <= user.getMaxRlsYr()):
                if (user.getMinRunTm() <= runTime and runTime <= user.getMaxRunTm()):
                    if (not(genre in user.getRejGen())):
                        return movie

    def reset(self, user):
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


# def suggestMovie(user):

#     response = requests.get('https://www.finder.com/ca/netflix-movies')
#     soup = BeautifulSoup(response.text, 'html.parser')

#     movieList = soup.find(class_='luna-table__body').findAll('tr')
#     print(len(movieList), 'movies were found.')
#     return findMovie(user, movieList)


# def findMovie(user, movieList):
#     global recursionCounter
#     if(recursionCounter > 500):
#         recursionCounter = 0
#         print('Something went wrong!')
#         print('It is possible that we have used too much resources trying to find a movie based on your narrow preferances.')
#         print('You can change your preferances or try the link to netflix yourself to find a movie.')
#         print('http://www.netflix.com')
#         return 'http://www.netflix.com'

#     movieIndex = random.randint(0, len(movieList))
#     movie = movieList[movieIndex]

#     # to see the full code of movie entry uncomment the line bellow
#     # print(movie)

#     try:
#         # All of the movie titles are in <b> tags
#         movieTitle = movie.find('b').get_text()
#         releaseYr = int(movie.find(
#             'td', {"data-title": "Year of release"}).get_text())
#         runTime = int(movie.find(
#             'td', {"data-title": "Runtime (mins)"}).get_text())
#         genre = movie.find('td', {"data-title": "Genres"}).get_text()
#         # the link on the website is routed through itself, it needs to be split
#         link = movie.find('a')['href'].split('=')[1]
#     except Exception as err:
#         # the source code of the website had an error we go onto another movie
#         print(type(err).__name__)
#         recursionCounter += 1
#         return findMovie(user, movieList)

#     # if the current movie is against the user's preferances it will pick another movie
#     if (not (user.getMinRlsYr() <= releaseYr and releaseYr <= user.getMaxRlsYr())):
#         recursionCounter += 1
#         return findMovie(user, movieList)
#     if (not (user.getMinRunTm() <= runTime and runTime <= user.getMaxRunTm())):
#         recursionCounter += 1
#         return findMovie(user, movieList)
#     if (genre in user.getRejGen()):
#         recursionCounter += 1
#         return findMovie(user, movieList)

#     print('Movie Title: ', movieTitle)
#     print('Release Year: ', releaseYr)
#     print('Runtime: ', runTime, ' mins')
#     print('Genre: ', genre)
#     print('Link: ', link)

#     # we reset the counter
#     recursionCounter = 0
#     return link
