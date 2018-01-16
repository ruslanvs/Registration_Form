from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "My_secret_session_key"

@app.route( "/" )
def reg_page():
    return render_template( "index.html" )

@app.route( "/process", methods = ["POST"] )
def validation():
    error = False
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    print request.form["first_name"]
    if not str.isalpha( str( request.form["first_name"] ) ) or not str.isalpha( str( request.form["last_name"] ) ):
        error = True
        flash( "Error: name cannot contain characters other than letters" )
    
    if len( str(request.form["password"])) < 9:
        error = True
        flash( "Password should be at least 9 characters long" )
    
    elif request.form["password"] != request.form["password_confirmation"]:
        error = True
        flash( "Password and Password Confirmation do not match" )

    if not email_regex.match( request.form["email"] ):
        error = True
        flash( "Please provide a valid email" )

    for i in request.form:
        if len(request.form[i]) < 1:
            error = True
            flash( "Error: " + i + " cannot be left blank" )

    if error:
        return redirect( "/" )

    flash( "<p class='green'>Thank you for your submission!</p>" )
    return redirect( "/" )

app.run( debug = True )