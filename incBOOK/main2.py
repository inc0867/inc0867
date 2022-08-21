
from flask import *
from wtforms import *
from flask_mysqldb import *



app = Flask(__name__)


app.secret_key = "incBOOK"

app.config["MYSQL_HOST"] = "localhost"

app.config["MYSQL_USER"] = "root"

app.config["MYSQL_PASSWORD"] = ""

app.config["MYSQL_DB"] = "incBOOK"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"



mysql = MySQL(app)













class RegisterForm(Form):

    name = StringField("İsim Soyisim",validators=[validators.Length(min=4,max=25,message="4 ile 25 Arası Karakter Giriniz."),validators.DataRequired(message="Lütfen Bu Alanı Doldurunuz.")])

    email = StringField("Email Adresi",validators=[validators.DataRequired(message="Lütfen Bu Alanı Doldurunuz."),validators.Email(message="Geçerli Bir Email Adresi Giriniz...")])

    username = StringField("Kullanıcı Adı",validators=[validators.Length(min=5,max=35),validators.DataRequired(message="Lütfen Bu Alanı Doldurunuz.")])

    password = PasswordField("Parola",validators=[validators.DataRequired(),validators.EqualTo(fieldname="confirm",message="Parolalar Uyuşmuyor."),validators.DataRequired(message="Lütfen Bu Alanı Doldurunuz.")])

    confirm = PasswordField("Parola Tekrar")



class LoginForm(Form):

    username = StringField("Kullanıcı Adı")
    
    password = PasswordField("Parola")











@app.route("/")
def index():
    return render_template("index.html")



@app.route("/about")
def about():
    return render_template("about.html")






@app.route("/register",methods=["GET","POST"])

def regis():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

        cursor = mysql.connection.cursor()

        sorgu = "Insert into users(name,email,username,password) Values(%s,%s,%s,%s)"

        cursor.execute(sorgu,(name,email,username,password))

        mysql.connection.commit()

        flash("başarıyla kaydolundu","success")
        return redirect(url_for("login"))



    else:
        return render_template("register.html",form=form)



@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm(request.form)

    if request.method == "POST":

        username = form.username.data
        password_entered = form.password.data


        cursor = mysql.connection.cursor()




        sorgu = "SELECT * FROM users where username = %s"

        result = cursor.execute(sorgu,(username,))

        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]

            if real_password == password_entered:
                flash("başarıyla giriş yapıldı.Hoşgeldiniz "+username,"success")


                session["logged_in"] = True
                session["username"] = username

                #session kullanıcının oturumunn kaydedilmesidir.


                return redirect(url_for("index"))
            else:
                flash("Parolanız Yanlış","warning")
                return redirect(url_for("login"))


        else:
            flash("böyle bir kullanıcı yok!!","warning")

            
            return redirect(url_for("login"))
            

    return render_template("login.html",form=form)




@app.route("/profil")
def profil():
    username = session["username"]

    cursor = mysql.connection.cursor()

    sorgu =  "Select * From users where username = %s"

    cursor.execute(sorgu,(username,))

    data = cursor.fetchone()

    date = data["kayıtT"]

    cursor.close()

    

    cursor = mysql.connection.cursor()

    sorgu = "Select * From paylasım where author = %s"

    result = cursor.execute(sorgu,(username,))


    if result > 0:
        paylasımlar = cursor.fetchall()
        return render_template("profil.html",date=date,paylasımlar=paylasımlar)
    else:


        return render_template("profil.html",date = date)




@app.route("/cık")
def cık():
    session.clear()
    return redirect(url_for("index"))

@app.route("/Paylasımyap",methods=["GET","POST"])
def paylas():
    form = paylasım(request.form)


    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data

        cursor = mysql.connection.cursor()


        sorgu = "Insert into paylasım(title,author,content) VALUES(%s,%s,%s) "

        cursor.execute(sorgu,(title,session["username"],content))

        mysql.connection.commit()

        cursor.close()

        flash("Başarıyla paylaşıldı","success")

        return redirect(url_for("index"))
    else:
        return render_template("paylasımyap.html",form = form)




@app.route("/paylasımlar")
def paylasım():
    cursor = mysql.connection.cursor()

    sorgu = "Select * From paylasım"

    result = cursor.execute(sorgu)


    if result > 0:
        paylasımlar = cursor.fetchall()

        return render_template("paylasımsayfası.html",paylasımlar=paylasımlar)
    else:
        return render_template("paylasımsayfası.html")


@app.route("/friends")
def friends():
    cursor = mysql.connection.cursor()

    sorgu = "Select * From users"

    result = cursor.execute(sorgu)

    if result > 0:
        kullanıcılar = cursor.fetchall()

        return render_template("friends.html",kullanıcılar=kullanıcılar)

    else:

        return render_template("friends.html")




@app.route("/Chat/<string:id>",methods=["GET","POST"])
def Chat(id):
    form = message(request.form)

    if form.validate():
        mesaj = form.mesaj.data

        cursor = mysql.connection.cursor()

        sorgu = "Insert into chat(gonderen,alıcı,mesaj) Values(%s,%s,%s)"    


        cursor.execute(sorgu,(session["username"],id,mesaj))

        mysql.connection.commit()

        cursor.close()

        

    
        cursor = mysql.connection.cursor()

        sorgu = "Select * From chat"

        result = cursor.execute(sorgu)

     
        Chat = cursor.fetchall()

        return render_template("Chat.html",Chat=Chat,form=form,id = id)

        


    

        





class message(Form):
    mesaj = TextAreaField("Bir Mesaj girin",validators=[validators.length(max=400)])



class paylasım(Form):
    title = StringField("Paylaşımın Başlığı",validators=[validators.Length(min=4 ,max=20)])
    content = TextAreaField("Paylaşımın içeriği",validators=[validators.Length(min=10)])









if __name__ == ("__main__"):
    app.run(debug=True)