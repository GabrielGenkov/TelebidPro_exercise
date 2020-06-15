from flask import Flask, redirect, url_for, request, render_template, session

from segments import Point

app = Flask(__name__)

app.secret_key = "wagabunga"

@app.route('/', methods=['GET', 'POST'])
def main():
	if(request.method == 'GET'):
		return render_template("index.html", meters=None,
		george=None,gergana=None,distance=None,
		answer=None, array=None)
	if(request.method == 'POST'):
		parameters = [
			int(request.form['input1']), 
			int(request.form['input2']), 
			int(request.form['input3']), 
			int(request.form['input4'])
		]
		array = []
		for i in range(parameters[0]):
			array.append(False)
			
		ans = Point(*parameters).points()[0]
		redpoints = Point(*parameters).points()[1]
		
		for element in redpoints:
			for i in range(element[0], element[1]):
				array[i] = True
		
		return render_template("index.html", meters=parameters[0],
		george=parameters[1],gergana=parameters[2],distance=parameters[3],
		answer=ans, array=array)
	
if __name__ == '__main__':
	app.run(debug=True)
	

