from flask import Flask , render_template
app = Flask(__name__)
@app.route('/')                           
def hello_world():
    return "Hello World!!"
@app.route('/play')
def boxes():
    return render_template("index.html", box = "" ,times=0)
@app.route('/play/<num>')
def number_boxes(num):
    return render_template("index.html", box = "" , times =int(num)  )
@app.route('/play/<num>/<color>')
def number_boxes_with_color(num , color):
    return render_template("index.html", box = "" , times =int(num) , color = color )



if __name__=="__main__":
    app.run(debug=True) 