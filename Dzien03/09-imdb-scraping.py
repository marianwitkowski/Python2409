
# Scraping danych
import requests
import bs4

response = requests.get("https://www.imdb.com/chart/top/")
html_data = bs4.BeautifulSoup(response.text, features="lxml")
tbody = html_data.find("tbody", class_="lister-list")
rows = tbody.findAll("tr")
print(len(rows))
for row in rows:
    title = row.find("td", class_="titleColumn").find("a").text.strip()
    rating = row.find("td", class_="ratingColumn").text.strip()
    year = row.find("td", class_="titleColumn").find("span", class_="secondaryInfo").text.strip()[1:-1]
    _id = row.find("td",class_="posterColumn").findAll("span")[0].get("data-value")
    url = "https://www.imdb.com/" + row.find("td", class_="titleColumn").find("a").get("href")
    print(_id, title, year, rating, url, sep=";")

