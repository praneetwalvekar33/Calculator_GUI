from tkinter import *
from math import *

root = Tk()
root.title("Calculator")

e = Entry(root, width = 50 , borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

#Variable
count = 0 #To check if the number is a float value 
mom = 0   #for checking if operator is used after 1st calculation
flag=0    #To clear the display after the calculation
he=0      #To check how many times equalto is used in a calculation    

opera=0
f_num=0
#Functions
def click(n):
	global flag
	if flag==1:
		e.delete(0,END)
		flag=0
		global mom
		mom=0
	current = e.get()
	e.delete(0,END)
	a = str(current) + str(n)
	if n == ".":
		global count
		count = 1
	e.insert(0,a)

def clear_func():
	global mom
	mom = 0
	global flag
	flag=0
	global count
	count=0
	global he
	he=0
	e.delete(0 , END)

def add_func(n):
	global mom
	mom = mom + 1
	if mom > 1:
		global he
		he=1
		func()
	global first_number
	first_number = e.get()	
	if(first_number==""):
		e.insert(0,"Syntax Error")
		return
	global f_num
	if count == 1: 
		f_num = float(first_number)
	else:
		f_num = int(first_number)
	e.delete(0 , END)
	global opera
	opera = n
	global flag
	flag=0

def func():
	global flag
	global f_num
	global opera
	if he==0:
		mom=0
	second_number = e.get()
	global count
	for i in second_number:
		if(i=="."):
			count=1
	if(second_number=="" or second_number=="Syntax Error"):
		e.delete(0,END)
		e.insert(0, "Syntax Error")
		flag=1
		return
	if f_num==0:
		e.delete(0, END)
		e.insert(0, second_number)
		flag=1
		return
	e.delete(0,END)
	if count == 1:
		s_num = float(second_number)
	else:
		s_num = int(second_number)
	if opera==0:
		e.insert(0, "Syntax Error")
		return
	if opera == "+":
		result = f_num + s_num
	elif opera == "-":
		result = f_num - s_num
	elif opera == "*":
		result = f_num * s_num
	else:
		result = f_num / s_num
	e.insert(0, result)
	flag=1
	f_num=s_num

def power():
	global flag
	flag=1
	number = e.get()
	global count
	for i in number:
		if(i=="."):
			count=1
	if count == 1:
		num = float(number)
	else:
		num = int(number)
	result = num ** 2
	e.delete(0, END)
	e.insert(0, result)

def square():
	global flag
	flag=1
	number = e.get()
	global count
	for i in number:
		if(i=="."):
			count=1
	if count == 1:
		num = float(number)
	else:
		num = int(number)
	result = sqrt(num)
	e.delete(0, END)
	e.insert(0, result)

def reciporcal():
	global flag
	flag=1
	number = e.get()
	global count
	for i in number:
		if(i=="."):
			count=1
	if count == 1:
		num = float(number)
	else:
		num = int(number)
	result = 1 / num
	e.delete(0, END)
	e.insert(0, result)

#Define Buttons
button_1 = Button(root, text = "1", padx = 35, pady = 20, command = lambda:click(1))
button_2 = Button(root, text = "2", padx = 35, pady = 20, command = lambda:click(2))
button_3 = Button(root, text = "3", padx = 35, pady = 20, command = lambda:click(3))
button_4 = Button(root, text = "4", padx = 35, pady = 20, command = lambda:click(4))
button_5 = Button(root, text = "5", padx = 35, pady = 20, command = lambda:click(5))
button_6 = Button(root, text = "6", padx = 35, pady = 20, command = lambda:click(6))
button_7 = Button(root, text = "7", padx = 35, pady = 20, command = lambda:click(7))
button_8 = Button(root, text = "8", padx = 35, pady = 20, command = lambda:click(8))
button_9 = Button(root, text = "9", padx = 35, pady = 20, command = lambda:click(9))
button_0 = Button(root, text = "0", padx = 35, pady = 20, command = lambda:click(0))
button_01 = Button(root, text = ".", padx = 35, pady = 20, command = lambda:click("."))
button_02 = Button(root, text = "Clear", padx = 25, pady = 20, command = clear_func)
button_add = Button(root, text = "+", padx = 35, pady = 20, command = lambda:add_func("+"))
button_sub = Button(root, text = "-", padx = 35, pady = 20, command = lambda:add_func("-"))
button_multi = Button(root, text = "*", padx = 35, pady = 20, command = lambda:add_func("*"))
button_div = Button(root, text = "/", padx = 35, pady = 20, command = lambda:add_func("/"))
button_equ = Button(root, text = "=", padx = 35, pady = 20, command = func)
button_reci = Button(root, text = "1/x", padx = 25, pady = 20, command = reciporcal)
button_squ = Button(root, text = "x^2", padx = 25, pady = 20, command = power)
button_squrt = Button(root, text = "sqrt x", padx = 25, pady = 20, command = square)

#Display buttons
button_reci.grid(row = 1, column = 0)
button_squ.grid(row = 1, column = 1)
button_squrt.grid(row = 1, column = 2)
button_div.grid(row = 1, column = 3)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)
button_multi.grid(row = 2, column = 3)

button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)
button_sub.grid(row = 3, column = 3)

button_3.grid(row = 4, column = 2)
button_2.grid(row = 4, column = 1)
button_1.grid(row = 4, column = 0)
button_add.grid(row = 4, column = 3)

button_02.grid(row = 5, column = 0)
button_0.grid(row = 5, column = 1)
button_01.grid(row = 5, column = 2)
button_equ.grid(row = 5, column = 3)

root.mainloop()