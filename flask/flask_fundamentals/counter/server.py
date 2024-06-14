from flask import Flask , render_template , request , redirect , session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'  
@app.route('/')
def sum_count():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter']+=1
    return render_template("index.html" , sum=session['counter'])

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/plus2')
def add2():
    session['counter'] +=1
    return redirect('/')

@app.route('/delete')
def delete():
    session.clear() 
    return redirect('/')

@app.route("/increment" ,methods=['POST'])
def increase():
    print(request.form)
    session['number'] = request.form['number']
    session['counter'] += int(session['number'])
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)