from bs4 import BeautifulSoup
import requests
import re

page = requests.get("https://7summitpathways.com/blog/mental-health-quotes/")

soup = BeautifulSoup(page.content, 'html.parser')

raw_list = soup.findAll('li')

new_list = [item.getText() for item in raw_list]

with open("Quotes.txt", 'w') as f:
    for string in new_list:
        match = re.search('“.+”\s—.+', string)
        if match:
            f.write(match.group() + "\n")
