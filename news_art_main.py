from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/news"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_text = [article.getText() for article in articles]

with open("news_article.txt", mode="w") as file:
    for num in range(len(article_text) - 1):
        news = f"{num + 1}). {article_text[num]}\n"
        file.write(f"{news}\n")



