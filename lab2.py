#1
'''a = [6, 10, 15, 20, 25,34,86]
def new_list():
	b = [a[0], a[-1]]
	print(b)

new_list()'''

#2
'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def fun():
	b = a[0:5]
	print(b)
	return b
fun()'''

#3
'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in (a):
	if i in b:
		c.append(i)
print (c)'''

#4
import tkinter as tk
from tkinter import simpledialog
answer = simpledialog.askstring("Input", "Your message here!",
                                parent=tk.Tk())