from flask import Flask, render_template, jsonify
from flask import request
import requests
import time
# from flask_migrate import Migrate
#from flask_sqlalchemy import SQLALchemy

#Start Flask App
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

# the associated function.
def home():
    # if request.method == 'POST':        
    return 'Maze Application'
    return render_template("index.html")
if __name__ == '__main__':
    #Debugging
    app.run(debug= True)






