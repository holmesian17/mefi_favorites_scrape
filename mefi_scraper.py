import bs4
import requests

url = "https://www.metafilter.com/favorites/169597/comments/ask/" #must be logged into mefi to access this page

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

