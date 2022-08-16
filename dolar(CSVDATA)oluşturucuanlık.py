import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
import datetime


class veri(QWidget):
    def __init__(self):
        super().__init__()


        self.kontrol()


    def kontrol(self):
        self.yazı = QLabel("CSV dosyası oluşturun")
        self.bilgi = QLabel("Bilgilendirme:uygulama yazdığınız sayı kadar dolar verisini 5 sniyede bir çekcek not: PC hızına göre değişir")
     
        self.icerik = QLineEdit("Almak istediğiniz veri miktarını yazın")
        self.baslat = QPushButton("işlemi başlat")



        hb = QVBoxLayout()

        hb.addWidget(self.yazı)
        hb.addWidget(self.bilgi)
   
        hb.addWidget(self.icerik)
        hb.addWidget(self.baslat)

        vb = QHBoxLayout()

        vb.addLayout(hb)


        self.setLayout(vb)


        self.baslat.clicked.connect(self.islem)

        self.show()





    def islem(self):
        verisayı = self.icerik.text()
        

        verisayı = float(verisayı)


        othersayı = verisayı

        a = 0

 
        while a < verisayı:
            url = "https://www.google.com/finance/quote/USD-TRY?sa=X&ved=2ahUKEwjspNbd8sv5AhWlQvEDHa3EDXMQmY0JegQIAhAb"

            response = requests.get(url)

            html = response.content

            soup = BeautifulSoup(html,"html.parser")


            for i in soup.find_all("div",{"class":"YMlKec fxKbKc"}):
                verii = i.text

                dosya = open("dolardata.csv","a+")
                zaman = datetime.datetime.now()
                zaman = str(zaman)
                dosya.write(zaman)
                dosya.write(",")
                dosya.write(verii)
                dosya.write("\n")


                a += 1



        



















uygulama = QApplication(sys.argv)

pen = veri()


sys.exit(uygulama.exec_())
