from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "abc"
    list1 = [10,20,30]
    return render_template('h1.html',name = name)
@app.route("list1/")
def index():
    list1 = [10,20,30]
    return render_template('h1.html',list1 = list1)
@app.route("tuple1/")
def index():
    tuple1 = (1,2,3)
    return render_template('h1.html',tuple1 = tuple1)


if __name__=="__main__":
    app.run(debug=True)

