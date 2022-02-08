from flask import Flask, render_template, make_response, request, redirect

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True # Remove it in prod
app.config["SECRET_KEY"] = "74d35de28ff1ca91a54d293f0e6da8a5"


# Error handler
@app.errorhandler(404)
def page_not_found(error):
    return redirect("/", 302)

# robots.txt
@app.route("/robots.txt", methods=["GET"])
def robots():
    with open(file="robots.txt", mode="r") as file:
        response = make_response(file.read(), 200)
        response.mimetype = "text/plain"
    return response

# Home page
@app.route("/", methods=["GET"])
def index():
    # Init
    return make_response(render_template("index.html"))


# Admin page
@app.route("/admin", methods=["GET", "POST"])
def admin():
    # Init
    response = ""

    if request.method == "GET":
        response = make_response(render_template("admin.html"))

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Verify crendentials
        if username == "part4" and password == "_C4n_B3_":
            response = make_response(render_template("admin.html", login="flag"))
        else:
            response = make_response(render_template("admin.html", login="failure"))

    return response