import requests
from bs4 import BeautifulSoup

URL = "https://www.popxo.com/article/best-web-series-of-all-time/"

response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())
all_movies = soup.find_all(name="h3")
# print(all_movies)

movie_titles = [movie.getText() for movie in all_movies]

with open("web_series.txt", mode="w") as file:
    for movie in range(len(movie_titles)):
        movies = f"{movie + 1}).{movie_titles[movie]}"
        file.write(f"{movies}\n")
