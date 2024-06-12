from flask import Flask, render_template,request , redirect
app = Flask(__name__)
@app.route('/')
def default(x=4,y=4):
    return render_template("index.html" , x=x , y=y)

@app.route('/<num>')
def mult4(num):
    print(num)
    num = int(num)
    if num%2 ==0:
        y = int(num)/2
        odd=False
    else:
        y = int(num)/2
        odd=True
    return render_template("index.html" , odd = odd , y=int(int(num)/2))

@app.route('/<hor>/<ver>')
def mult(hor , ver):
    print(hor , ver)
    y = int(hor)
    if y%2 ==0:
        odd=False
    else:
        odd=True
    x = int(ver)
    if x%2 ==0:
        result = False
    else:   
        result = True
    return render_template("index.html" ,x=int(int(hor)/2) ,result = result ,odd = odd , y=int(int(hor)/2))


if __name__ =="__main__":
    app.run(debug=True)