import requests
from bs4 import BeautifulSoup

url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"  #dovizin çekilecek olan site


response = requests.get(url)

html_içerik = response.content

soup = BeautifulSoup(html_içerik,"html.parser")

for i in soup.find_all("span",{"class":"value up"}):
    kur = i.text
    
kur = kur.replace(",",".")

kur = float(kur)







print("dolar şuan (satış)",kur)


a = int(input("(not:(0 girerseniz tl yi dolara çevirirsiniz))dolarınız varsa eger dolar girin:"))


if a > 0:
    print(a,"dolar şuanda:",kur * a,"TL")
elif a < 0:
    b = int(input("TL giriniz:"))

    print(b,"TL şuanda ",b / kur, "dolar")
