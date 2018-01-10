from flask import Flask, request, redirect, render_template
import jinja2 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        # empty strings for errors

        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = "" 

        # username validation
        username_error = reqfield_charcount_errorcheck(username)

        # password validation
        password_error = reqfield_charcount_errorcheck(password)

        # password re-entry verification   
        verify_error = reqfield_charcount_errorcheck(verify)

        if email:
            email_error = valid_email(email)

        # match password to verify

        if password != verify:
            password_error = "Passwords don't match"
            verify_error = password_error

        if not (username_error or password_error or verify_error or email_error):
            return render_template('welcome.html',username=username)

        return render_template('signup_form.html', username_error = username_error, 
        errorpass = password_error, verr_orify = verify_error, err_mail = email_error, username = username)

    return render_template('signup_form.html')

def reqfield_charcount_errorcheck(field):
    error = ""
    if not field:
        error = "This field is required"
    if len(field) > 0 and len(field) < 3 or len(field) > 20:
        error = "Entry must be between 3 and 20 characters"
    return error 

def valid_email(user_input):
    error = ""
    if user_input.count('@') > 1 or user_input.count('.') > 1 or user_input.count(' ') > 0:
        error = "Email must contain no spaces, one @ symbol and one . symbol"
    return error

app.run()