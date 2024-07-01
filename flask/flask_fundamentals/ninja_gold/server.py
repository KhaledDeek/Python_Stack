from flask import Flask , render_template , request , redirect , session 
app = Flask(__name__)
import random
app.secret_key = 'gold'

@app.route('/')
def game():
    if'gold' not in session:
        session['gold'] = 0

    return render_template('index.html' ,  gold = session['gold'] , random = session['rand'] , building = session['building'] ) 


@app.route('/process_money' , methods=["POST"])
def find_gold():
    print(request.form)
    session['building'] = request.form['building']
    session['rangex'] = request.form['rangex']
    session['rangey'] = request.form['rangey']
    session['rand'] = random.randint(int(request.form['rangex']),int(request.form['rangey']))
    return redirect('/')



@app.route('/reset')
def reset():
    session['gold'] = 0
    session['rand'] = 0 
    return redirect('/')

if(__name__) == '__main__':
    app.run(debug=True)