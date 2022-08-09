import requests
import sys
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup

class dolaruyg(QWidget):
    def __init__(self):
        super().__init__()

        self.uyglm()

    def uyglm(self):
        self.dolar1 = QLabel("dolar : .........")
        self.gün = QPushButton("Güncelle")
        self.cevir = QLineEdit()
        self.sonuc = QLabel("...........")
        self.bas = QPushButton("Çevir")

        vb = QVBoxLayout()

        vb.addWidget(self.dolar1)
        vb.addWidget(self.gün)
        vb.addWidget(self.cevir)
        vb.addWidget(self.sonuc)
        vb.addWidget(self.bas)

        hb = QHBoxLayout()

        hb.addLayout(vb)

        self.setLayout(hb)

        self.gün.clicked.connect(self.aaa)

        self.bas.clicked.connect(self.bbb)

        self.setWindowTitle("dolar uygulaması")

        self.show()

    def aaa(self):
        url = "https://www.google.com/finance/quote/USD-TRY?sa=X&ved=2ahUKEwjUltL94Lf5AhUKXvEDHT7fBhYQmY0JegQIAxAb"

        response = requests.get(url)

        html = response.content

        corba = BeautifulSoup(html,"html.parser")


        for i in corba.find_all("div",{"class":"YMlKec fxKbKc"}):
            dolar2 = i.text


            self.dolar1.setText("Dolar şuanda :" + dolar2)


    def bbb(self):
        url = "https://www.google.com/finance/quote/USD-TRY?sa=X&ved=2ahUKEwjUltL94Lf5AhUKXvEDHT7fBhYQmY0JegQIAxAb"

        response = requests.get(url)

        html = response.content

        corba = BeautifulSoup(html,"html.parser")


        for i in corba.find_all("div",{"class":"YMlKec fxKbKc"}):
            dolar2 = i.text


        kullanıcı_deger = self.cevir.text()

        kullanıcı_deger = float(kullanıcı_deger)

       

        dolar2 = float(dolar2)

        sonuc = dolar2 * kullanıcı_deger

        dolar2 = str(dolar2)
        sonuc = str(sonuc)
        kullanıcı_deger = str(kullanıcı_deger)

        self.sonuc.setText(kullanıcı_deger + "Dolar şuanda " + sonuc + "TL")









uygulama = QApplication(sys.argv)

pencere = dolaruyg()

sys.exit(uygulama.exec_())
