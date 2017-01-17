from urllib2 import urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import random
import re
import json

fish_names = ['Heniochus acuminatus', 'Chaetodon auripes', 'Paracanthurus hepatus', 'Platax boersii']
image_folders = ['1. Heniochus+acuminatus', '2. Chaetodon+auripes', '3. Paracanthurus+hepatus', '4. Platax+boersii']

print fish_names
print '\n'.join(image_folders)

def getImageSource(fishImageUrl):
	html = urlopen(fishImageUrl).read()
	bsObj = BeautifulSoup(html)
	imageLocations = bsObj.find_all('li',{'class':'ld '})
	
	images = []
	for img in imageLocations:
		json_parse = json.loads(img['data'])
		images.append(json_parse.get('iurl'))

	return images

def downloadImage(imageLinks, image_folder):
	count = 0
	for img in imageLinks:
		count = count +1
		print count
		if(img.startswith('http://') | img.startswith('https://')):
			urlretrieve(img, '~/Fish_Pictures/'+image_folder+'/'+img.split("/")[-1])

folder_name_order = int(raw_input('Enter folder NO: '))

images = getImageSource(raw_input('Enter URL: '), )

downloadImage(images, image_folders[folder_name_order-1])
