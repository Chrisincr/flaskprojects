from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)

app.secret_key = 'I solemly swear I am upto no good'


@app.route('/')

def index():
    if 'player_gold' not in session:
        session['player_gold'] = 0
    if 'action_log' not in session:
        session['action_log'] =[]
    player_gold = session['player_gold']
    print(session['action_log'])
    return render_template("index.html", player_gold = player_gold, action_log = session['action_log'])


@app.route('/process_gold', methods=['POST'])
def process_gold():
    print(request.form)
    action = {
        'Farm': random.randint(10,20),
        'Cave': random.randint(5,10),
        'House': random.randint(2,5),
        'Casino': random.randint(0,50)*random.choice([-1,1])
    }
    result = action[request.form['action']]
    session['player_gold'] += result
    current_date=datetime.datetime.now()
    current_date = current_date.strftime("%B %d %Y %I:%M:%S %p")
    if result < 0:
        log = "Lost " + str(result) + " gold at the " + request.form['action']+"! (" +current_date+ ")"
    else:
        log = "Earned " + str(result) + " gold at the " + request.form['action']+"! (" +current_date+ ")"
    session['action_log'].append(log)
    

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)