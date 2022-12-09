#This made by Vera Trinh

from tkinter import *
from tkinter import ttk
root = Tk()


width_entry = Entry(root)
length_entry = Entry(root)
radius_entry = Entry(root)
a_entry = Entry(root)
b_entry = Entry(root)
c_entry = Entry(root)
area = StringVar()
perimeter  =StringVar()
area_retangle = StringVar()
perimeter_retangle= StringVar()
area_circle = StringVar()
perimeter_circle = StringVar()
area_triangle = StringVar()
perimeter_triangle = StringVar()
l1 = Label(root, text="Width")
l2 = Label(root, text="Lenght")
l3 = Label(root, text="a")
l4 = Label(root, text="b")
l5 = Label(root, text="c")
l6 = Label(root, text="Radius")
b1 = Button(root, text="Calculate")

class Figure:
    def __init__():
        pass

class Retangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width =  width
     
    def area(self):
        return float(self.length)*float(self.width)
    def perimeter(self):
        return float(self.length)+float(self.width)
        
class Triangle(Figure):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return float(self.a)+float(self.b)+float(self.c)
    def area(self):
        s = (float(self.a)+float(self.b)+float(self.c))/2
        return s*(s- float(self.a))*(s-float(self.b))*(s-float(self.c)) ** 0.5 
class Circle(Figure):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*float(self.radius)*float(self.radius)
    def perimeter(self):
        return 2*3.14*float(self.radius)

def RetangleWindow():
    l3.grid_forget()
    l4.grid_forget()
    l5.grid_forget()
    l6.grid_forget()
    a_entry.grid_forget()
    b_entry.grid_forget()
    c_entry.grid_forget()
    radius_entry.grid_forget()
    l1.grid(column=1, row=3)
    width_entry.grid(column=2, row=3)
    l2.grid(column=1, row=4)
    length_entry.grid(column=2, row=4)
    b1.config(command=lambda:RetangleCal(length_entry.get(),width_entry.get()))
    b1.grid(column=2, row=5)
    
def RetangleCal(length,width):
    length = float(length)
    width = float(width)
    retangle1 = Retangle(length, width)
    area_retangle.set(retangle1.area())
    perimeter_retangle.set(retangle1.perimeter())
    l8 = Label(root, text="Area: ").grid(column=1, row=6)
    l9 = Label(root, text="Perimeter: ").grid(column=1, row=7)
    ttk.Label(root,background="white", width=15, textvariable=area_retangle).grid(column=2, row=6)
    ttk.Label(root,background="white", width=15, textvariable=perimeter_retangle).grid(column=2, row=7)

def CircleWindow():
    l1.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    l4.grid_forget()
    l5.grid_forget()
    width_entry.grid_forget()
    length_entry.grid_forget()
    a_entry.grid_forget()
    b_entry.grid_forget()
    c_entry.grid_forget()
    l6.grid(column=2, row=1)
    radius_entry.grid(column=2, row=2)
    b1.config(command=lambda:CircleCal(radius_entry.get()))
    b1.grid(column=2, row=5)
def CircleCal(radius):
    radius = float(radius)
    circle1 = Circle(radius)
    area_circle.set(circle1.area())
    perimeter_circle.set(circle1.perimeter())
    l8 = Label(root, text="Area: ").grid(column=1, row=6)
    l9 = Label(root, text="Perimeter: ").grid(column=1, row=7)
    ttk.Label(root,background="white", width=15, textvariable=area_circle).grid(column=2, row=6)
    ttk.Label(root,background="white", width=15, textvariable=perimeter_circle).grid(column=2, row=7)
def TriangleWindow():
    l1.grid_forget()
    l2.grid_forget()
    l6.grid_forget()
    width_entry.grid_forget()
    length_entry.grid_forget()
    radius_entry.grid_forget()
    l3.grid(column=1, row=1)
    a_entry.grid(column=2, row=1)    
    l4.grid(column=1, row=2)
    b_entry.grid(column=2, row=2)
    l5.grid(column=1, row=3)
    c_entry.grid(column=2, row=3)
    b1.config(command=lambda:TriangleCal(a_entry.get(), b_entry.get(), c_entry.get()))
    b1.grid(column=2, row=5)
    
def TriangleCal(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    triangle1 = Triangle(a,b,c)
    area_triangle.set(triangle1.area())
    perimeter_triangle.set(triangle1.perimeter())
    l8 = Label(root, text="Area: ").grid(column=1, row=6)
    l9 = Label(root, text="Perimeter: ").grid(column=1, row=7)
    ttk.Label(root,background="white", width=15, textvariable=area_triangle).grid(column=2, row=6)
    ttk.Label(root,background="white", width=15, textvariable=perimeter_triangle).grid(column=2, row=7)

b_Circle = Button(root, text = "Circle", command = lambda:CircleWindow()).grid(row = 0, column = 1)
b_Rectangle = Button(root, text = "Rectangle", command = lambda:RetangleWindow()).grid(row = 0, column = 2)
b_Triangle = Button(root, text = "Triangle", command = lambda:TriangleWindow()).grid(row = 0, column = 3)
root.mainloop()
#print("Welcome to the calculator")
#print("Enter 1 for Retangle, Enter 2 for Triangle, Enter 3 for Circle")
#shape = float(input("Please enter your choice: "))
#print(shape)

#if shape == 1:
    #length = float(input("Enter the length amount: "))
    #width = float(input("Enter the width amount: "))
    #retangle1 = Retangle(length, width)
    #retangle1.area_retangle()
    #retangle1.perimeter_retangle()
#if shape == 2:
    #a = float(input("Please Enter a = "))
    #b = float(input("Please Enter b = "))
    #c = float(input("Please Enter c = "))
    #t1 = Triangle(a,b,c)
    #t1.area_triangle()
    #t1.perimeter_triangle()
#if shape == 3:
    #radius = float(input("Please enter the radius of this circle: "))
    #cercle1 = Circle(radius)
    #cercle1.area_circle()
    #cercle1.perimeter_circle()

