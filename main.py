from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            .error {{color: red}}
        </style>
    </head>
    <body>
        <form action = "hello" method = "POST">
        <h1>Signup</h1>
        <br>
        <label for ="user_name">Username
            <input id = "user_name"  type = "text" name = "user_name" value = "{user}"/>
            <p class = "error">{user_error}</p>
        </label>    
        <br>
        <label for ="user_password">Password
            <input id = "user_password" type = "password" name = "user_password" value = "{password}"/>
            <p class = "error">{password_error}</p>    
        </label>    
        <br>
        <label for ="verify_password">Verfiy Password
            <input id ="verify_password" type = "password" name = "verify_password" value = "{verify_password}"/>
            <p class = "error">{verify_password_error}</p>
        </label>    
        <br>
        <input type = "submit" />
        </form>
    </body>
</html>

"""

@app.route("/")
def index ():
    return form

@app.route("/welcome", methods = ["POST"])
def welcome():
    user_name = request.form["user_name"]
    return '<h1> Welcome, ' + user_name + '</h1>'

@app.route('/display')
def display():
    return form.format(user = '', password = '', verify_password = '',
                        user_error = '', password_error = '', verify_password_error ='')

@app.route('/display', methods = ["POST"])
def display_welcome():
    user_name = request.form["user_name"]
    user_password = request.form["user_password"]
    verify_password = request.form["verify_password"]

    user_error = ''
    password_error = ''
    verify_password_error = ''

app.run()