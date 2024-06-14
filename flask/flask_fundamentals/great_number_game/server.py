from flask import Flask , render_template , request , redirect , session
app = Flask(__name__)
app.secret_key = 'random'
@app.route('/')
def random():
    import random 	
    session['random'] = random.randint(1,100)
    return redirect('/game')

@app.route('/game')
def game():
    if 'number' not in session:
        odd = 1
        return render_template("index.html" ,odd=odd, rand = session['random'])
    if 'counter' not in session:
        session['counter'] = 0
    session['counter']+=1
    if int(session['random']) < int(session['number'] and int(session['counter'] < 5)) :
        odd = 2
        return render_template("index.html" ,odd=odd, count= session['counter'] )
    elif int(session['random']) > int(session['number']) and int(session['counter'] < 5):
        odd = 3
        return render_template("index.html" , odd=odd, count= session['counter'])
    elif int(session['random']) == int(session['number']):
        odd = 4
        return render_template("index.html" , odd=odd , random = session['random'], count = session['counter'])
    else:
        odd = 5
        return render_template("index.html" , odd=odd , random = session['random'], count = session['counter'])

@app.route('/num', methods=['POST'])
def num():
    print(request.form)
    session['number'] = request.form['number']
    return redirect('/game')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
@app.route('/winners' , methods=['POST'])
def winners():
    print(request.form)
    name = request.form['users']
    return render_template("index2.html" , username = name , attempts = session['counter'] )

if __name__ == "__main__":
    app.run(debug=True)