import pyshorteners as sh
from flask import Flask, request, render_template , Response,url_for
import json
app = Flask(__name__)
@app.route('/', methods =["GET", "POST"])
def index():
   return render_template("home.html")

def shortner(content):
   content=str(content)
   link = content
   s = sh.Shortener()
   print(s.tinyurl.short(link))
   she =s.tinyurl.short(link)
   f = open("demofile3.txt", "w+")
   f.write(she)
   f.close()

@app.route('/submit', methods =["GET", "POST"])
def submit():
   if request.method == "POST":
      content = request.form.get("content")
      print(content)
      shortlink=shortner(content)
      print(shortlink)
      submit.var=shortlink
   return render_template("home.html")

@app.route('/goback')
def goback():
   if request.method == 'POST':
      return redirect(url_for('signup'))
   return render_template('urldetails.html')

@app.route('/gg')
def gg():
   file1 = open("demofile3.txt","r+") 
   cont=file1.read()
   if request.method == 'POST':
      return redirect(url_for('urldetails'))
   return render_template('urldetails.html',mes=cont)



if __name__=='__main__':
   app.run(host="192.168.0.108",port="8000",use_reloader=True,debug=True)