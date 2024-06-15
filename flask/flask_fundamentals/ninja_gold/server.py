from flask import Flask , render_template , request , redirect , session 
app = Flask(__name__)
app.secret_key = 'gold'
@app.route('/')
def game():
    if 'count' not in session:
        session['count'] = -1
    if 'gold' not in session:
        session['gold'] = 0
    if 'rand' not in session:
        session['rand'] = 0
    if'building' not in session:
        session['building'] = 0
    if 'message' not in session:
        session['message'] = []
    x = '<br>'
    msg = x.join(session['message'])
    return render_template('index.html' , gold = session['gold'] , logs=int(session['rand']) , messages = msg )
@app.route('/process_money' , methods=["POST"])
def find_gold():
    print(request.form)
    import random
    msg1 = f"<ul><li>'Earned {session['rand']} golds from the {session['building']}'</li></ul>"
    msg2 = f"<ul><li>'Entered a casino and lost {session['rand']} golds .. Ouch ..'</li></ul>"
    if 'count' not in session:
        session['count'] = -1
    session['count'] +=1
    session['building'] = request.form['building']
    if request.form['building'] == 'farm':
        session['rand'] = random.randint(10,20)
        session['message'].insert(0,msg1)
        session['gold'] +=  int(session['rand'])
    elif request.form['building'] == 'cave':
        session['rand'] = random.randint(5,10)
        session['message'].insert(0,msg1)
        session['gold'] += int(session['rand'])
    elif request.form['building'] == 'house':
        session['rand'] = random.randint(2,5)
        session['gold']+= int(session['rand'])
        session['message'].insert(0,msg1)
    elif request.form['building'] == 'casino':
        session['rand'] = random.randint(-50,50)
        if session['rand'] > 0:
            session['gold'] += int(session['rand'])
            session['message'].insert(0,msg1)
        else:
            session['gold'] -= int(session['rand'])
            session['message'].insert(0,msg2)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if(__name__) == '__main__':
    app.run(debug=True)