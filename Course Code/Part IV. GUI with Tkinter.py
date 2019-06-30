# Applications with Graphical User Interface
# A basic window with plain text
from tkinter import *

root = Tk()
label1 = Label(root, text="Hello World!")
label1.pack()
root.mainloop()

# Adding frames
root = Tk()
new_frame = Frame(root)
new_frame.pack()

second_frame = Frame(root)
second_frame.pack(side=BOTTOM)

button1 = Button(new_frame, text="Click here", fg="Red")
button2 = Button(second_frame, text="Click here", fg="Blue")

button1.pack()
button2.pack()

root.mainloop()

# Adding grids
root = Tk()

label1 = Label(root, text="First Name")
label2 = Label(root, text="Last Name")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()

# Self-adjusting widgets
root = Tk()

label1 = Label(root, text="First", bg="Red", fg="White")
label1.pack(fill=X)

label2 = Label(root, text="Second", bg="Blue", fg="White")
label2.pack(side=LEFT, fill=Y)

root.mainloop()

# Handling Button Clicks
root = Tk()

def sample_function():
    print("You clicked the button!")

button1 = Button(root, text="Click here", command=sample_function)
button1.pack()

root.mainloop()

# Using classes
class Mybuttons:

    def __init__(self, root_one):
        frame = Frame(root_one)
        frame.pack()

        self.print_button = Button(frame, text="Click Here", command=self.print_message)
        self.print_button.pack()

        self.quit_button = Button(frame, text="Exit", command=frame.quit)
        self.quit_button.pack(side=LEFT)

    def print_message(self):
        print("Button clicked!")


root = Tk()
b = Mybuttons(root)
root.mainloop()

# Drop down menus
def function_one():
    print("Menu item clicked!")

root = Tk()

my_menu = Menu(root)
root.config(menu=my_menu)
sub_menu = Menu(my_menu)

# Add items to the menu
my_menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="Project", command=function_one)
sub_menu.add_command(label="Save", command=function_one)

sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=function_one)

new_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=new_menu)
new_menu.add_command(label="Undo", command=function_one)

root.mainloop()

# Toolbar
def function_one():
    print("Menu item clicked!")

root = Tk()

my_menu = Menu(root)
root.config(menu=my_menu)
sub_menu = Menu(my_menu)

# Add items to the menu
my_menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="Project", command=function_one)
sub_menu.add_command(label="Save", command=function_one)

sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=function_one)

new_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=new_menu)
new_menu.add_command(label="Undo", command=function_one)

# Adding the toolbar
toolbar = Frame(root, bg="Pink")
insert_button = Button(toolbar, text="Insert Files", command=function_one)
insert_button.pack(side=LEFT, padx=2, pady=3)

print_button = Button(toolbar, text="Print", command=function_one)
print_button.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

root.mainloop()

# Status Bar
def function_one():
    print("Menu item clicked!")

root = Tk()

my_menu = Menu(root)
root.config(menu=my_menu)
sub_menu = Menu(my_menu)

# Add items to the menu
my_menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="Project", command=function_one)
sub_menu.add_command(label="Save", command=function_one)

sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=function_one)

new_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=new_menu)
new_menu.add_command(label="Undo", command=function_one)

toolbar = Frame(root, bg="Pink")
insert_button = Button(toolbar, text="Insert Files", command=function_one)
insert_button.pack(side=LEFT, padx=2, pady=3)

print_button = Button(toolbar, text="Print", command=function_one)
print_button.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

# Adding the status bar
status = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()

# Message box
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Title", "This is awesome")
response = tkinter.messagebox.askquestion("Question 1", "Do you like movies?")
if response == "yes":
    print("You should watch the Avengers!")

root.mainloop()

# Drawing
root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

new_line = canvas.create_line(0, 0, 50, 100)
other_line = canvas.create_line(10, 10, 100, 100, fill="Green")

root.mainloop()

# Building a Calculator with Tkinter
from tkinter import *
import parser

root = Tk()
root.title("Calculator")

# Adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

# Get the user input to the input field
i = 0
def get_variables(number):
    global i
    display.insert(i, number)
    i += 1


# The All Clear function
def clear_all():
    display.delete(0, END)


# Deleting a single element <-
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error!")


# The arithmetic operations
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


# Calculate the result
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")


# Adding the necessary buttons
Button(root, text="1", command=lambda: get_variables(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_variables(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_variables(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_variables(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_variables(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_variables(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_variables(9)).grid(row=4, column=2)

Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_variables(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3)

Button(root, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", command=lambda: get_operation("**")).grid(row=5, column=4)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5)

root.mainloop()