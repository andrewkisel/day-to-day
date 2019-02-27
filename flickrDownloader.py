#! python3
# This app searches for the top interesting images in high res on Flickr depending on user input and downloads them.

import requests
import bs4
import os
import sys
import logging
import re

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

# Make sure search query is present and get it from command line args.
assert len(sys.argv) > 1, 'Search query is empty. Run the program like this: flickrDownload <searchquery>.'
query = ' '.join(sys.argv[1:])
# Make search URL
url = 'https://www.flickr.com/search/?text=' + query + '&media=photos&sort=interestingness-desc' + \
      '&dimension_search_mode=min&height=1024&width=1024'
# Create a new folder.
os.makedirs(query, exist_ok=True)
# Regex to find different types of URLs and parse them.
REX = re.compile(r'((//.*/)(\w+[^_]\w)(\.\w{3,4}))|((//.*/)(\w+[^_])(_\w))(\.\w{3,4})')
# Get the search results web page.
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Parse the web page and find items with specified class only.
items = soup.select('.photo-list-photo-view')

for i in items:
    # Get only 'style' attribute from the item.
    i = i.get('style')
    # Search for all regex matches.
    url_rex = REX.search(i)
    # Handle different types of URLs
    if url_rex.group(5):
        imgUrl = 'http:' + url_rex.group(6) + url_rex.group(7) + '_b' + url_rex.group(9)
    else:
        imgUrl = 'http:' + url_rex.group(2) + url_rex.group(3) + '_b' + url_rex.group(4)
    res = requests.get(imgUrl)
    # Write to files.
    imgFile = open(os.path.join(query, os.path.basename(imgUrl)), 'wb')
    print('Writing file %s' % os.path.basename(imgUrl))
    for chunk in res.iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()

print('Process complete!')
