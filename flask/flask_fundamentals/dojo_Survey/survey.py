from flask import Flask , render_template, request , redirect , session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'                       
@app.route('/')
def survey():
    return render_template("index.html")
@app.route("/result" ,methods=['POST'])
def survey_result():
    print(request.form)
    name_on_form = request.form['name']
    location_select = request.form['location']
    language_select = request.form['language']
    comment = request.form['textarea']
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['textarea'] = request.form['textarea']
    return redirect("/result")
@app.route("/result")
def main_form():
    return render_template("index2.html" , name_on_template=session['name'] ,selected_location=session['location'] ,selected_language=session['language'], commented=session['textarea'])
@app.route('/')
def main_page():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True) 