from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_webpage = (response.text)
soup = BeautifulSoup(movie_webpage, "html.parser")
# print(soup)
title_tags = soup.find_all(name="h3", class_="title")
all_titles = [title.text for title in title_tags]
print(all_titles)

with open("movies.txt", 'a', encoding="utf8") as file:
    for movie in all_titles[::-1]:
        file.write(movie+"\n")