from tkinter import *
import os
from PIL import ImageTk, Image

#main-screen
master = Tk()
master.title("banking app")

#functions
def finish_reg():
   name=temp_name.get()
   age= temp_age.get()
   gender= temp_gender.get()
   password= temp_password.get()

   all_accounts=os.listdir()
   if name=="" or age=="" or gender==" " or password=="":
      notif.config(fg='red',text="All fields required", font=('calibri',12))
      return
   for name_check in all_accounts:
      if name==name_check:
         notif.config(fg='red',text="Account already exist")
      else:
         new_file=open(name,"w")
         new_file.write(name+'\n')
         new_file.write(age + '\n')
         new_file.write(gender + '\n')
         new_file.write(password + '\n')
         new_file.write('0')
         new_file.close()
         notif.config(fg="green",text="Account successfully created")



def register():
   global temp_name
   global temp_age
   global temp_gender
   global temp_password
   global notif
   global balance
   global temp_balance
   temp_name=StringVar()
   temp_age = StringVar()
   temp_gender = StringVar()
   temp_password = StringVar()
    #registrationscreen
   register_screen= Toplevel(master)
   register_screen.title("Register")

    #labels
   Label(register_screen,text="please provide the below details to complete registration", font=('calibri', 14)).grid(row=0,sticky=N,pady=10)
   Label(register_screen,text='Name', font=('calibri', 12)).grid(row=1,sticky=W)
   Label(register_screen, text='Age', font=('calibri', 12)).grid(row=2, sticky=W)
   Label(register_screen, text='Gender', font=('calibri', 12)).grid(row=3, sticky=W)
   Label(register_screen, text='Password', font=('calibri', 12)).grid(row=4, sticky=W)
   notif=Label(register_screen, font=('calibri', 12))
   notif.grid(row=6, sticky=N)


#entries
   Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
   Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
   Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
   Entry(register_screen,textvariable=temp_password,show='*').grid(row=4,column=0)

#buttons
   Button(register_screen,text="Register",command=finish_reg,font=('calibri', 12)).grid(row=5,sticky=N,pady=10)
def login_session():
   global login_name
   all_accounts=os.listdir()
   login_name=temp_login_name.get()
   login_password=temp_login_password.get()
   for name in all_accounts:
      if name== login_name:
         file=open(name,"r")
         file_data= file.read()
         file_data=file_data.split("\n")
         password=file_data[3]
        #account dashboard
         if login_password == password:
           login_screen.destroy()
           account_dashboard = Toplevel(master)
           account_dashboard.title("Dashboard")
           #labels:
           Label(account_dashboard, text="Account Dashboard", font=('calibri', 12)).grid(row=0, sticky=N, pady=10)
           Label(account_dashboard,text="Welcome "+name,font=('calibri',12)).grid(row=1,sticky=N,pady=10)

           #buttons
           Button(account_dashboard,text='Personal Details',font=('calibri',12),command=personal_details,width=20).grid(row=2,sticky=N,pady=5)
           Button(account_dashboard, text='Deposit', font=('calibri', 12),width=30,command=deposit).grid(row=3, sticky=N, pady=5)
           Button(account_dashboard, text='Withdraw', font=('calibri', 12),width=30,command=withdraw).grid(row=4, sticky=N, pady=5)
           Label(account_dashboard).grid(row=5,sticky=N,pady=10)
         else:
           login_notif.config(fg="red",text="password incorrect")
           return
      login_notif.config(fg="red",text="No account found!")
def deposit():
   global amount
   global current_balance_label
   global deposit_notif
   amount= StringVar()
   file=open(login_name,'r')
   file_data=file.read()
   user_details=file_data.split('\n')
   details_balance=user_details[4]
   #deposit screen
   deposit_screen=Toplevel(master)
   deposit_screen.title("Deposit")
   Label(deposit_screen,text='deposit',font=('calibri',12)).grid(row=0,sticky=N,pady=10)
   current_balance_label=Label(deposit_screen,text='Current_balance: Rs.'+details_balance,font=('calibri',12))
   current_balance_label.grid(row=1,sticky=W,pady=5)
   Label(deposit_screen,text="Amount: ",font=('calibri',12)).grid(row=2,sticky=W,pady=5)
   deposit_notif=Label(deposit_screen,font=('calibri',12))
   deposit_notif.grid(row=4,sticky=W,pady=5)
   #entry
   Entry(deposit_screen,textvariable=amount).grid(row=2,column=1)
   #itbutton
   Button(deposit_screen,text='Finish',font=('calibri',12), command=finish_deposit).grid(row=3,sticky=W,pady=5)

def finish_deposit():
    if amount.get()=="":
      deposit_notif.config(text="Amount is required",fg="red")
      return
    if float(amount.get())<=0:
       deposit_notif.config(text="Negative currency is not accepted",fg='red')
       return
    file=open(login_name,"r+")
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[4]
    updated_balance=current_balance
    updated_balance=float(updated_balance)+float(amount.get())
    file_data=file_data.replace(current_balance,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text="current_balance: Rs."+str(updated_balance),fg='green')
    deposit_notif.config(text="Balance updated",fg='green')
def withdraw():
   global withdraw_amount
   global current_balance_label
   global withdraw_notif
   withdraw_amount= StringVar()
   file=open(login_name,'r')
   file_data=file.read()
   user_details=file_data.split('\n')
   details_balance=user_details[4]
   #withdraw screen
   withdraw_screen=Toplevel(master)
   withdraw_screen.title("Withdraw")
   Label(withdraw_screen,text='Withdraw',font=('calibri',12)).grid(row=0,sticky=N,pady=10)
   current_balance_label=Label(withdraw_screen,text='Current_balance: Rs.'+details_balance,font=('calibri',12))
   current_balance_label.grid(row=1,sticky=W,pady=5)
   Label(withdraw_screen,text="Amount: ",font=('calibri',12)).grid(row=2,sticky=W,pady=5)
   withdraw_notif=Label(withdraw_screen,font=('calibri',12))
   withdraw_notif.grid(row=4,sticky=W,pady=5)
   #entry
   Entry(withdraw_screen,textvariable=withdraw_amount).grid(row=2,column=1)
   #button
   Button(withdraw_screen,text='Finish',font=('calibri',12), command=finish_withdraw).grid(row=3,sticky=W,pady=5)


def finish_withdraw():
   if withdraw_amount.get() == "":
      withdraw_notif.config(text="Amount is required", fg="red")
      return
   if float(withdraw_amount.get()) <= 0:
      withdraw_notif.config(text="Negative currency is not accepted", fg='red')
      return
   file = open(login_name, "r+")
   file_data = file.read()
   details = file_data.split('\n')
   current_balance = details[4]
   if float(withdraw_amount.get())>float(current_balance):
      withdraw_notif.config(text="Insufficient balance",fg='red')
      return
   updated_balance = current_balance
   updated_balance = float(updated_balance) - float(withdraw_amount.get())
   file_data = file_data.replace(current_balance, str(updated_balance))
   file.seek(0)
   file.truncate(0)
   file.write(file_data)
   file.close()
   current_balance_label.config(text="current_balance: Rs." + str(updated_balance), fg='green')
   withdraw_notif.config(text="Balance updated", fg='green')
def personal_details():
   file=open(login_name,'r')
   file_data=file.read()
   user_data=file_data.split('\n')
   details_name=user_data[0]
   details_age=user_data[1]
   details_gender= user_data[2]
   details_balance=user_data[4]

   #personaldetails screen
   personaldetails_screen=Toplevel(master)
   personaldetails_screen.title("Personal Details")

   #labels
   Label(personaldetails_screen,text="Personal Details",font=('calibri',12)).grid(row=0,sticky=N,pady=5)
   Label(personaldetails_screen, text="Name: "+details_name, font=('calibri', 12)).grid(row=1, sticky=W, pady=5)
   Label(personaldetails_screen, text="Age: "+details_age, font=('calibri', 12)).grid(row=2, sticky=W, pady=5)
   Label(personaldetails_screen, text="Gender: "+details_gender, font=('calibri', 12)).grid(row=3, sticky=W, pady=5)
   Label(personaldetails_screen, text="Balance: "+details_balance, font=('calibri', 12)).grid(row=4, sticky=W, pady=5)





#login
def login():
   global temp_login_name
   global temp_login_password
   global login_notif
   global login_screen
   temp_login_name=StringVar()
   temp_login_password=StringVar()
   login_screen=Toplevel(master)
   login_screen.title('Login')
#labels
   Label(login_screen,text="Login to your account",font=('calibri',12)).grid(row=0,sticky=N,pady=5)
   Label(login_screen,text="Username",font=('calibri',12)).grid(row=1,sticky=W)
   Label(login_screen,text="password",font=('calibri',12)).grid(row=2,sticky=W)
   login_notif=Label(login_screen,font=('calibri',12))
   login_notif.grid(row=4,sticky=N)
#entries
   Entry(login_screen,textvariable=temp_login_name,).grid(row=1,column=1)
   Entry(login_screen,textvariable=temp_login_password,show="*").grid(row=2,column=1)
#Button
   Button(login_screen,text="Login",command=login_session,font=('calibri',12),width=20).grid(row=3, sticky=N, pady=10)

# image import
img = Image.open('C:\\Users\\krupa\\OneDrive\\Desktop\\banking gui app\\bank-image.jpg')
img = img.resize((250, 250))
img = ImageTk.PhotoImage(img)

#labels
Label(master, text='Customer banking app', font=('Calibri', 14)).grid(row=0,  sticky=N, pady=10)
Label(master, text='The most secure bank you have probably used', font=('Calibri', 12)).grid(row=1,  sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=5)

#buttons
Button(master, text='Register', font=('calibri', 10), width=20, command=register).grid(row=3, sticky=N)
Button(master, text='Login', font=('calibri', 10), width=20, command= login).grid(row=4, sticky=N, pady=10)
master.mainloop()
