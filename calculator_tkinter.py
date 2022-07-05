import tkinter

root = tkinter.Tk()
root.title("Calculator")

expression = ""

#functions

def add(value):
	global expression
	expression += value
	label_result.config(text=expression)

def clear():
	global expression
	expression = ""
	label_result.config(text=expression)

def calculate():
	global expression
	result = ""
	if expression != "":
		try:
			result = eval(expression)
		except:
			result = "error"
			expression = ""
	label_result.config(text=result)

#GUI

label_result = tkinter.Label(root, text = "")
label_result.grid(row=0, column=0, columnspan =4)

button1 = tkinter.Button(root, text= "1", width=4, command=lambda: add("1"))
button1.grid(row=1, column=0)

button2 = tkinter.Button(root, text= "2", width=4, command=lambda: add("2"))
button2.grid(row=1, column=1)

button3 = tkinter.Button(root, text= "3", width=4, command=lambda: add("3"))
button3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text = "/", width=4, command=lambda: add("/"))
button_divide.grid(row=1, column=3)

button4 = tkinter.Button(root, text= "4", width=4, command=lambda: add("4"))
button4.grid(row=2, column=0)

button5 = tkinter.Button(root, text= "5", width=4, command=lambda: add("5"))
button5.grid(row=2, column=1)

button6 = tkinter.Button(root, text= "6", width=4, command=lambda: add("6"))
button6.grid(row=2, column=2)

button_multiply = tkinter.Button(root, text = "*", width=4, command=lambda: add("*"))
button_multiply.grid(row=2, column=3)

button7 = tkinter.Button(root, text= "7", width=4, command=lambda: add("7"))
button7.grid(row=3, column=0)

button8 = tkinter.Button(root, text= "8", width=4, command=lambda: add("8"))
button8.grid(row=3, column=1)

button9 = tkinter.Button(root, text= "9", width=4, command=lambda: add("9"))
button9.grid(row=3, column=2)

button_subtract = tkinter.Button(root, text = "-", width=4, command=lambda: add("-"))
button_subtract.grid(row=3, column=3)

buttonC = tkinter.Button(root, text= "C", width=4, command=lambda: clear())
buttonC.grid(row=4, column=0)

button0 = tkinter.Button(root, text= "0", width=4, command=lambda: add("0"))
button0.grid(row=4, column=1)

buttonDot = tkinter.Button(root, text= ".", width=4, command=lambda: add("."))
buttonDot.grid(row=4, column=2)

button_addition = tkinter.Button(root, text = "+", width=4, command=lambda: add("+"))
button_addition.grid(row=4, column=3)

button_equals = tkinter.Button(root, text = "=", width =20, command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan =4)

root.mainloop()