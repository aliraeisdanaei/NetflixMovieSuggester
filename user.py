import datetime
import glob


class User:

    # oldest film in existence, Roundhay Garden Scene 1888 (https://en.wikipedia.org/wiki/Roundhay_Garden_Scene)
    OLDEST_RLSYR = 1888

    # this is from the longest movie ever made, Logistics 2012 (https://en.wikipedia.org/wiki/Logistics_(film))
    LONGEST_RUNTIME_POSSIBLE = 51420

    def __init__(self):
        self.__name = "default"
        self.__fileName = User.getFileNameByName(self.__name)
        self.__minRunTm = 1
        self.__maxRunTm = User.LONGEST_RUNTIME_POSSIBLE
        self.__minRlsYr = User.OLDEST_RLSYR
        self.__maxRlsYr = datetime.datetime.now().year
        self.__rejectedGenres = []

    @classmethod
    def getFileNameByName(cls, name: str) -> str:
        fileName = 'users/' + name + '.txt'
        return fileName

    @classmethod
    def createUser(cls, name, minRunTm, maxRunTm, minRlsYr, maxRlsYr, rjtGenres):
        tmpUser = cls()
        tmpUser.__name = name
        tmpUser.__fileName = 'users\\' + tmpUser.__name + '.txt'
        tmpUser.__minRunTm = minRunTm
        tmpUser.__maxRunTm = maxRunTm
        tmpUser.__minRlsYr = minRlsYr
        tmpUser.__maxRlsYr = maxRlsYr
        tmpUser.__rejectedGenres = rjtGenres.split(',')

        tmpUser.__savePreference()
        return tmpUser

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
            # print('the file has been updated')

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
    def getAllUserNames(cls) -> list:
        userList = glob.glob('users/*.txt')
        userNameList = []

        for user in userList:

            with open(user, 'r') as userFile:
                username = userFile.readline().replace('\n', '')
            userNameList.append(username)
        return userNameList

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

    def getRejGen(self) -> list:
        return self.__rejectedGenres

    def setName(self, name):
        self.__name = name
        self.__fileName = str(User.getFileNameByName(self.__name))
        self.__savePreference()

    def setMinRunTm(self, minRunTm):
        self.__minRunTm = minRunTm
        self.__savePreference()

    def setMaxRunTm(self, maxRunTm):
        self.__maxRunTm = maxRunTm
        self.__savePreference()

    def setMinRlsYr(self, minRlsYr):
        self.__minRlsYr = minRlsYr
        self.__savePreference()

    def setMaxRlsYr(self, maxRlsYr):
        self.__maxRlsYr = maxRlsYr
        self.__savePreference()

    def setRejGen(self, rejectedGenres: list):
        self.__rejectedGenres = rejectedGenres
        self.__savePreference()
