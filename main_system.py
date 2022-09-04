from distutils.log import debug
from flask import Flask, render_template
from collections.abc import Mapping

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(r"index.html")

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)
    
    