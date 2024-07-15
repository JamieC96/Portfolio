from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/biography")
def biography():
    return render_template("html/biography.html")

@app.route("/lavein")
def lavein():
    return render_template("html/lavein.html")

@app.route("/garsenda")
def garsenda():
    return render_template("html/garsenda.html")

@app.route("/convulsion")
def convulsion():
    return render_template("html/convulsion.html")

@app.route("/listen")
def listen():
    return render_template("html/listening-corner.html")

@app.route("/gallery")
def gallery():
    return render_template("html/gallery.html")

@app.route("/contact")
def contact():
    return render_template("html/contact.html")

if __name__ == "__main__":
    app.run()