from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')

def index():
    return render_template("index.html")


@app.route('/results', methods=['POST'])
def show_submission():
    
    subscribe = request.form.get('subscribe','No')
    if subscribe == 'checkedValue':
        subscribe = 'Yes'
    print(request.form)
    return render_template("submission.html",name=request.form["name"],email=request.form['email'],subscribe=subscribe)




if __name__ == "__main__":
    app.run(debug=True)
