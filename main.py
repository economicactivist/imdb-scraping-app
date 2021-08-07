import random
import requests

from bs4 import BeautifulSoup

URL = 'http://www.imdb.com/chart/top'


def main():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_rows = soup.select('tbody tr')
    for movie_row in movie_rows:
        title_column = movie_row.select_one('td.titleColumn')
        print(title_column.text)
        rating_column = movie_row.select_one('td.ratingColumn')
        print(rating_column.text)
        # print(movie_row.text)
        # print(movie_row.attrs)
        # print(movie_row.attrs['class'])
        # print(movie_row.attrs['class'][0])
        # print(movie_row.attrs['class'][0] == 'titleColumn')
        # print(movie_row.attrs['class'][0] == 'ratingColumn')


if __name__ == '__main__':
    main()
    