from tkinter import * #importing tkinter module
import numpy as np #importing numpy module
import math     #importing math module

def btnClick(numbers):  #this function is evoked when number buttons are clicked in the calculator
    global operator   #operator is globally defined
    operator=operator+str(numbers) #stores the numbers that are clicked in the form of a string
    text_Input.set(operator) #displays the numbers clicked, on the calculator screen

def btnClearDisplay():  #this function is evoked when'C'(clear screen) button is clicked to clear screen
    global operator  #operator is globally defined
    operator="" #contents of operator is removed and operator is reset to an empty string
    text_Input.set("") #clears the calculator string by setting it to an empty string ""

def btnEquals():    #this function is evoked when '='(equals to') button is clicked to obtain result
    global operator
    if operator.find('^')!=-1 and operator.find('e')==-1:  #checks if operator contains '^' but not 'e' 
        k=operator.find('^') #finds the index of '^'
        a=operator[0:k]     #extracts the substring from 0th to (k-1)th index and stores it in a
        b=operator[k+1:]    #extracts the substring from (k+1)th index to the end of the string and stores it in b
        c=math.pow(int(a),int(b)) #c stores the result of a raised to the power b by converting both a and b to int type
        text_Input.set(str(c)) #displays the result c by converting into a string on the calculator screen
        operator=""  #resets the operator into an empty string

    elif operator.find('e')!=-1: #checks if operator contains 'e'
        p=operator.find('^') #finds the index of '^'
        m=operator[p+1:]    #extracts the substring from (p+1)th index to the end of the string and stores it in m
        k=math.exp(int(m))  #find the exponential of m and stores it in k
        text_Input.set(str(k)) #displays k on the calculator screen
        operator=""#resets the operator into an empty string

    elif operator.find('/')!=-1: #MATH ERROR
        p=operator.find('/')
        k=operator[p+1:]
        if int(k)==0:
            text_Input.set("MATH ERROR")
        operator=""
        
    else:
        sumup=str(eval(operator)) #eval() evaluates the string if it contains '+','-','*','/' and returns the result in int type
        text_Input.set(sumup)   #displays the result 'sumup' as a string on the calculator screen
        operator="" #resets the operator into an empty string
        
def btnsin():   #this function is invoked when the 'sin' button is clicked to find the sine of an angle in degrees
    global operator
    s=np.sin(np.deg2rad(int(operator))) #sin() function of numpy package is used after converting the angle from degree to radian
    text_Input.set(s)   #displays the result on the calculator screen
    operator="" #resets the operator into an empty string

def btncos():  #this function is invoked when the 'cos' button is clicked to find the cos of an angle in degrees
    global operator
    s=np.cos(np.deg2rad(int(operator)))  #cos() function of numpy package is used after converting the angle from degree to radian
    text_Input.set(s)   #displays the result on the calculator screen
    operator="" #resets the operator into an empty string

def btntan():  #this function is invoked when the 'cos' button is clicked to find the cos of an angle in degrees
    global operator
    s=np.tan(np.deg2rad(int(operator))) #tan() function of numpy package is used after converting the angle from degree to radian
    text_Input.set(s)  #displays the result on the calculator screen
    operator=""  #resets the operator into an empty string

def btnln():  #this function is invoked when the 'ln' button is clicked to find the natural log of a number
    global operator
    s=np.log(int(operator)) #log() function of numpy package is used to find the log base e of a number
    text_Input.set(s)  #displays the result on the calculator screen
    operator=""  #resets the operator into an empty string

def btnsquare(): #this function is invoked when the 'x^2' button is clicked to find the square of a number
    global operator
    operator=operator+str('*')+str(operator) #we concatenate "*" + "operator" with the existing operator
    s=str(eval(operator))   #eval() evaluates the string and returns the result in integer type
    text_Input.set(s)  #displays the result on the calculator screen
    operator=""  #resets the operator into an empty string

def btnroot(): #this function is invoked when the '√' button is clicked to find the square root of a number
    global operator
    operator=np.sqrt(int(operator)) #sqrt() function of numpy package is used to find the square root
    text_Input.set(operator) #displays the result on the calculator screen
    operator="" #resets the operator into an empty string

def btnpower(): #this function is invoked when the '^' button is clicked to find power
    global operator
    operator=operator+"^" #"^" is concatenated with the existing operator string
    text_Input.set(operator) #displays the concatenated string on the calculator

def btnexp(): #this function is invoked when the 'e' button is clicked to find exponential
    global operator
    operator="e"+"^"  #string is concatenated
    text_Input.set(operator) #string is displayed on calculator screen
    
    
#Creating the GUI application main window
cal=Tk()
cal.title("Sreeja's Calculator")

operator=""
text_Input=StringVar()# creating a Tkinter variable by calling the StrinVar() constructor

#Entry widget is used to get input from the user where the font, foreground colour, border, background colour,
#alignment, number of columns, everythig is specified
txtDisplay=Entry(cal,font=('arial',27,'italic'),textvariable=text_Input,bd=10,
                 bg='black',fg='white', justify='right').grid(columnspan=5)


#Button widget is used to add buttons in the calculator
#'command' argument invokes the respective function when a button is pressed
#'grid' specifies the row and column number describing the position of a button
#'relief' is a 3D potrayal around the side of the widget that gives it a 3D look
#'bd' is the border width
#'fg' is the foreground colour
#'bg' is the background colour
#'text' specifies what is to be displayed on the Button widget
btn7=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="7",command=lambda:btnClick(7),relief='flat').grid(row=3,column=0)

btn8=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="8",command=lambda:btnClick(8),relief='flat').grid(row=3,column=1)

btn9=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="9",command=lambda:btnClick(9),relief='flat').grid(row=3,column=2)

Addition=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="+",command=lambda:btnClick("+"),relief='flat').grid(row=4,column=3)

btn4=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="4",command=lambda:btnClick(4),relief='flat').grid(row=4,column=0)

btn5=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="5",command=lambda:btnClick(5),relief='flat').grid(row=4,column=1)

btn6=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="6",command=lambda:btnClick(6),relief='flat').grid(row=4,column=2)

Subtraction=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="-",command=lambda:btnClick("-"),relief='flat').grid(row=5,column=3)

btn1=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="1",command=lambda:btnClick(1),relief='flat').grid(row=5,column=0)

btn2=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="2",command=lambda:btnClick(2),relief='flat').grid(row=5,column=1)

btn3=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="3",command=lambda:btnClick(3),relief='flat').grid(row=5,column=2)

Multiply=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="*",command=lambda:btnClick("*"),relief='flat').grid(row=6,column=3)

Zero=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="0",command=lambda:btnClick(0),relief='flat').grid(row=6,column=0)

Clear=Button(cal,padx=10,bd=2,fg='black',font=('arial',12,'bold'),
            text="C",command=lambda:btnClearDisplay(),relief='flat').grid(row=3,column=3)

Equal=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="=",command=lambda:btnEquals(),relief='flat').grid(row=6,column=1)

Division=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="/",command=lambda:btnClick("/"),relief='flat').grid(row=6,column=2)

Sine=Button(cal,padx=10,bd=2,fg='black',font=('arial',12,'bold'),
            text="sin",command=lambda:btnsin(),relief='flat').grid(row=1,column=0)

Cos=Button(cal,padx=10,bd=2,fg='black',font=('arial',12,'bold'),
            text="cos",command=lambda:btncos(),relief='flat').grid(row=1,column=1)

Tan=Button(cal,padx=10,bd=2,fg='black',font=('arial',12,'bold'),
            text="tan",command=lambda:btntan(),relief='flat').grid(row=1,column=2)

Ln=Button(cal,padx=10,bd=2,fg='black',font=('arial',12,'bold'),
            text="ln",command=lambda:btnln(),relief='flat').grid(row=1,column=3)

square=Button(cal,padx=10,bd=2,fg='black',font=('arial',12,'bold'),
            text="x^2",command=lambda:btnsquare(),relief='flat').grid(row=2,column=0)

root=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="√",command=lambda:btnroot(),relief='flat').grid(row=2,column=1)

power=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="^",command=lambda:btnpower(),relief='flat').grid(row=2,column=2)

exponential=Button(cal,padx=10,bd=2,fg='black',font=('arial',15,'bold'),
            text="e",command=lambda:btnexp(),relief='flat').grid(row=2,column=3)


#calls the mainloop to bring up the window and start the tkinter event loop
cal.mainloop()
