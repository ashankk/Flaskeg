from flask import Flask,render_template
app = Flask(__name__)

@app.route('/result')
def result():
    dict = {'maths':80,'c':90,'java':78}
    
    return render_template('h1.html',result=dict)
if __name__=="__main__":
    app.run(debug=True)
