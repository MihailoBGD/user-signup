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

        # error messages
        required_error = "This field is required"
        password_re_enter = "Please re-enter password"
        charcount_error = "Entry must be between 3 and 20 characters"
        passmatch_error = "Password and password confirmation must match"
        invalid_email_error = "Email must contain no spaces, one @ symbol and one . symbol"


        # username validation
'''
        if not username:
            #username_error = required_error
        if len(username) > 0 and len(username) < 3 or len(username) > 20:
            #username_error = charcount_error

        # password validation

        if not password:
            #password_error = required_error
        if len(password) > 0 and len(password) < 3 or len(password) > 20:
            #password_error = charcount_error

        # password re-entry verification

        if not verify:
            verify_error = required_error
        if len(verify) > 0 and len(verify) < 3 or len(verify) > 20:
            verify_error = charcount_error    
'''

        if 
        # username validation
        username_error = reqfield_charcount_errorcheck(username)

        # password validation
        password_error = reqfield_charcount_errorcheck(password)

        # password re-entry verification   
        verify_error = reqfield_charcount_errorcheck(verify)

        # match password to verify

        if password != verify:
            password_error = passmatch_error 
            verify_error = passmatch_error
        
        if not (username_error or password_error or verify_error or email_error):
            return render_template('welcome.html',username=username)
        
        return render_template('signup_form.html', username_error = username_error, 
        errorpass = password_error, verr_orify = verify_error, err_mail = email_error)

    return render_template('signup_form.html')



def reqfield_charcount_errorcheck(field):
    error = ""
    if not field:
        error = "This field is required"
    if len(field) > 0 and len(field) < 3 or len(field) > 20:
        error = "Entry must be between 3 and 20 characters"
    return error 

  def valid_email(user_input):
    if user_input.count('@') > 1:
       
        error = "Email must contain no spaces, one @ symbol and one . symbol"
    if     
    return error


'''
def valid_email(user_input):
    for look_for in ['@', '.']:
        count = username_error.count(look_for)
        if count > 1:
            # error = "Email must contain no spaces, one @ symbol and one . symbol"
    return error
'''

'''
def count(actual_string, sub, start = 0, end = len(string)):
    count = 0
    for character in range(start, end, 1):
        if actual_string[character] == sub:
            count += 1

    return count
'''

app.run()