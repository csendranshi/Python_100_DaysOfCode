from bs4 import BeautifulSoup
import requests

# with open("website.html", encoding="utf8") as file:
#     data = file.read()
#     # print(data)
#
# soup = BeautifulSoup(data, 'html.parser')
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = (response.text)
soup = BeautifulSoup(yc_webpage,"html.parser")
# print(soup.title)
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = (article_tag.get_text())
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [score.get_text().split()[0] for score in soup.find_all(name="span", class_="score")]
# print(article_texts,"\n",article_links,"\n", article_upvote)

highest_upvote = max(article_upvote)
highest_index = article_upvote.index(highest_upvote)

print(article_texts[highest_index])
print(article_links[highest_index])
print(article_upvote[highest_index])
