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
    return render_template("index2.html" , name_on_template=name_on_form ,selected_location=location_select ,selected_language= language_select, commented=comment)
if __name__=="__main__":
    app.run(debug=True) 