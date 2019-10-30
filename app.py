# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Hello World")
    return "Hello World!"

@app.route("/about")
def home():
    print("Krys - Phoenix")
    return "Krys - Phoenix"

@app.route("/contact")
def home():
    print("email me at...")
    return "email me at..."


if __name__ == "__main__":
    app.run(debug=True)
