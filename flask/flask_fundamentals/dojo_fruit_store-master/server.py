from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first = request.form['first_name']
    last = request.form['last_name']
    num = request.form['student_id']
    straw = request.form['strawberry']
    rasp = request.form['raspberry']
    app = request.form['apple']
    sum_all = int(straw) + int(rasp) + int(app)
    
    return render_template("checkout.html" , first_name = first , last_name=last , id=num ,strawberry=straw ,raspberry =rasp , apple = app ,sum = sum_all)
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    