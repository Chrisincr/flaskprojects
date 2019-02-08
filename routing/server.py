from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')

def index():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/dojo')

def dojo():
    return 'Dojo!'

@app.route('/say/<name>')

def say_name(name):
    name=str(name)
    return f'Hello {name}'

@app.route('/repeat/<num>/<word>')

def repeat_word(num,word):
    num = int(num)
    word = str(word)
    val = word*num
    return val

@app.errorhandler(404)
def page_not_found(e):
    
    print(e)
    return 'Sorry! No response. Try again.'


if __name__ == "__main__":
    app.run(debug=True)

