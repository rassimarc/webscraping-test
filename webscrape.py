from bs4 import BeautifulSoup
from lxml import etree


filehandle = open("templates/test.html", mode='r', encoding='utf-8')
soup = BeautifulSoup(filehandle, 'html.parser')
filehandle.close()
dom = etree.HTML(str(soup))
print("Ad: ",dom.xpath('//*[@id="body-wrapper"]/div/header[2]/div/div/div/div[4]/div[1]/div[2]/div/h1')[0].text)
print("Price: ",dom.xpath('//*[@id="body-wrapper"]/div/header[2]/div/div/div/div[4]/div[1]/div[2]/div/div[1]/div[1]/span[1]')[0].text)
