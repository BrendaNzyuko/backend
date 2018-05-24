
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  return "welcome student"
@app.route('/home')
def home():
  return "welcome home"

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0', port=8080)