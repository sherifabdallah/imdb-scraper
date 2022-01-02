import requests
from bs4 import BeautifulSoup
import csv
import re
import math
from itertools import zip_longest



URL = "https://www.imdb.com/search/title/?genres=action&after=WzkyMjMzNzIwMzY4NTQ3NzU4MDcsInR0MTM1Mjg0ODAiLDE5NDkwMV0%3D"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')


while True:
    def next_page():
        next_button = soup.find('a', {'class':'lister-page-next next-page'})['href']
        next_button = 'https://www.imdb.com' + next_button
        print(next_button)
        return next_button

    r = requests.get(next_page())
    soup = BeautifulSoup(r.content, 'html5lib')





    main = soup.find_all('div', {'class':'lister-item-content'})


    title_list = []
    certificate_list = []
    genre_list = []
    production_list = []
    year_list = []
    runtime_list = []
    stars_list = []


    for line in main:

        # Title
        title = line.find('a').text
        title_list.append(title)
        


        text_muted = line.find('p')

        # Certificate
        certificate = text_muted.find('span', {'class':'certificate'})
        if certificate != None:
            certificate = certificate.text
        else:
            certificate = 'None'
            
        certificate_list.append(certificate)

        

        # Genre
        genre = text_muted.find('span', {'class':'genre'}).text
        genre = str(genre).strip()
        genre_list.append(genre)

        # production
        production = text_muted.find('b')
        if production != None:
            production = production.text
        else:
            production = 'None'


        production_list.append(production)



        # year
        year = line.find('span', {'class', 'lister-item-year text-muted unbold'})

        year = year.text
        year = str(year)
        year = re.sub('\D', '', year)
        if len(str(year)) == 8:
            year = str(year)[0:4]
        year_list.append(year)

        
        


        # runtime
        runtime = text_muted.find('span', {'class':'runtime'})
        if runtime != None:
            runtime = runtime.text
        else:
            runtime = 'None'
        runtime_list.append(runtime)
        


        # stars
        stars = line.find('strong')
        if stars != None:
            stars = stars.text
            stars = float(stars)
            stars = int(stars)
        else:
            stars = 'None'
        stars_list.append(stars)
        






    file_list = [title_list, certificate_list, genre_list, production_list, year_list, runtime_list, stars_list]
    exported = zip_longest(*file_list)
    with open('main.csv', "a") as myfile:
        wr = csv.writer(myfile)
        # Title, Certificate, Genre, Production, Year, Runtime, Stars
        wr.writerows(exported)