from flask import *
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():



    değişken = 1
    a = 0




    dolar = 0                                                                                         
    euro=0
    sterlin=0




    parabirimi_ata = [dolar,euro,sterlin]









    while değişken <= 3:
        urllist = ["https://www.google.com/finance/quote/USD-TRY?sa=X&ved=2ahUKEwiUnbCL1eb5AhVvQfEDHTKICM0QmY0JegQIAhAb","https://www.google.com/finance/quote/EUR-TRY?sa=X&ved=2ahUKEwig69Kl1-b5AhUvQvEDHfXpB2UQmY0JegQIAhAb","https://www.google.com/finance/quote/GBP-TRY?sa=X&ved=2ahUKEwjBq4yb2eb5AhW4XvEDHRYqANsQmY0JegQIAhAb"]
    
        paralist = ["dolar","euro","sterlin"]
    


        response = requests.get(urllist[a])



        html = response.content


        soup = BeautifulSoup(html,"html.parser")



        for i in soup.find_all("div",{"class":"YMlKec fxKbKc"}):
            para = i.text
            print(paralist[a],":",para)


            para = float(para)

            parabirimi_ata[a] = para


            print(parabirimi_ata)



        a +=1
        değişken +=1


    if request.method == "POST":
        ilkp = request.form.get("firstCurrency")
        ikip = request.form.get("secondCurrency")

        miktar = request.form.get("amount")
        miktar = float(miktar)


        if ilkp == "USD" and ikip == "TRY":
            sonuc = miktar * parabirimi_ata[0]
        elif ilkp == "USD" and ikip == "EUR":
            sonuc = (parabirimi_ata[0] / parabirimi_ata[1]) * miktar
        elif ilkp == "USD" and ikip == "GBP":
            sonuc = (parabirimi_ata[0] / parabirimi_ata[2]) * miktar
        elif ilkp == "EUR" and ikip == "TRY":
            sonuc = parabirimi_ata[1] * miktar
        elif ilkp == "EUR" and ikip == "USD":
            sonuc = (parabirimi_ata[1] / parabirimi_ata[0]) * miktar
        elif ilkp == "EUR" and ikip == "GBP":
            sonuc = (parabirimi_ata[1] / parabirimi_ata[2]) * miktar
        elif ilkp == "GBP" and ikip == "TRY":
            sonuc = parabirimi_ata[2] * miktar
        elif ilkp == "GBP" and ikip == "EUR":
            sonuc = (parabirimi_ata[2] / parabirimi_ata[1]) * miktar
        elif ilkp == "GBP" and ikip == "USD":
            sonuc = (parabirimi_ata[2] / parabirimi_ata[0]) * miktar
        elif ilkp == "TRY" and ikip == "USD":
            sonuc = (miktar /parabirimi_ata[0])
        elif ilkp == "TRY" and ikip == "EUR":
            sonuc = (miktar / parabirimi_ata[1])
        elif ilkp == "TRY" and ikip == "GBP":
            sonuc =(miktar / parabirimi_ata[2])
        else:
            pass
           
        return render_template("index.html",sonuc = sonuc)
    else:
        return render_template("index.html")
 
    











    



if __name__ == "__main__":
    app.run(debug=True)