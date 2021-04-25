import bs4
import requests

url = "https://www.metafilter.com/favorites/169597/comments/ask/" #must be logged into mefi to access this page

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

block = soup.select('#copy')

print(block.attrs) # get the attribute for the more link

for copy in block:
  if 'a' in block.attrs:
    # open <a> "more" link to go to full comment
    # save everything within div class "comments"
    # save question title from previous page

    else:
      # download "#copy"
    
  

