import datetime
import glob


class User:
    def __init__(self):
        self.__name = "default"
        self.__fileName = 'users\\' + self.__name + '.txt'
        self.__minRunTm = 0
        self.__maxRunTm = 1000
        self.__minRlsYr = 1890
        self.__maxRlsYr = datetime.datetime.now().year
        self.__rejectedGenres = []

    def __savePreference(self):
        with open(self.__fileName, 'w') as userFile:
            userFile.write(self.__name)
            userFile.write('\n')
            userFile.write(str(self.__minRunTm))
            userFile.write('\n')
            userFile.write(str(self.__maxRunTm))
            userFile.write('\n')
            userFile.write(str(self.__minRlsYr))
            userFile.write('\n')
            userFile.write(str(self.__maxRlsYr))
            userFile.write('\n')

            rejGenStr = ''
            for genre in self.__rejectedGenres:
                rejGenStr += genre + ','
            userFile.write(rejGenStr.rstrip(','))

    def loadUserPref(self, newFileName):
        with open(newFileName, 'r') as userFile:
            self.__name = userFile.readline().replace('\n', '')
            self.__fileName = newFileName
            self.__minRunTm = int(userFile.readline())
            self.__maxRunTm = int(userFile.readline())
            self.__minRlsYr = int(userFile.readline())
            self.__maxRlsYr = int(userFile.readline())
            self.__rejectedGenres = userFile.readline().split(',')
            # print(self.__rejectedGenres)

    @classmethod
    def getAllUsers(cls) -> list:
        return glob.glob('users/*.txt')

    def getName(self):
        return self.__name

    def getMinRunTm(self):
        return self.__minRunTm

    def getMaxRunTm(self):
        return self.__maxRunTm

    def getMinRlsYr(self):
        return self.__minRlsYr

    def getMaxRlsYr(self):
        return self.__maxRlsYr

    def getRejGen(self):
        return self.__rejectedGenres

    def setName(self, name):
        self.__name = name
        self.__savePreference

    def setMinRunTm(self, minRunTm):
        self.__minRunTm = minRunTm
        self.__savePreference

    def setMaxRunTm(self, maxRunTm):
        self.__maxRunTm = maxRunTm
        self.__savePreference

    def setMinRlsYr(self, minRlsYr):
        self.__minRlsYr = minRlsYr
        self.__savePreference

    def setMaxRlsYr(self, maxRlsYr):
        self.__maxRlsYr = maxRlsYr
        self.__savePreference

    def setRejGen(self, rejectedGenres):
        self.__rejectedGenres = rejectedGenres
        self.__savePreference
