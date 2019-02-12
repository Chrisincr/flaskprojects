from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] +=1
    else:
        session['counter'] = 1
    print(session['counter'])
    return render_template('index.html',counter=session['counter'])

@app.route('/plus_two')
def plus2_session():
    print('session plus 2')
    if 'counter' in session:
        session['counter'] +=1
    else:
        session['counter'] = 0
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    print('incrementing from form')
    print(request.form)
    if 'counter' in session:
        if 'number' in request.form:
            if request.form['number'].isdigit():
                number = int(request.form['number'])
            else:
                number = 1
            session['counter'] +=number-1
        else:
            session['counter'] += 1
    else:
        session['counter'] = 0
    return redirect('/')

@app.route('/destroy_session')
def clear_session():
    print('destroying session')
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)