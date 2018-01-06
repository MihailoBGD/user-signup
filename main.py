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

        username_error = ""
        password_error = ""
        verify_error = ""
        email_error = "" 


        required_error = "This field is required"
        password_re_enter = "Please re-enter password"
        charcount_error = "Entry must be between 3 and 20 characters"
        passmatch_error = "Password and password confirmation must match"
        invarlied_email_error = "Email must contain no spaces, one @ symbol and one . symbol"

        # username validation

        if not username:
            username_error = required_error
        if len(username) > 0 and len(username) < 3 or len(username) > 20:
            username_error = charcount_error

        # password validation

        if not password:
            password_error = required_error
        if len(password) > 0 and len(password) < 3 or len(password) > 20:
            password_error = charcount_error

        # password re-entry verification

        if not verify:
            verify_error = required_error
        if len(verify) > 0 and len(verify) < 3 or len(verify) > 20:
            verify_error = charcount_error    

        # match password to verify

        if password != verify:
            password_error = passmatch_error 
            verify_error = passmatch_error
        
        if not (username_error or password_error or verify_error or email_error):
            return render_template('welcome.html',username=username)
        
        return render_template('signup_form.html', 
    username_error = username_error, 
    errorpass = password_error, verr_orify = verify_error, err_mail = email_error)        
    return render_template('signup_form.html')



'''def no_fields_empty(fields_input):
    is_empty = False
    for input in fields_input:
        if len(input) == 0:
            is_empty = True
    return is_empty'''

            

# def valid_password(user_input):

# def passwords_match (user_input):

# def valied_email(user_input):



app.run()