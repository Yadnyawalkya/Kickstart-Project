from flask import Flask, redirect, url_for, request, render_template
import os

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
	fo = open("kickstart.cfg", "ab+")
	if request.method == 'POST':
		first_boot = request.form['first-boot']
		print first_boot
	return render_template('index.html')
	fo.close()

if __name__ == '__main__':
   app.run(debug = True)

