from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')

def index():
    return render_template("index.html",rows=8,columns=8,pColor="blue",sColor="darkred")

@app.route('/<rows>')

def index_rows(rows):
    return render_template("index.html",rows=int(rows),columns=8,pColor='blue',sColor='darkred')

@app.route('/<rows>/<columns>')

def index_rows_columns(rows,columns):
    return render_template("index.html",rows=int(rows),columns=int(columns),pColor="blue",sColor="darkred")

@app.route('/<rows>/<columns>/<pColor>/<sColor>')

def index_rows_columns_colors(rows,columns,pColor,sColor):
    return render_template("index.html",rows=int(rows),columns=int(columns),pColor=pColor,sColor=sColor)


@app.errorhandler(404)
def page_not_found(e):
    
    print(e)
    return 'Sorry! No response. Try again.'

if __name__ == "__main__":
    app.run(debug=True)