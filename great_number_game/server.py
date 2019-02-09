from flask import Flask, render_template, request, redirect, session
import random 

app = Flask(__name__)

app.secret_key = 'I solemly swear I am upto no good'


@app.route('/')

def index():
    if 'guesses' not in session:
        session['guesses'] = 0
    if 'secret' not in session:
        session["secret"] = random.randint(1,100)

    if 'Won' not in session:
        session["Won"] = 'False'
    
    if 'guess' in session:
        session['guesses'] += 1
        if int(session['guess']) > session['secret']:
            difference = 'High'
        else:
            difference = 'Low'
        return render_template("index.html", victory=session["Won"], guess=session['guess'],difference = difference, guesses = session['guesses'])

    return render_template("index.html")


@app.route('/results', methods=['POST'])
def show_submission():
    print(request.form)
    print(session['secret'])
    
    lastguess = request.form.get('guess','No Guess')
    session['guess'] = lastguess
    if str(lastguess) == str(session['secret']):
        session["Won"] = 'True'
        
        return redirect('/')

    return redirect('/')

@app.route('/reset')
def reset():
    print("reset requested")
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)