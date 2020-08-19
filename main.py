from flask import Flask, flash, redirect, render_template,request, url_for
from weather import query_api
from pprint import pprint as pp

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('weather.html',
							data=[
								{'name':'Chicago'}, 
								{'name':'Montreal'}, 
								{'name':'Calgary'},
								{'name':'Ottawa'}, 
								{'name':'Austin'}, 
								{'name':'Mississauga'},
								{'name':'Winnipeg'}, 
								{'name':'Vancouver'}, 
								{'name':'Brampton'},
								{'name':'Quebec'}
							])

@app.route("/result",methods=['GET','POST'])
def result():
	data =[]
	error = None
	select = request.form.get('comp_select')
	resp = query_api(select)
	pp(resp)
	if resp:
		data.append(resp)
	if len(data) != 2:
		error = 'Bad Response from weather API'
	print("I am other data *****----- ", data)
	return render_template('result.html',data=data,error=error)


if __name__=='__main__':
	print("Running with index")
	app.run(debug=True)