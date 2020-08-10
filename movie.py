class Movie:
    def __init__(self, title, rlsyr, runTime, genre, link):
        self.__title = title
        self.__rlsyr = rlsyr
        self.__runTime = runTime
        self.__genre = genre
        self.__link = link

    def printMovie(self):
        print('Movie Title: ', self.__title)
        print('Release Year: ', self.__rlsyr)
        print('Runtime: ', self.__runTime, ' mins')
        print('Genre: ', self.__genre)
        print('Link: ', self.__link)

    def getTitle(self):
        return self.__title

    def getRlsYr(self):
        return self.__rlsyr

    def getRunTm(self):
        return self.__runTime

    def getGenre(self):
        return self.__genre

    def getLink(self):
        return self.__link
