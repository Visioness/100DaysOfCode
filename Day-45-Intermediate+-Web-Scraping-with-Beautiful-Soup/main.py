from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
print(response)
content = response.text
soup = BeautifulSoup(content, "html.parser")

#article_tag = soup.select_one(selector=".titleline a")
#article_text = article_tag.getText()
#article_link = article_tag.get("href")
#article = soup.select_one(selector=".subline span")
#article_score = article.getText()


article_tags = soup.select(selector="tr.athing td.title > span.titleline > a")
subline_tag = soup.find_all(name="span", class_="score")

texts = []
links = []

for tag in article_tags:
    text = tag.getText()
    texts.append(text)
    link = tag.get("href")
    links.append(link)

scores = [int(tag.getText().split()[0]) for tag in subline_tag]

print(texts)
print()
print(links)
print()
print(scores)
print()
max_score = max(scores)
index = scores.index(max_score)
print(texts[index])
print()
print(links[index])
print()
print(scores[index])