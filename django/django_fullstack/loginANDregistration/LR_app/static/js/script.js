fname = document.getElementById('fn').value;
lname = document.getElementById('ln').value;
pass = document.getElementById('pw').value;
email = document.getElementById('e').value
pattern = '^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'

function validate_fn(){
    if (fname == ""){
        document.getElementById('first_name_error').innerHTML = 'Field is Required'
    }
    else if (fname.length < 2){
        document.getElementById('first_name_error').innerHTML = 'First Name must be 2 characters at least'
    }
    else {
        document.getElementById('first_name_error').innerHTML = ''
    }
}

function validate_ln(){
    if (lname == ""){
        document.getElementById('last_name_error').innerHTML = 'Field is Required'
    }
    else if (lname.length < 2){
        document.getElementById('last_name_error').innerHTML = 'Last Name must be 2 characters at least'
    }
    else {
        document.getElementById('last_name_error').innerHTML = ''
    }
}

function validate_pw(){
    if (pass == ""){
        document.getElementById('password_error').innerHTML = 'Field is Required'
    }
    else if (pass.length < 8){
        document.getElementById('password_error').innerHTML = 'Password must be 8 characters at least !!'
    }
    else {
        document.getElementById('password_error').innerHTML = ''
    }
}

function validate_em(){
    if (email.pattern != pattern){
        document.getElementById('email_error').innerHTML = 'Please enter a valid Email Address !!!!!!!!'
    }
    else {
        document.getElementById('email_error').innerHTML = ''
    }
}

document.getElementById('register_btn').addEventListener('click' , function(event){
        if (fname == "" || fname.length < 2 || lname == "" || lname.length < 2 || pass == "" || pass.lnegth < 8 || email.pattern != pattern ){
            event.preventDefault()
        }
})

