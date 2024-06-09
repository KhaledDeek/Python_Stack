from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World"
@app.route('/Dojo')
def dojo():
    return "Dojo"
@app.route('/say/<name>')
def name(name):
    print(name)
    return "Hi ," +name
@app.route('/repeat/<num>/<name>')
def repeat(name , num):
    print(name*int(num))
    return f'{name* int(num)}'
@app.errorhandler(404)
def rest_URL(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 