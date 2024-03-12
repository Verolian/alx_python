"""Basic flask web server"""
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>', strict_slashes=False)
def profile(Username):
    return f"Welcome,{Username}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)