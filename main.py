from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index ():
    return render_template('form.html')

@app.route('/display')
def display_form():
    return render_template('form.html', user = '', user_error = '', password = '', password_error = '',
                        verify = '', verify_error ='', email = '', email_error = '')
                           

@app.route('/display', methods = ["POST"])
def display_welcome():
    user_name = request.form["user_name"]
    user_password = request.form["user_password"]
    verify = request.form["verify"]
    email = request.form["email"]

    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if user_name == '':
        user_error = 'please enter a name'
    else:
        user_name = user_name
        if len(user_name) < 3 or len(user_name) > 20:    
            user_error = 'name should be 3-20 characters'
        else:
            user_name = user_name
            if user_name:
                for x in user_name:
                    if x.isspace():
                        user_error = 'no space within the name'
                    else:
                        user_name = user_name    

    if user_password == '':
        password_error = 'please enter a password'
        user_password = ''
    else:
        user_password = user_password
        if len(user_password) < 3 or len(user_password) > 20:
            password_error = 'password needs to be 3-20 characters'
            user_password = ''
        else:
            user_password = user_password
            if user_password:
                for x in user_password:
                    if x.isspace():
                        password_error = 'no space within the password'
                        user_password = ''
                    else:
                        user_password = user_password    

    if verify == '':
        verify_error = 'please verify your password'
        verify = ''
    else:
        verify = verify        
        if verify != user_password:
            verify_error = 'passwords do not match'
            verify = ''
        else:
            verify = verify

    if email == '':
        email = email
    else:            
        if '@' not in email:
            email_error = "missing an '@' "
        elif '.' not in email:
            email_error = "missing an '.' "    
        else:
            email = email
            if len(email) < 3 or len(email) > 20:
                email_error = 'email address needs to be 3-20 characters long'
            else:
                email = email                    

    if not user_error and not password_error and not verify_error and not email_error:
        name = user_name
        return redirect('/welcome?name={0}'.format(name))
    else:
        return render_template('form.html', user_error=user_error, password_error=password_error, verify_error=verify_error, 
            email_error=email_error, email=email, user=user_name, password=user_password, verify=verify)

@app.route('/welcome')
def welcome():
    name = request.args.get('name') 
    return '<h1> Welcome, {0}! </h1>'.format(name)        
                    

app.run()