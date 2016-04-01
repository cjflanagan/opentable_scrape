
# coding: utf-8

# In[57]:
date = '2016-12-23'
url="http://www.opentable.com/bernheim-and-schwartz?DateTime="+date+"%2020%3A30&Covers=2&OnlyOffers=false&autocompleteName=Bernheim%20%26%20Schwartz&RestaurantIDs=166489&MetroId=8"
import urllib.request
from bs4 import BeautifulSoup
import requests


response = requests.get(url) #.post if its a post request


page_data.find_all('li', class_='dtp-results-times')


page_data = BeautifulSoup(response.text, "lxml")
page_data.prettify()

title_tag = page_data.find('title')
retaurant_name = title_tag.get_text()

times = page_data.findAll('a', class_="dtp-button")


times


times_list = []

for item in times:
        times_list.append(item.get_text())
        
print('List of times available: %s' % times_list)

