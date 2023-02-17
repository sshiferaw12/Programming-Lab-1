from flask import Flask, render_template, redirect, url_for, request,session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("loginpage.html")


@app.route("/handle-login", methods=["POST"])
def handelLogin():
    
    username = request.form["username"]
    password = request.form["password"]

    if (username == "alex" and password == "alex"):
        return render_template("profilepage.html")

    else :
       return render_template("loginpage.html")
  

if __name__ == "__main__":
    app.run(debug=True, port = 7000)