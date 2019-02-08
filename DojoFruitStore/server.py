from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    current_date=datetime.datetime.now()
    day = int(datetime.datetime.now().strftime('%I'))
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    current_date = current_date.strftime("%B %d"+suffix+", %Y %I:%M:%S %p")

    print('Charging',request.form['first_name'],request.form['last_name'],'for',int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple']),'fruits')
    return render_template("checkout.html",strawberry=int(request.form['strawberry']), raspberry=int(request.form['raspberry']), apple=int(request.form['apple']), first_name=request.form['first_name'], last_name=request.form['last_name'], student_id=request.form['student_id'],current_date=current_date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    