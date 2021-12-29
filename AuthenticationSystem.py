#import tkinter module
from tkinter import *
from tkinter import messagebox


#Connecting Database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123@Dhee",
  database="SampleUserData"
)

#Adding Functionality 
def submitForm():
    Auth_result = -1
    userid = UserID.get()
    pass1 = Password.get()
    Auth_result = Authentication(userid, pass1)
    if Auth_result == 1:
      messagebox.showinfo("Login Successfull", "You are Logged in")
    else:
      messagebox.showerror("Login Failed", "Invalid UserID or Password")
    
    UserID.set("")
    Password.set("")


def Authentication(userid, pass1):
  mycursor = mydb.cursor()
  mycursor.execute("SELECT Email,Password FROM NewUserData")
  row = mycursor.fetchall()
  for i in row:
    if i[0] == userid and i[1] == pass1 :
      return 1
  return 0

def Register():

  #Function to create a new window for registration
  def registerForm():
    firstname = FirstName.get()
    lastname = LastName.get()
    email = Email.get()
    gender = Gender.get()
    createpassword = CreatePassword.get()
    confirmpassword = ConfirmPassword.get()
    checkboxvalue = CheckboxVal.get()
    
    if firstname == "":
      messagebox.showerror("Incomplete Data","Please Enter your First Name")
    elif lastname == "":
      messagebox.showerror("Incomplete Data","Please Enter your Last Name")
    elif email == "":
      messagebox.showerror("Incomplete Data","Please Enter your Email Address")
    elif gender == 0:
      messagebox.showerror("Incomplete Data","Please select your Gender")
    elif createpassword == "":
      messagebox.showerror("Incomplete Data","Please Create your Password")
    elif len(createpassword) > 10:
      messagebox.showerror("Incorrect Data", "Please Enter Password less than 10 Letter")
    elif confirmpassword == "":
      messagebox.showerror("Incomplete Data","Please Re-Enter your Password")
    elif createpassword != confirmpassword:
      messagebox.showerror("Incomplete Data","Please Enter Same Password")
    elif checkboxvalue == 0:
      messagebox.showerror("Incomplete Data","Please accept Terms and Conditions")
    else:
      genderData = ""
      if gender == 1:
        genderData = "Male"
      elif gender == 2:
        genderData = "Female"
      mycursor = mydb.cursor()
      query = "INSERT INTO NewUserData(FirstName, LastName, Email, Gender, Password) VALUES (%s, %s, %s, %s, %s )"
      val = (firstname,lastname,email,genderData,confirmpassword)
      mycursor.execute(query, val)
      mydb.commit()
      messagebox.showinfo("Successfully Registered","Please Login to Continue")
    
  RegisterWindow = Toplevel(root)
  RegisterWindow.title("Register Here")
  RegisterWindow.geometry("950x600")
  RegisterWindow.configure(background='#808080')
  RegisterTitle = Label(RegisterWindow, text="Please Fill your Details",bg="#A36846", font=fnt3).place(x=275,y=50)

  FirstName = StringVar()
  FirstNameLabel= Label(RegisterWindow, text= "First Name", font=fnt2, bg= "#1e847f").place(x=25, y=150)
  FirstNameEntry = Entry(RegisterWindow, textvariable = FirstName, font=fnt2,cursor="pencil").place(x=175, y=150)

  LastName = StringVar()
  LastNameLabel= Label(RegisterWindow, text= "Last Name", font=fnt2, bg= "#1e847f").place(x=450, y=150)
  LastNameEntry = Entry(RegisterWindow, textvariable = LastName, font=fnt2,cursor="pencil").place(x=660, y=150)

  Email = StringVar()
  EmailLabel= Label(RegisterWindow, text= "Email ID", font=fnt2, bg= "#1e847f").place(x=25, y=200)
  EmailEntry = Entry(RegisterWindow, textvariable = Email, font=fnt2,cursor="pencil").place(x=175, y=200)

  Gender = IntVar()
  GenderLabel= Label(RegisterWindow, text= "Gender", font=fnt2, bg= "#1e847f").place(x=450, y=200)
  MaleOption = Radiobutton(RegisterWindow, text = "Male",variable=Gender, value=1, font=fnt2).place(x=660, y=200)
  FemaleOption = Radiobutton(RegisterWindow, text = "female",variable=Gender, value=2, font=fnt2).place(x=800, y=200)
  
  CreatePassword = StringVar()
  CreatePasswordLabel= Label(RegisterWindow, text= "Password", font=fnt2, bg= "#1e847f").place(x=25, y=250)
  CreatePasswordEntry = Entry(RegisterWindow, textvariable = CreatePassword, font=fnt2,cursor="pencil").place(x=175, y=250)

  ConfirmPassword = StringVar()
  ConfirmPasswordLabel= Label(RegisterWindow, text= "Confirm Password", font=fnt2, bg= "#1e847f").place(x=450, y=250)
  ConfirmPasswordEntry = Entry(RegisterWindow, textvariable = ConfirmPassword, font=fnt2,cursor="pencil").place(x=660, y=250)
  
  CheckboxVal = IntVar()
  ChechboxOption = Checkbutton(RegisterWindow, text = "I accept all the terms and conditions.", variable= CheckboxVal, onvalue=1, offvalue=0, font=fnt2, bg= "#1e847f").place(x=25, y= 300)
  
  RegisterButton = Button(RegisterWindow, text="Register", font=fnt4, bg= "#ecc19c", command = registerForm).place(x=400, y= 450)

  

  

#Creating Root Window
root = Tk()
root.title("User Authentication")
root.geometry("800x700")
root.configure(background='#808080')

#Set maxsize and min size
root.maxsize(800,700)
root.minsize(800,700)

#Adding diffrent Font
fnt = ('arial', -45, 'bold')
fnt1 = ('Garamond', -25, 'bold')
fnt2 = ('Monaco', -20)
fnt3 = ('sans-serif', -36, 'bold' )
fnt4 = ('serif', -28, 'bold' )

#Creating Canvas for Title of the Billing System
title = Canvas(root, bg = "#ecc19c", height=100, width=800)
title.create_text(400,50, text='User Authentication', font=fnt, fill="black")

#Creating a Frame to display Login window
LoginWindow = Frame(root, bg='#1e847f', height=300, width=400)

#Adding data in Frame
LoginTitle = Label(LoginWindow, text="Enter your User ID and Password",bg="#A36846", font=fnt1).place(x=20,y=15)

UserID = StringVar()
UserIDLabel = Label(LoginWindow, text= "User ID", font=fnt2, bg= "#1e847f").place(x=15, y=100)
UserIDEntry = Entry(LoginWindow, textvariable = UserID, font=fnt2,cursor="pencil").place(x=130, y=100)

Password = StringVar()
PasswordLabel = Label(LoginWindow, text= "Password", font=fnt2, bg= "#1e847f").place(x=15, y=150)
PasswordEntry = Entry(LoginWindow, textvariable= Password, font=fnt2,cursor="pencil").place(x=130, y=150)

SubmitButton = Button(LoginWindow, text="Login", font=fnt4, bg= "#ecc19c", command = submitForm).place(x=150, y=225)
Ortext = Label(root, text= "New User ?", font=fnt1, bg= "#808080").place(x=200, y=520)
RegisterButton = Button(root, text= "Create Account", font=fnt1, bg= "#AF5107",fg="#FFFFFF", command = Register).place(x=412, y= 520)

#add Canvas to root
title.pack()

#add Frame to root
LoginWindow.place(x=200,y=200)

root.mainloop()
