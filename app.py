import bs4
from urllib.request import urlopen  as uReq
from bs4 import BeautifulSoup as soup

myUrl="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

myUrl='http://dl2.mojdl.com/upload/Tv-Series/Better%20Call%20Saul/S04/720p/'
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




