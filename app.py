import bs4
from urllib.request import urlopen  as uReq
from bs4 import BeautifulSoup as soup


def scraper_site(my_url):
	uClient=uReq(myUrl)
	page=uClient.read()
	uClient=close()

def parser(page):
	page_soup=soup(page,"html.parser")
	cards=page_soup.findAll("div",{"class":"item-container"})

def write_to_file(cards,filename):
	f=open(filename,"w")
	headers="brand,title,shipping\n"
	f.write(headers)
	for card in cards:
	
	brand=card.find("a",{"class":"item-brand"}).img["title"].replace(",","|")
	title=card.find("a",{"class":"item-title"}).text.replace(",","|")

	shipping=card.find("li",{"class":"price-ship"}).text.replace(",","|").strip()

	f.write(brand+","+title +","+shipping+"\n")

	f.close()

myUrl="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
uClient=uReq(myUrl)

page=uClient.read()
# dsa

uClient.close()

page_soup=soup(page,"html.parser")

cards=page_soup.findAll("div",{"class":"item-container"})

print(len(cards))

filename="products.csv"
f=open(filename,"w")
headers="brand,title,shipping\n"
f.write(headers)

for card in cards:
	
	brand=card.find("a",{"class":"item-brand"}).img["title"].replace(",","|")
	title=card.find("a",{"class":"item-title"}).text.replace(",","|")

	shipping=card.find("li",{"class":"price-ship"}).text.replace(",","|").strip()

	# f.write(brand,title,shipping)


	f.write(brand+","+title +","+shipping+"\n")



f.close()




