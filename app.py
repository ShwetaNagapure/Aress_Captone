from flask import Flask, render_template
from routes.contact_routes import contact_bp

app = Flask(__name__)

app.register_blueprint(contact_bp)

@app.route("/")
def home():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)