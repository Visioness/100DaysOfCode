import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

film_tags = soup.select(".article-title-description__text > .title")
#print(film_tags)

film_names = [film.getText() for film in film_tags[::-1]]
films = "\n".join(film_names)

with open("movies.txt", "w") as file:
    file.write(films)