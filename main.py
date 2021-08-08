import random
import requests

from bs4 import BeautifulSoup

URL = 'http://www.imdb.com/chart/top'


def main():
    response = requests.get(URL)
    #* response.text is like the text from right-clicking on the webpage and clicking "page source"
    #* 'html.parser' is the default web-scraping parser for BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    #first decide what you want to look for. in this case, year, title, actors, and rating
    #finding the right section can be difficult.  For example the element with the titleColum class
    # was on *line 926*, so it's best to use control+f to find the right element based on text on the orgininal page

    #* select() finds all occurences of a certain tag and returns a list 
    movie_rows = soup.select('tbody tr')
    #print(len(movie_rows))
    for movie_row in movie_rows:
        #<class 'bs4.element.Tag'>  (each element is a class object, not a string)
        #print(type(movie_row))
        #* select_one() finds the first occurence of a certain tag and returns a **tag object**
        # title_column = movie_row.select_one('td.titleColumn')
        title = movie_row.select_one('td.titleColumn a').get_text()
        print(title)
        year = movie_row.select_one('td.titleColumn span.secondaryInfo').get_text()
        print(year)
        rating = movie_row.select_one('td.ratingColumn strong').get_text()
        print(rating)
        actor = movie_row.select_one('td.titleColumn a').attrs['title']
        actor_list = actor.split(',')[1:]
        print(actor_list)
        # print(title_column.attrs.get('class'))  #* same as print(title_column['class'])
        # rating_column = movie_row.select_one('td.ratingColumn')
        # print(rating_column.text)
        # print(movie_row.text) #* contatins scattered text of all info (ratings, title, actors, year)
        
        # print(movie_row.attrs)
        # print(movie_row.attrs['class'])
        # print(movie_row.attrs['class'][0])
        # print(movie_row.attrs['class'][0] == 'titleColumn')
        # print(movie_row.attrs['class'][0] == 'ratingColumn')


if __name__ == '__main__':
    main()
