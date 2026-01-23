from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:9000"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    form_data = dict(request.form)

    try:
        response = requests.post(
            BACKEND_URL + '/submit',
            json=form_data,
            timeout=5
        )

        if response.status_code == 200:
            return redirect(url_for('success'))

        else:
            error = response.json().get("error", "Unknown error")
            return render_template("index.html", error=error)

    except requests.exceptions.RequestException as e:
        return render_template("index.html", error=str(e))


@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)