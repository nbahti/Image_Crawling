from urllib2 import urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import random
import re

fish_names = ['Heniochus acuminatus', 'Chaetodon auripes', 'Paracanthurus hepatus', 'Platax boersii']
image_folders = ['Heniochus+acuminatus', 'Chaetodon+auripes', 'Paracanthurus+hepatus', 'Platax+boersii']

#base_url = raw_input('Enter the base URL: -->  ')

random.seed(datetime.datetime.now())

def getImageSource(fishImageUrl):
	html = urlopen(fishImageUrl)
	bsObj = BeautifulSoup(html)
	#imageLocations = bsObj.findAll("img", {"src":re.compile("^(\.\.\/images\/species)")})
	imageLocations = bsObj.findAll("table")
	images = []
	#for img in imageLocations:
	#	images.append(img['src'])

	for table in imageLocations:
		for tr in table.findAll('tr'):
			for td in tr.findAll('td'):
				if(td.img is not None):
					images.append(td.img['src'])

	return images

def downloadImage(imageLinks, image_folder):
	count = 0
	for img in imageLinks:
		count = count +1
		print count
		if(img.startswith('http://')):
			urlretrieve(img, '/Users/expether/Documents/Fish_Image_Crawlling/Scrapy_Project/fishScrapy_beautifulSoap/Fish_Pictures/'+image_folder+'/'+img.split("/")[-1])
		else:
			urlretrieve('http://www.fishbase.org/photos/'+img, '/Users/expether/Documents/Fish_Image_Crawlling/Scrapy_Project/fishScrapy_beautifulSoap/Fish_Pictures/'+image_folder+'/'+img.split("/")[-1])


for fish_name in fish_names:
	images = getImageSource("http://www.fishbase.org/photos/thumbnailssummary.php?Genus="+fish_name.split()[0]+"&Species="+fish_name.split()[1])
	order = fish_names.index(fish_name)

	downloadImage(images, image_folders[order])
