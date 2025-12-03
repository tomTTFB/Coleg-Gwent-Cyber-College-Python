print("🧠 Code Dissection Challenge")

# ------------------------------------------------------------------------------------------------

''' 
Instructions
Use # to add comments to the code to identify and label the dissection code. For example firstName = "Chris" # Statement 
'''

print("🔍 Task 1: Procedural Programming")

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print(calculate_average([10, 20, 30]))


''' Instructions:

Identify and label the following:

Function definition
Loop
Statement
Return value
Function call '''

# ------------------------------------------------------------------------------------------------
print("🧠 Task 2: Object-Oriented Programming)

Class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

alice = Student('Alice', [10, 20, 30])
print(alice.average())

''' Instructions:

Identify and label the following:

Class definition
Constructor (__init__)
Attributes
Method
Object instantiation
Method call '''

# ------------------------------------------------------------------------------------------------

print("🧠 Task 3: Event-Driven Programming (Tkinter)")


import tkinter as tk

def on_click():
    print('Button clicked!')

root = tk.Tk()
button = tk.Button(root, text='Click Me', command=on_click)
button.pack()
root.mainloop()

''' Instructions:

Identify and label the following:

Event handler
Listener
Callback function
Main loop
GUI element '''
