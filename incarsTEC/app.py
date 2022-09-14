from werkzeug.utils import secure_filename
from flask import *
import sqlite3


app = Flask(__name__)

app.secret_key  = "helllokkdddk"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kayıt",methods=["GET","POST"])
def kayıt():
    if request.method == "POST":
        isim = request.form.get("isim")
        email_i = request.form.get("email")
        sifre = request.form.get("sifre")


        vt = sqlite3.connect("incars.db")

        cursor = vt.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS uyeler(id INTEGER PRIMARY KEY AUTOINCREMENT,isim TEXT,email TEXT,sifre TEXT,resim TEXT,acıklama TEXT)"

        cursor.execute(sorgu) 

        vt.commit()
        vt.close()

        

        vt = sqlite3.connect("incars.db")

        cursor = vt.cursor()

        sorgu = "SELECT * FROM uyeler where isim = ?"

        cursor.execute(sorgu,(isim,))

        veri = cursor.fetchall()


        vt = sqlite3.connect("incars.db")

        cursor = vt.cursor()

        sorgu = "SELECT * FROM uyeler where isim = ?"

        cursor.execute(sorgu,(isim,))

        veri2 = cursor.fetchall()


        if len(veri) == 0 and len(veri2) == 0:

            if isim and email_i and sifre is not None:
                





            
                vt = sqlite3.connect("incars.db")

                cursor = vt.cursor()

                sorgu = "INSERT INTO uyeler(isim,email,sifre,resim,acıklama) VALUES(?,?,?,?,?)"

                resim = "https://as1.ftcdn.net/v2/jpg/01/74/35/40/1000_F_174354059_oegCS2Hmk3eTwTPCfoROZVDfbAh3Gp1v.jpg"

                cursor.execute(sorgu,(isim,email_i,sifre,resim,"acıklama yok"))

                vt.commit()
                vt.close()

                return redirect(url_for("index"))
            else: 

                bos = ""
                return render_template("kayıt.html",bos=bos)
            
        else:
            sonuc = "Bu kullanıcı adı veya email zaten kullanılıyor"
            return render_template("kayıt.html",sonuc=sonuc)
    else:
        
        return render_template("kayıt.html")

@app.route("/gir",methods=["GET","POST"])
def gir():
    if request.method == "POST":
        isim = request.form.get("isim")
        sifre = request.form.get("sifre")

        vt = sqlite3.connect("incars.db")

        cursor = vt.cursor()

        sorgu = "SELECT * FROM uyeler where isim = ? and sifre = ?"

        cursor.execute(sorgu,(isim,sifre))

        veri = cursor.fetchall()

        if len(veri) == 1:
            session["logged_in"] = True
            session["username"] = isim
            
            return render_template("index.html")
        else:
            sonuc = sonuc
            return render_template("gir.html",sonuc=sonuc)



    else:
        return render_template("gir.html")

@app.route("/cık")
def cik():
    session.clear()
    return render_template("gir.html")





@app.route("/Profil")
def profil():

    vt = sqlite3.connect("incars.db")

    cursor = vt.cursor()

    sorgu = "SELECT * FROM uyeler where isim = ?"

    isim = session["username"]

    cursor.execute(sorgu,(isim,))

    bilgi = cursor.fetchall()

    resim = bilgi[0][4]
    acık = bilgi[0][5]

    vt.commit()
    vt.close()




    return render_template("profil.html",resim=resim,acık=acık)




@app.route("/profilduzenle",methods=["GET","POST"])
def indexss():
    if request.method == "POST":
        isim = session["username"]
        acıklama = request.form.get("acıklama")
        resim = request.form.get("resim")

        if acıklama and resim == None:
            return render_template("Profil.html")

        elif acıklama == None:
            vt = sqlite3.connect("incars.db")

            cursor = vt.cursor()

            sorgu = "UPDATE uyeler SET resim = ?  where isim = ?"

            cursor.execute(sorgu,(resim,isim))

            vt.commit()
            vt.close()

            return render_template("profil.html")
        elif resim == None:
            vt = sqlite3.connect("inars.db")

            cursor = vt.cursor()

            sorgu = "UPDATE uyeler SET acıklama = ?  where isim = ?"

            cursor.execute(sorgu,(acıklama,isim))

            vt.commit()
            vt.close()

            return render_template("profil.html")

        elif resim and acıklama is not None:
            vt = sqlite3.connect("incars.db")

            cursor = vt.cursor()

            sorgu = "UPDATE uyeler SET acıklama = ?  where isim = ?"

            cursor.execute(sorgu,(acıklama,isim))

            vt.commit()
            vt.close()

            vt = sqlite3.connect("incars.db")

            cursor = vt.cursor()

            sorgu = "UPDATE uyeler SET resim = ?  where isim = ?"

            cursor.execute(sorgu,(resim,isim))

            vt.commit()
            vt.close()

            return render_template("profil.html")




        else:
            return render_template("index.html")

    else:

        isim = session["username"]
        return render_template("duzen.html",isim=isim)








@app.route("/kod",methods=["GET","POST"])
def kod():
    if request.method == "POST":
        veri = request.files['file']

        a = secure_filename(veri.filename)
        


        return render_template("kod.html",a=a)
    else:

        return render_template("kod.html")







if __name__ == "__main__":
    app.run(debug=True)