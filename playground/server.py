from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play')

def index():
    return render_template("index.html", num=3, color="#999999")

@app.route('/play/<num>')

def index_num(num):
    return render_template("index.html", num=int(num), color="blue")

@app.route('/play/<num>/<color>')

def index_num_color(num,color):
    return render_template("index.html", num=int(num), color=color)

@app.errorhandler(404)
def page_not_found(e):
    
    print(e)
    return 'Sorry! No response. Try again.'

if __name__ == "__main__":
    app.run(debug=True)