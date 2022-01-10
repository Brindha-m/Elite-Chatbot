from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import os
from os.path import isfile, join
from threading import Thread
from userHandler import UserData
import  mysql.connector

conn = mysql.connector.connect(user='root', password='', host='localhost', database='Chatbot')
# #ee9ca7 → #ffdde1,#ffd89b
background, textColor = 'black', '#ffd89b'
background, textColor = textColor, background


avatarChoosen = 0
choosedAvtrImage = None
user_name = ''
user_gender = ''



###### ROOT1 ########
def startLogin():		
	try:
		
		user = UserData()
		user.extractData()
		#userName = user.getName().split()[0]
		os.system('python assistant.py')
        
	except Exception as e:
		print(e)

####### ROOT2 ########



def database():
    #getting form data
    user_name=nameField.get()
    user_gender=r.get()
   
    cursor = conn.cursor()
    insert_stmt = ("INSERT INTO information(user_name, user_gender) VALUES (%s,%s)")      
    data = (user_name, user_gender)
      
    try:
        cursor.execute(insert_stmt,data)
        conn.commit()
    except:
        conn.rollback()


def Add_details():

	global cap, user_name, user_gender
	user_name = nameField.get()
	user_gender = r.get()
	if user_name != '' and user_gender!=0:
		if agr.get()==1:
			raise_frame(root3)
		else:
			statusLbl['text'] = '(Check the Condition)'
	else:
		statusLbl['text'] = '(Please fill the details)'


def SuccessfullyRegistered():
	if avatarChoosen != 0:
		gen = 'Male'
		if user_gender==1: gen = 'Female'
		u = UserData()
		u.updateData(user_name, gen, avatarChoosen)
		usernameLbl['text'] = user_name
		raise_frame(root4)

def selectAVATAR(avt=0):
	global avatarChoosen, choosedAvtrImage
	avatarChoosen = avt
	i=1
	for avtr in (avtb1,avtb2,avtb3,avtb4,avtb5,avtb6,avtb7,avtb8):
		if i==avt:
			avtr['state'] = 'disabled'
			userPIC['image'] = avtr['image']
		else: avtr['state'] = 'normal'
		i+=1


################################################# GUI ###############################


def raise_frame(frame):
	frame.tkraise()

if __name__ == '__main__':

	root = Tk()
	root.title('Elite Chatbot 👩🏻‍🚀')
    
	w_width, w_height = 350, 590
	s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
	root.configure(bg="pink")
	# root.attributes('-toolwindow', True)
    


	root1 = Frame(root, bg=background)
	root2 = Frame(root, bg=background)
	root3 = Frame(root, bg=background)
	root4 = Frame(root, bg=background)

	for f in (root1, root2, root3, root4):
		f.grid(row=0, column=0, sticky='news')	
	
	################################
	########  MAIN SCREEN  #########
	################################

	image1 = Image.open('extrafiles/images/welcome.gif')
	image1 = image1.resize((300,180))
	defaultImg1 = ImageTk.PhotoImage(image1)

	dataFrame1 = Frame(root1, bd=10, bg=background)
	dataFrame1.pack(fill=X)
	logo = Label(dataFrame1,image=defaultImg1)
	logo.pack(padx=10, pady=10)

	#welcome label
	welcLbl = Label(root1, text='\nWelcome to the Elite Chatbot😊', font=('Aharoni', 12), fg='black', bg=background)
	welcLbl.pack(padx=10, pady=20)


	#status of Login

	loginStatus = Button(root1, text='   Register    ', font=('Aharoni', 12), bg='#018384', fg='white', relief=FLAT, command=lambda:raise_frame(root2))
	loginStatus.pack(pady=5)

	##################################
	########  LOGIN ADD SCREEN  #######
	##################################

	image2 = Image.open('extrafiles/images/seeyou.gif')
	#image2 = image2.resize((300, 250))
	defaultImg2 = ImageTk.PhotoImage(image2)

	dataFrame2 = Frame(root2, bd=10, bg=background)
	dataFrame2.pack(fill=X)
	lmain = Label(dataFrame2, width=300, height=250, image=defaultImg2)
	lmain.pack(padx=10, pady=10)

	#Details
	detailFrame2 = Frame(root2, bd=10, bg=background)
	detailFrame2.pack(fill=X)
	userFrame2 = Frame(detailFrame2, bd=10, width=300, height=250, relief=FLAT, bg=background)
	userFrame2.pack(padx=10, pady=10)

	#progress
	progress_bar = ttk.Progressbar(root2, orient=HORIZONTAL, length=303, mode='determinate')

	#name
	nameLbl = Label(userFrame2, text='Name', font=('Aharoni', 12), fg='#303E54', bg=background)
	nameLbl.place(x=10,y=10)
	nameField = Entry(userFrame2, bd=5, font=('Aharoni', 10), width=25, relief=FLAT, bg='#D4D5D7')
	nameField.focus()
	nameField.place(x=80,y=10)

	genLbl = Label(userFrame2, text='Gender', font=('Aharoni', 12), fg='#303E54', bg=background)
	genLbl.place(x=10,y=50)
	r = IntVar()
	s = ttk.Style()
	s.configure('Wild.TRadiobutton', background=background, foreground=textColor, font=('Aharoni', 10), focuscolor=s.configure(".")["background"])
	genMale = ttk.Radiobutton(userFrame2, text='Female', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
	genMale.place(x=80,y=52)
	genFemale = ttk.Radiobutton(userFrame2, text='Male', value=2, variable=r, style='Wild.TRadiobutton', takefocus=False)
	genFemale.place(x=150,y=52)

	#agreement
	agr = IntVar()
	sc = ttk.Style()
	sc.configure('Wild.TCheckbutton', background=background, foreground='#303E54', font=('Aharoni',10), focuscolor=sc.configure(".")["background"])
	agree = ttk.Checkbutton(userFrame2, text='I agree to continue the Elite login',command=database, style='Wild.TCheckbutton', takefocus=False, variable=agr)
	agree.place(x=28, y=100)
	#add login
	addBtn = Button(userFrame2, text='    Happy Login    ', font=('Aharoni', 12), bg='#01933B', fg='white', command=Add_details, relief=FLAT)
	addBtn.place(x=90, y=150)

	#status of login
	statusLbl = Label(userFrame2, text='', font=('Aharoni 10'), fg=textColor, bg=background)
	statusLbl.place(x=80, y=190)

	##########################
	#### AVATAR SELECTION ####
	##########################
	
	Label(root3, text="Choose Your Avatar", font=('Aharoni', 15), bg=background, fg='#303E54').pack()

	avatarContainer = Frame(root3, bg=background, width=300, height=500)
	avatarContainer.pack(pady=10)
	size = 100

	avtr1 = Image.open('extrafiles/images/avatars/a1.png')
	avtr1 = avtr1.resize((size, size))
	avtr1 = ImageTk.PhotoImage(avtr1)
	avtr2 = Image.open('extrafiles/images/avatars/a2.png')
	avtr2 = avtr2.resize((size, size))
	avtr2 = ImageTk.PhotoImage(avtr2)
	avtr3 = Image.open('extrafiles/images/avatars/a3.png')
	avtr3 = avtr3.resize((size, size))
	avtr3 = ImageTk.PhotoImage(avtr3)
	avtr4 = Image.open('extrafiles/images/avatars/a4.png')
	avtr4 = avtr4.resize((size, size))
	avtr4 = ImageTk.PhotoImage(avtr4)
	avtr5 = Image.open('extrafiles/images/avatars/a5.png')
	avtr5 = avtr5.resize((size, size))
	avtr5 = ImageTk.PhotoImage(avtr5)
	avtr6 = Image.open('extrafiles/images/avatars/a6.png')
	avtr6 = avtr6.resize((size, size))
	avtr6 = ImageTk.PhotoImage(avtr6)
	avtr7 = Image.open('extrafiles/images/avatars/a7.png')
	avtr7 = avtr7.resize((size, size))
	avtr7 = ImageTk.PhotoImage(avtr7)
	avtr8 = Image.open('extrafiles/images/avatars/a8.png')
	avtr8 = avtr8.resize((size, size))
	avtr8 = ImageTk.PhotoImage(avtr8)

	
	avtb1 = Button(avatarContainer, image=avtr1, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(1))
	avtb1.grid(row=0, column=0, ipadx=25, ipady=10)

	avtb2 = Button(avatarContainer, image=avtr2, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(2))
	avtb2.grid(row=0, column=1, ipadx=25, ipady=10)

	avtb3 = Button(avatarContainer, image=avtr3, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(3))
	avtb3.grid(row=1, column=0, ipadx=25, ipady=10)

	avtb4 = Button(avatarContainer, image=avtr4, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(4))
	avtb4.grid(row=1, column=1, ipadx=25, ipady=10)

	avtb5 = Button(avatarContainer, image=avtr5, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(5))
	avtb5.grid(row=2, column=0, ipadx=25, ipady=10)

	avtb6 = Button(avatarContainer, image=avtr6, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(6))
	avtb6.grid(row=2, column=1, ipadx=25, ipady=10)

	avtb7 = Button(avatarContainer, image=avtr7, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(7))
	avtb7.grid(row=3, column=0, ipadx=25, ipady=10)

	avtb8 = Button(avatarContainer, image=avtr8, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(8))
	avtb8.grid(row=3, column=1, ipadx=25, ipady=10)


	Button(root3, text='Submit', font=('Aharoni', 15), bg='#01933B', fg='white', bd=0, relief=FLAT, command=SuccessfullyRegistered).pack()

	#########################################
	######## SUCCESSFULL REGISTRATION #######
	#########################################

	userPIC = Label(root4, bg=background, image=avtr2)
	userPIC.pack(pady=(40, 10))
	usernameLbl = Label(root4, text="Brindha", font=('Aharoni',15), bg=background, fg='#85AD4F')
	usernameLbl.pack(pady=(0, 70))

	Label(root4, text="Your account has been successfully activated!", font=('Aharoni',13), bg=background, fg='#303E54', wraplength=300).pack(pady=10)

	Button(root4, text='OK', bg='#0475BB', fg='white',font=('Aharoni', 18), bd=0, relief=FLAT, command=lambda:startLogin()).pack(pady=50)
	#Button(root4, text='exit', bg='#0475BB', fg='white',font=('Aharoni', 18), bd=0, relief=FLAT, command=lambda:quit()).pack(pady=50)


	root.iconbitmap('extrafiles/images/chatapp_ca.ico')
	raise_frame(root1)
	root.mainloop()
	os.close
