from flask import Flask, render_template
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def posts():
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = res.json()[:10]
    return render_template('index.html', posts=data)

if __name__ == "__main__":
    app.run(debug=True)