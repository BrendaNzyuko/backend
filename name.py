
from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')
def index(name ="Student"):
  name = request.args.get('name',name)
  return "welcome {}".format(name)
@app.route('/home')
def home():
  return "welcome home"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)