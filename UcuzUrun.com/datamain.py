from dataclasses import replace
from unicodedata import name
from flask import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as oto
import sqlite3
import time
import os

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        urun = request.form.get("urun")

        url = "https://www.amazon.com.tr/"

        

        browser = webdriver.Edge()

        browser.get(url)


        time.sleep(3)


        ara = browser.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']")

        ara.send_keys(urun)

        arabas = browser.find_element(By.XPATH,"//*[@id='nav-search-submit-button']")


        arabas.click()


        time.sleep(15)


        browser.close()

        url = "https://www.hepsiburada.com/"


        browser = webdriver.Edge()

        browser.get(url)

        time.sleep(3)

        ara = browser.find_element(By.XPATH,"//*[@id='SearchBoxOld']/div/div/div[1]/div[2]/input")

        ara.send_keys(urun)


        arabas = browser.find_element(By.XPATH,"//*[@id='SearchBoxOld']/div/div/div[2]")


        arabas.click()


        time.sleep(15)


        browser.close()

        url = "https://www.trendyol.com/butik/liste/2/erkek"


        browser = webdriver.Edge()


        browser.get(url)

        ara = browser.find_element(By.XPATH,"//*[@id='auto-complete-app']/div/div/input")


        ara.send_keys(urun)
        oto.press("enter")  #i use this because trendyol submit button xpath is i and its doesnt work.
        oto.press("enter")


        time.sleep(15)

        browser.close()














        return render_template("index.html",urun=urun)







    else:

        return render_template("index.html")


@app.route("/fiyattakipetme",methods=["GET","POST"])
def layout():
    if request.method == "POST":
        url = request.form.get("url")
        xpath = request.form.get("xpath")
        urun = request.form.get("urun")

        n_url = url

        browser = webdriver.Edge()

        browser.get(n_url)

        fiyat_n = browser.find_element(By.XPATH,xpath)

        fiyat = fiyat_n.text
        try:
            fiyat = fiyat.replace(".","")

        except:
            pass

        try:
            fiyat = fiyat.replace(",",".")
        except:
            pass

        

        browser.close()


        con = sqlite3.connect("urunvt.db")

        cursor = con.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS urunler(url TEXT,urun TEXT,fiyat TEXT,xpath TEXT,takip TEXT,degisim TEXT)")

        sorgu = "INSERT INTO urunler VALUES(?,?,?,?,?,?)"

        cursor.execute(sorgu,(url,urun,fiyat,xpath,"Takip et","degisim yok"))

        con.commit()
        con.close()







        



        return render_template("index2.html")
    else:
        con = sqlite3.connect("urunvt.db")

        cursor = con.cursor()

        sorgu2 = "SELECT * FROM urunler"

        cursor.execute(sorgu2)

        veriler = cursor.fetchall()

        return render_template("index2.html",veriler = veriler)


@app.route("/takipet/<string:id>")
def hedef(id):
    #id == urun adı auto increment kullanması gerekir teknikte ama bu daha beta olduğu için böyle bir yol izledim
    
    
    vt = sqlite3.connect("urunvt.db")

    cursor = vt.cursor()

    sorgu3 = "SELECT * FROM urunler where urun = ?"

    cursor.execute(sorgu3,(id,))

    veri = cursor.fetchone()

    url = veri[0]

    browser = webdriver.Edge()

    browser.get(url)

    xpath = veri[3]

    now_f = browser.find_element(By.XPATH,xpath)

    s_fiyat = now_f.text

    browser.close()

    try:
        s_fiyat = s_fiyat.replace(".","")

    except:
        pass

    try:
        s_fiyat = s_fiyat.replace(",",".")
    except:
        pass

        

    s_fiyat = float(s_fiyat)  #suanki fiyat inteneger

    vt_f = veri[2]

        

    vt_f = float(vt_f)  #veri tabanındaki fiyat

    if vt_f == s_fiyat:
        vt = sqlite3.connect("urunvt.db")

        cursor = vt.cursor()

        sorgu4 = "UPDATE urunler SET takip = ? where urun = ?"

            

        cursor.execute(sorgu4,("Takip ediliyor",id))


        vt.commit()
        vt.close()



            

            

        return render_template("index2.html")
    elif vt_f > s_fiyat:
        oto.alert(veri[1]+"adlı ürünün fiyatı düştü detaylar UcuzUrun.com'da")
        degisim = vt_f - s_fiyat  #değişim kat sayısı
        #veritabanını güncellemek
        vt = sqlite3.connect("urunvt.db")

        cursor = vt.cursor()

        sorgu4 = "UPDATE urunler SET fiyat = ? where urun = ?"

        s_fiyat = str(s_fiyat)

        cursor.execute(sorgu4,(s_fiyat,id))

        vt.commit()
        vt.close()

        vt = sqlite3.connect("urunvt.db")

        cursor = vt.cursor()

        sorgu4 = "UPDATE urunler SET takip = ? where urun = ?"

            

        cursor.execute(sorgu4,("Takip ediliyor",id))

        vt.commit()
        vt.close()

        vt = sqlite3.connect("urunvt.db")

        cursor = vt.cursor()

        degisim = str(degisim)

        sorgu5 = "UPDATE urunler SET degisim = ? where urun = ?"

        cursor.execute(sorgu5,(degisim,id))

        vt.commit()

        vt.close()






        return render_template("index2.html",degisim=degisim)
    elif s_fiyat > vt_f:
        oto.alert(veri[1]+"adlı ürünün arttı detaylar UcuzUrun.com'da")
        degisim = vt_f - s_fiyat#değişim kat sayısı
        #veritabanını güncellemek
        vt = sqlite3.connect("urunvt.db")

        cursor = vt.cursor()

        sorgu4 = "UPDATE urunler SET fiyat = ? where urun = ?"

        s_fiyat = str(s_fiyat)

        cursor.execute(sorgu4,(s_fiyat,id))

        vt.commit()
        vt.close()

        vt = sqlite3.connect("urunvt.db")

        cursor = vt.cursor()

        sorgu4 = "UPDATE urunler SET takip = ? where urun = ?"

            

        cursor.execute(sorgu4,("Takip ediliyor",id))

        vt.commit()
        vt.close()

        vt = sqlite3.connect("urunvt.db")

        cursor = vt.cursor()

        degisim = str(degisim)

        sorgu5 = "UPDATE urunler SET degisim = ? where urun = ?"

        cursor.execute(sorgu5,(degisim,id))

        vt.commit()

        vt.close()





        return render_template("index2.html",degisim=degisim)
    else:
        return render_template("baslat.html")

        
    


    

            



@app.route("/silbenii/<string:id>")
def layoutsof(id):
    vt = sqlite3.connect("urunvt.db")

    cursor = vt.cursor()

    sorgu = "DELETE * FROM urunler where urun = ?"

    cursor.execute(sorgu,(id,))

    vt.commit()
    vt.close()

    return render_template("index2.html")

        
@app.route("/yardım")
def video():
    return render_template("video.html")






    






if __name__ == ("__main__"):
    app.run(debug=True)