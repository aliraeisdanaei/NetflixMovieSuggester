import netflixWebScraper
import user
import webbrowser
import sys
import os


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
        print('(3) Go to Menu')
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


def changeUser():
    print('\n**********Change User**********\n')

    option = '0'

    userList = user.User.getAllUsers()
    for i in range(len(userList)):

        with open(userList[i], 'r') as userFile:
            username = userFile.readline().replace('\n', '')
        print('({}) {}'.format(i + 1, username))

    print('(0) Go to Menu')
    option = input("Enter the number on the left to choose username: ")

    if(option == '0'):
        showMainMenu()
    if(not option.isdigit()):
        print('\nInvalid input. Try again.\n')
        changeUser()
    elif(not(0 < int(option) and int(option) <= len(userList) + 1)):
        print('\nInvalid input. Try again.\n')
        changeUser()
    else:
        crntUser.loadUserPref(userList[int(option) - 1])
        print('\nCurrent User Name has been changed to {}.\n'.format(
            crntUser.getName()))
        showMainMenu()


def showMainMenu():
    print('\n****Netflix Movie Suggester****')
    print('***********Main Menu***********\n')
    print('Current User Name: ', crntUser.getName(), '\n')

    option = '0'

    print('(1) Sugggest Movie')
    print('(2) Change Users')
    print('(3) View & Change Preferances')
    print('(4) Quit')

    option = input("Enter Option: ")
    if(option == '1'):
        giveMovie()

    elif(option == '2'):
        changeUser()
    elif(option == '3'):
        pass
    elif(option == '4'):
        sys.exit()
    else:
        print('\nInvalid input. Try again.\n')
        showMainMenu()


crntUser = user.User()
crntUser.loadUserPref('users\Ali.txt')

# the scraper needs to be created as a global variable
scraper = netflixWebScraper.WebScraper()


showMainMenu()
