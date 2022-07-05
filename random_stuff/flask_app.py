from flask import Flask, render_template, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def about():
	return render_template('contact.html')

@app.route('/post')
def about():
	return render_template('post.html')

@app.route('/game')
def game():
	return render_template('game.html')

@app.route('/calc/<float:a>/<float:b>') # a simple calculator.
def calc(a, b):
	result = {
		"First number": a,
		"Second number": b,
		"sum of the two numbers": a+b,
		"product of the two numbers": a*b
		}
	return result

@app.route('/pow/<float:a>/<float:b>') # a power calculator.
def pow(a, b):
	result = {
		"Base": a,
		"Exponent or Power": b,
		"Value": a**b
		}
	return result

@app.route('/root/<float:n>') # square root calculator.
def root(n):
	result = {
		"Number": n,
		"root": math.sqrt(n)
	}
	return result

@app.route('/underroot/<float:a>/<float:b>') # a powerful root calculator.
def under_root(a,b):
	result = {
		"base": a,
		"power_in_underroot": b,
		"root_value": a**(1/b)
		}
	return result

@app.route('/prime/<int:n>') # check whether a number is prime or not.
def prime(n):
	b = 0
	if n > 1:
		for i in range(2, int(math.sqrt(n))+1):
			if (n % i) == 0:
				b = 1
				break
		if (b == 0):
			result = {
				"Value": n,
				"Prime": True
			}
		else:
			result = {
				"Value": n,
				"Prime": False
			}
	else:
		result = {
					"Value": n,
					"Prime": False
				}

	return result

@app.route('/sin/<float:n>') # sin calculator but bad.
def sin(n):
	a = n*22/(180*7)
	result = {
		"Angle": n,
		"Value(sin(n))": math.sin(a),
		"Value(cos(n))": math.cos(a),
		"Value(tan(n))": math.tan(a)
		}
	return result

@app.route('/armstrong/<int:n>') # program to check whether a number is an armstrong number or not.
def armstrong(n):
	#n = int(input("enter a number\n"))
	sum = 0
	order = len(str(n))
	copy_n = n
	while(n>0):
		digit = n%10
		sum += digit**order
		n = n//10

	if(sum == copy_n):
		print(f"{copy_n} is an armstrong number")
		result = {
			"Number": copy_n,
			"Armstrong": True
		}
	else:
		print(f"{copy_n} is not an armstrong number")
		result = {
			"Number": copy_n,
			"Armstrong": False
		}

	return jsonify(result)	

@app.route('/show/<string:n>') # just to show what you wrote
def show(n):
	result = {"What you wrote": n}
	return jsonify(result)

@app.route('/concat/<string:a>/<string:b>') # concatenate two pieces of strings.
def concat(a, b):
	return a+b


if __name__ == '__main__':
	app.run()