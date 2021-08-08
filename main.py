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
    num_movies = len(movie_rows)
 


        #<class 'bs4.element.Tag'>  (each element is a class object, not a string)
        #print(type(movie_row))
        #* select_one() finds the first occurence of a certain tag and returns a **tag object**
        # title_column = movie_row.select_one('td.titleColumn')
    title = [movie_row.select_one('td.titleColumn a').get_text() for movie_row in movie_rows]
    
    year = [movie_row.select_one('td.titleColumn span.secondaryInfo').get_text() for movie_row in movie_rows]
    
    rating = [float(movie_row.select_one('td.ratingColumn strong').get_text()) for movie_row in movie_rows]
    
    actors_and_director = [movie_row.select_one('td.titleColumn a').attrs['title'] for movie_row in movie_rows]
    
    director = [director_item.split(',')[0] for director_item in actors_and_director]
    
    actors = [actor_item.split(',')[1:] for actor_item in actors_and_director]
#     return num_movies, title, year, rating, director, actors
        

# num_movies, title, year, rating, director, actors = main()

    # print(num_movies[0])
    # print(title[0])
    # print(year[0])
    # print(rating[0])
    # print(director[0])
    # print(actors[0])
    while True:
        prevent_infinite = 0
        rand_movie_idx = random.randrange(0, num_movies, 1)
        rand_movie = f'''                         
                        {title[rand_movie_idx]} {year[rand_movie_idx]},
                        rating: {rating[rand_movie_idx]}, 
                        director: {director[rand_movie_idx]}, 
                        actors: {actors[rand_movie_idx]}'''
        print(rand_movie)
        print('\n')
        user_input = input('Would you like to see another movie? (y/[n]) ').casefold()
        if user_input != 'y':
            break
        prevent_infinite += 1
        if prevent_infinite > 1000:
            print("infinite loop detected. exiting...")
            break


    #* random.randrange(start, stop, step)




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
