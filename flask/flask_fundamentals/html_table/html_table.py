from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def table():
    print(request.form)
    all_users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template("index.html" ,users = all_users )



if __name__ =="__main__":
    app.run(debug=True)