# NetflixMovieSuggester

This program is a simple web scraper that uses bs4 to read off of [this website](https://www.finder.com/ca/netflix-movies) all of the movies on netflix. 

The user can enter their preferances for which movies they would like to see, and the program will save these as a text file. Every time the program is run, the user can login to their account with their preferances saved. 
The movie recommendations are exhaustive. 

In case the website changes or there is a new website the scraper can be easily modified thanks to the modular design of the program. 

Here is a sample output of the text user interface:

```
****Netflix Movie Suggester****
***********Main Menu***********

Current User Name:  default 

(1) Suggest Movie
(2) Change Users
(3) View & Change Preferances
(4) Create New User
(5) About
(6) Quit
Enter Option: 1

*******Movie Suggestion********

Movie Title:  Mapplethorpe
Release Year:  2018
Runtime:  102  mins
Genre:  Biographical Dramas
Link:  http://www.netflix.com/watch/81017021

(1) Open Link & Quit
(2) Sugggest Another Movie
(3) Go back to main menu
Enter Option: 3
4025 4026

****Netflix Movie Suggester****
***********Main Menu***********

Current User Name:  default 

(1) Suggest Movie
(2) Change Users
(3) View & Change Preferances
(4) Create New User
(5) About
(6) Quit
Enter Option: 6
```
