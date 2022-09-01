
from PyQt5.QtWidgets import *
import sys

#not uygulama bir iddia üzerine 5 dakikada yapılmıştır o yüzden arayüzü fazla detaylandırılmamıştır
#kullanmak için !pip install PyQt5' yeterlidir

class uygulama(QWidget):
    def __init__(self):
        super().__init__()


        self.init_ui()

    def init_ui(self):
        self.yazı = QLabel("Asal sayı bulma uygulaması (basitleştirilmiş arayüz)")
        self.yazı2 = QLabel("Sayı girin:")
        self.input = QLineEdit("")
        self.buton = QPushButton("İşlemi yap")
        self.sonuc = QLabel("")

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazı)
        v_box.addWidget(self.yazı2)
        v_box.addWidget(self.input)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.sonuc)


        h_box = QHBoxLayout()

        h_box.addLayout(v_box)


        self.buton.clicked.connect(self.sayibul)


        self.setLayout(h_box)






        self.show()


    def sayibul(self):
        sayı = self.input.text()
        sayı = int(sayı)

        bolenler = []
        for i in range(2,sayı):
            if sayı % i == 0:
                bolenler.append(i)
        if sayı == 1:
            self.sonuc.setText("sayı asal değil")
        elif sayı == 2:
            self.sonuc.setText("sayı asal")
        elif sayı == 0:
            self.sonuc.setText("........")
        elif len(bolenler) == 0:
            self.sonuc.setText("sayı asal")
        else: 
            self.sonuc.setText("sayı asal değil")











uyg = QApplication(sys.argv)

pen = uygulama()

sys.exit(uyg.exec_())