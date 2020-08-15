import netflixWebScraper
import user
import webbrowser
import sys
import os
import datetime


# this is from the longest movie ever made, Logistics 2012 (https://en.wikipedia.org/wiki/Logistics_(film))
LONGEST_RUNTIME_POSSIBLE = 51420

# oldest film in existence, Roundhay Garden Scene 1888 (https://en.wikipedia.org/wiki/Roundhay_Garden_Scene)
OLDEST_RLSYR = 1888


def giveMovie():

    movie = scraper.findNextMovie(crntUser)

    print('\n*******Movie Suggestion********\n')

    if(movie == None):
        print('The list of movies has been exhasted with the current preferances.')
        print('You can change your preferances, or go to www.netflix.com to find your own movie.')
        link = 'http://www.netflix.com'
    else:
        movie.printMovie()
        link = movie.getLink()

    print('')

    option = '0'

    while option != '1' and option != '2' and option != '3':
        print('(1) Open Link & Quit')
        print('(2) Sugggest Another Movie')
        print('(3) Go back to main menu')
        option = input("Enter Option: ")
        if (option == '1'):
            webbrowser.open(link, new=1)
            sys.exit()
        elif(option == '2'):
            giveMovie()
        elif(option == '3'):
            showMainMenu()
        else:
            print('\nInvalid input. Try again.\n')


def createNewUser():
    global crntUser

    print('\n********Create New User********\n')

    name = inputName()

    runTimeTuple = inputRunTime()
    minRunTm = runTimeTuple[0]
    maxRunTm = runTimeTuple[1]

    rlsYrTuple = inputRlsYr()
    minRlsYr = rlsYrTuple[0]
    maxRlsYr = rlsYrTuple[1]

    rjtGen = inputRejGen()

    crntUser = user.User.createUser(
        name, minRunTm, maxRunTm, minRlsYr, maxRlsYr, rjtGen)
    showMainMenu()


def inputName() -> str:
    userNameList = user.User.getAllUserNames()
    while True:
        name = input('Enter Name: ')
        if name in userNameList:
            print('This username is taken. Choose a different one.')
        else:
            return name


def inputRejGen() -> str:
    rjtGen = ''
    while True:
        newGen = input(
            'Enter a genre you would not like to see. Enter q or quit to quit: ')
        if (newGen == 'q' or newGen == 'Q' or newGen == 'quit' or newGen == 'Quit'):
            return rjtGen
        else:
            if rjtGen == '':
                rjtGen = newGen
            else:
                rjtGen = rjtGen + ',' + newGen


def inputRunTime():
    minRunTm = 0
    maxRunTm = 0

    while True:
        minRunTm = input(
            'Enter the MINIMUM RUN TIME (mins): ')
        if(not minRunTm.isdigit()):
            print('Invalid Input. This field must be a digit.')
        elif(int(minRunTm) <= 0):
            print('Invalid Input. Entry must be greater than 0.')
        elif(int(minRunTm) > LONGEST_RUNTIME_POSSIBLE):
            print('No movie exists yet with that run time.')
        else:
            break

    while True:
        maxRunTm = input(
            'Enter the MAXIMUM RUN TIME (mins): ')
        if(not maxRunTm.isdigit()):
            print('Invalid Input. This field must be a digit.')
        elif(int(maxRunTm) <= 0):
            print('Invalid Input. Entry must be greater than 0.')
        elif(int(maxRunTm) > LONGEST_RUNTIME_POSSIBLE):
            print('No movie exists yet with that run time.')
        elif(int(maxRunTm) < int(minRunTm)):
            print('The maximum run time cannot be less than the minimum run time.')
        else:
            break

    return minRunTm, maxRunTm


def inputRlsYr():
    minRlsYr = 0
    maxRlsYr = 0

    while True:
        minRlsYr = input(
            'Enter the MINIMUM RELEASE YEAR: ')
        if(not minRlsYr.isdigit()):
            print('Invalid Input. This field must be a digit.')
        elif(int(minRlsYr) < OLDEST_RLSYR):
            print('No movie exists before this year.')
        elif(int(minRlsYr) > datetime.datetime.now().year):
            print('No movie can be retrieved from the future.')
        else:
            break
    while True:
        maxRlsYr = input(
            'Enter the MAXIMUM RELEASE YEAR: ')
        if(not maxRlsYr.isdigit()):
            print('Invalid Input. This field must be a digit.')
        elif(int(maxRlsYr) < 0):
            print('Invalid Input. Entry must be greater than 0.')
        elif(int(maxRlsYr) > datetime.datetime.now().year):
            print('No movie exists yet with that run time.')
        elif(int(maxRlsYr) < int(minRlsYr)):
            print(
                'The maximum release year cannot be less than the minimum release year.')
        else:
            break

    return minRlsYr, maxRlsYr


def changeUser():
    print('\n**********Change User**********\n')

    userNameList = user.User.getAllUserNames()

    if(len(userNameList) == 0):
        print('There are no users for you to choose from.')
        print('You must create a user first.')
        option = input('Press 1 to do so or any key to go back: ')
        if(option == '1'):
            createNewUser()
        else:
            showMainMenu()
    else:
        for i in range(len(userNameList)):
            print('({}) {}'.format(i, userNameList[i]))

        print('(M) Go back to main menu')
        option = input("Enter the number on the left to choose username: ")

        if(option == 'M' or option == 'm'):
            showMainMenu()
        if(not option.isdigit()):
            print('\nInvalid input. Try again.\n')
            changeUser()
        elif(not(0 <= int(option) and int(option) < len(userNameList))):
            print('\nInvalid input. Try again.\n')
            changeUser()
        else:
            crntUser.loadUserPref(user.User.getFileNameByName(
                userNameList[int(option)]))
            print('\nCurrent User Name has been changed to {}.\n'.format(
                crntUser.getName()))

            showMainMenu()


def showAboutPage():
    print('\n*************About*************\n')

    print('This project was thought of by Alireza Golband after suggesting to Ali Raeisdanaei')
    print('an application that would suggest movies to watch from Netflix.')
    print('The friends had found it cumbersome to find movies to watch together.')
    print('\nThis program works by scraping a website, and suggesting movies based on the user\'s preferances.')
    print('To read more about this project visit the repository and read its documentation.\n')

    print('(1) To visit directory & quit program.')
    print('(2) Go back to main menu')

    option = input('Enter Option: ')
    if(option == '1'):
        webbrowser.open(
            'https://github.com/aliraeisdanaei/NetflixMovieSuggester/blob/master', new=1)
        sys.exit()
    if(option == '2'):
        showMainMenu()
    else:
        print('\nInvalid input. Try again.\n')
        showAboutPage()


def changeRejGenres():
    print('\n*View & Change Rejected Genres*\n')

    rejGenres = crntUser.getRejGen()

    if (len(rejGenres) == 0):
        print('No genres have been recorded')
        option = input('Press 1 to add genres or any key to go back: ')
        if(option == '1'):
            inputRejGen()
        else:
            view_change_Prefs()
    else:
        for i in range(len(rejGenres)):
            print('({}) {}'.format(i, rejGenres[i]))

        print('(A) Add new genres')
        print('(B) Go back to View & Change Preferances')

        option = input('Enter Option: ')

        if(option == 'B' or option == 'b'):
            view_change_Prefs()
        if(option == 'A' or option == 'a'):
            newGenres = str(inputRejGen()).split(',')
            for genre in newGenres:
                rejGenres.append(genre)
            crntUser.setRejGen(rejGenres)
            changeRejGenres()

        if(not option.isdigit()):
            print('\nInvalid input. Try again.\n')
            changeRejGenres()
        elif(not(0 <= int(option) and int(option) < len(rejGenres))):
            print('\nInvalid input. Try again.\n')
            changeRejGenres()
        else:
            newGenre = input('Enter the new genre: ')
            rejGenres[int(option)] = newGenre
            crntUser.setRejGen(rejGenres)
            changeRejGenres()


def view_change_Prefs():
    print('\n***View & Change Preferances***\n')

    print('(1) Username: ' + str(crntUser.getName()))
    print('(2) Run Time:')
    print('\t Min: ' + str(crntUser.getMinRunTm()) + ' mins')
    print('\t Max: ' + str(crntUser.getMaxRunTm()) + ' mins')
    print('(3) Release Year:')
    print('\t Min: ' + str(crntUser.getMinRlsYr()))
    print('\t Max: ' + str(crntUser.getMaxRlsYr()))
    print('(4) Rejected Genres: ', end='')
    for genre in crntUser.getRejGen():
        print(genre + ' ', end='')
    print('\n(5) Go back to main menu')

    option = input('Enter Option: ')

    if(option == '5'):
        showMainMenu()
    if(not (crntUser.getName() in user.User.getAllUserNames())):
        print('You must create a user first.')
        option = input('Press 1 to do so or any other key to quit: ')
        if(option == '1'):
            createNewUser()
        else:
            showMainMenu()
    elif(option == '1'):
        crntUser.setName(inputName())
        view_change_Prefs()
    elif(option == '2'):
        runTimeTuple = inputRunTime()
        minRunTm = runTimeTuple[0]
        maxRunTm = runTimeTuple[1]
        crntUser.setMinRunTm(minRunTm)
        crntUser.setMaxRunTm(maxRunTm)
    elif(option == '3'):
        rlsYrTuple = inputRlsYr()
        minRlsYr = rlsYrTuple[0]
        maxRlsYr = rlsYrTuple[1]
        crntUser.setMinRlsYr(minRlsYr)
        crntUser.setMaxRlsYr(maxRlsYr)
    elif(option == '4'):
        changeRejGenres()
    else:
        view_change_Prefs()

    view_change_Prefs()


def showMainMenu():
    scraper.reset()
    print('\n****Netflix Movie Suggester****')
    print('***********Main Menu***********\n')
    print('Current User Name: ', crntUser.getName(), '\n')

    option = '0'

    print('(1) Sugggest Movie')
    print('(2) Change Users')
    print('(3) View & Change Preferances')
    print('(4) Create New User')
    print('(5) About')
    print('(6) Quit')

    option = input('Enter Option: ')
    if(option == '1'):
        giveMovie()

    elif(option == '2'):
        changeUser()
    elif(option == '3'):
        view_change_Prefs()
    elif(option == '4'):
        createNewUser()
    elif(option == '5'):
        showAboutPage()
    elif(option == '6'):
        sys.exit()
    else:
        print('\nInvalid input. Try again.\n')
        showMainMenu()


crntUser = user.User()

# the scraper needs to be created as a global variable
scraper = netflixWebScraper.WebScraper()


showMainMenu()
