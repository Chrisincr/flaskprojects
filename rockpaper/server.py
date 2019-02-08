from flask import Flask, render_template, request, redirect
import random
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def get_result():
    print(request.form)
    input_from_form= request.form['result']
    options=["rock", "paper", "scissors"]
    random_option=random.choice(options)
    return render_template("result.html", result=input_from_form, computer=random_option)    
if __name__=="__main__":
    app.run(debug=True)