
from flask import Flask
from triangle import Triangle
app = Flask (__name__)
@app.route("/")

@app.route("/triangle/<int:base>/<int:height>")
@app.rout("/triangle/<float:<base>/<float:<height>")
@app.route("/triangle/<int:<base>/<float:<float>")
@app.route("/triangle/<float:<base>/<int:<height>")
def triangle(base= 0,height=0):
  tri =Triangle(base,height)
  return"Area of triangle is {}".format(tri.area())

if __name__ =='__main__':
   app.run(host='0.0.0.0',port =8080)

