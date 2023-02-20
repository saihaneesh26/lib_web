import json
from flask import Flask, render_template, request
import pandas as pd
import os
port = int(os.environ.get('PORT', 5000))

app = Flask(__name__,template_folder="templates")
@app.route('/',methods=['POST','GET'])
def mainPage():
    if request.method=="POST":
        print(int(request.form.get("index")))
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTo9pcOAqd_-2v6taNNfEIMOsjJQ0pnDsPslujwdWbvKocIWhvfVVXnfL38kzq8-E-9oQVYvyZpRYMV/pub?output=csv'
    df = pd.read_csv(url).to_json(orient="records")
    return render_template("index.html",df=df)

    
@app.route('/view',methods=['POST','GET'])
def viewPage():
    if request.method=="POST":
        try:
            index = (request.form.get("link"))
            url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTo9pcOAqd_-2v6taNNfEIMOsjJQ0pnDsPslujwdWbvKocIWhvfVVXnfL38kzq8-E-9oQVYvyZpRYMV/pub?output=csv'
            df = pd.read_csv(url)
            if index=="-1":
                pageurl = df['Upload file'][0]
                print(pageurl)
            else:
                pageurl = index.split('id=')[1]
                pageurl = "https://drive.google.com/file/d/"+pageurl+"/preview allow='autoplay'"
            return render_template("view.html",pageurl=pageurl)
        except:
            return render_template("index.html")
    else:
        return render_template("view.html")

if __name__=='__main__':
    app.run(host='0.0.0.0', port=port, debug=True)


