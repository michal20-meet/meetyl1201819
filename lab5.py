#1
# import tkinter as tk
# from tkinter import simpledialog

# greeting = simpledialog.askstring("Input","Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
# if greeting in ["Arrr!"]:
# 	print("Go away, pirate.")
# else:
# 	print("Greetings, hater of pirates!")


#2
# import tkinter as tk
# from tkinter import simpledialog

# year = simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw())

# if year <= "1900":
#     print ("Woah, that's the past!")
# if year > "1900" and year < "2020":
#     print ("That's totally the present!")
# if year >= "2020":
#     print ("Far out, that's the future!!")


#3
# class Person():
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name
#   def speak(self):
#   	print("My name is " +  self.first_name + ", " + self.last_name)

# me = Person("Brandon", "Walsh")
# you = Person("Ethan", "Reed")

# me.speak()
# you.speak()


#4
# import tkinter as tk
# from tkinter import simpledialog

# exam_1 = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

# exam_2 = int(simpledialog.askstring("Input", "exam grade two: ", parent=tk.Tk().withdraw()))

# exam_3 = int(simpledialog.askstring("Input", "exam grade three: ", parent=tk.Tk().withdraw()))

# grades = [exam_1, exam_2, exam_3]
# sum = 0
# i = 0
# for grade in grades:
#   sum = sum + grades[i]
#   i = i + 1

# avg = sum / len(grades)

# if avg >= 90:
#     letter_grade = "A"
# elif avg >= 80 and avg < 90:
#     letter_grade = "B"
# elif avg >= 70 and avg < 80:
#     letter_grade = "C"
# elif avg >= 65 and avg < 70:
#     letter_grade = "D"
# else:
#     letter_grade = "F"

# for grade in grades:
#     print("Exam: " + str(grade))

# print("Average: " + str(avg))
# print("Grade: " + letter_grade)

# if letter_grade == "F":
#     print("Student is failing.")
# else:
#     print ("Student is passing.")


#5
class Person():
   def __init__(self, name, fav_food, age):
       self.name = name
       self.fav_food = fav_food
       self.age = age

    def def_color(self, color):
    	

	def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)

    
    	

a = Person("Britney", "Pizza", 16)
a.print_info()

b = Person("Jake", "tuna", 15)
b.print_info()
