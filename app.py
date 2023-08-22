from flask import Flask, render_template,url_for
from flask import request as req
import requests


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    #return "Hello world!!"
    return render_template("index.html")

@app.route("/summarize", methods = ["GET","POST"])
def summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": f"Bearer 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"}
        
        data = req.form["input_data"]

        maxl = int(req.form["maxL"])
        minl = maxl//4 #int(input())

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
	
        output = query({
	        "inputs": data,
	        "parameters":{"min_length":minl,"max_length":maxl},
        })[0]

        #print(output)
        return render_template("index.html",result=output['summary_text'])
    
    else:
        return render_template('index.html')




if __name__ == '__main__':
    app.debug= True
    app.run()
#set FLASK_APP=api.py 
#$env:FLASK_APP = "api.py" 

#flask run