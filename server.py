from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "My_secret_session_key"

@app.route( "/" )
def reg_page():
    return render_template( "index.html" )

@app.route( "/process", methods = ["POST"] )
def validation():
    error = False
    for i in request.form:
        if len(request.form[i]) < 1:
            error = True
            flash("Error: " + i + " cannot be left blank" )
    if error:
        return redirect( "/" )

    flash( "Thank you for your submission!" )
    return redirect( "/" )

app.run( debug = True )
