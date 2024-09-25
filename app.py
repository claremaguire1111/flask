from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello!  I am a developer and I love flask!"

# Run the flask server
if __name__ == "__main__":
    app.run()