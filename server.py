from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "My_secret_session_key"

@app.route( "/" )
def reg_page():
    return render_template( "index.html" )

app.run( debug = True )
