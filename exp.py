from flask import Flask,render_template,redirect,url_for


app=Flask(__name__)

@app.route('/')
def sample():
    return render_template('nav_bar.html')

@app.route("/labtest")
def lab():
    return render_template('labtest.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')
if __name__=='__main__':
    app.run(debug=True)