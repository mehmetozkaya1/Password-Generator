from tkinter import *
from tkinter import messagebox
import random

master = Tk() # Creating Tk object

master.title("Random Password Generator") # Setting the window title

img = PhotoImage(file='pass-icon.png') # Creating a img variable
master.iconphoto(False,img) # Setting the window icon

canvas = Canvas(master,height=450,width=750) # Creating the canvas
canvas.pack() # Sending the canvas to master

top_frame = Frame(master, bg="light blue") # Creating the top frame
top_frame.place(relx = 0.026, rely=0.05,relwidth=0.95,relheight=0.7) # Place

bottom_frame = Frame(master, bg="light blue") # Creating the bottom frame
bottom_frame.place(relx = 0.026, rely=0.77,relwidth=0.95,relheight=0.17) # Place

# Main Title Label
main_title_label = Label(top_frame,bg="light blue",text="Random Password Generator",font=("Verdana",15,"bold")) # Creating the label
main_title_label.pack(padx=10,pady=10,side="top")

# Checkbutton choises

def check_state1():
    if var1.get() == 0:
        letters_count.configure(state="disabled")
    else:
        letters_count.configure(state="normal")

def check_stat2():
    if var2.get() == 0:
        numbers_count.configure(state="disabled")
    else:
        numbers_count.configure(state="normal")

def check_state3():
    if var3.get() == 0:
        specials_count.configure(state="disabled")
    else:
        specials_count.configure(state="normal")

var1 = IntVar(master)
cb_letters = Checkbutton(top_frame,variable=var1,onvalue=1,offvalue=0,bg="light blue",font=("Verdana",10,"bold"),text="Include letters [(a-z)/(A-Z)]",command=check_state1)
cb_letters.place(x=50,y=100)


var2 = IntVar(master)
cb_numbers = Checkbutton(top_frame,variable=var2,onvalue=1,offvalue=0,bg="light blue",font=("Verdana",10,"bold"),text="Include numbers (0-9)",command=check_stat2)
cb_numbers.place(x=50,y=150)

var3 = IntVar(master)
cb_specials = Checkbutton(top_frame,variable=var3,onvalue=1,offvalue=0,bg="light blue",font=("Verdana",10,"bold"),text="Include special characters ($-&)",command=check_state3)
cb_specials.place(x=50,y=200)

# Label

long_label = Label(top_frame,bg="light blue",font=("Verdana",10,"bold"),text="How many characters of:")
long_label.place(x=450,y=50)

# Entry_areas

cvar1 = StringVar(value="0")
letters_count = Entry(top_frame,state="disabled",textvariable=cvar1,width=31)
letters_count.place(x=450,y=100)

cvar2 = StringVar(value="0")
numbers_count = Entry(top_frame,state="disabled",textvariable=cvar2,width=31)
numbers_count.place(x=450,y=150)

cvar3 = StringVar(value="0")
specials_count = Entry(top_frame,state="disabled",textvariable=cvar3,width=31)
specials_count.place(x=450,y=200)

# Arrays

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
specials = ['#','$','%','&','?','!']
empty_array = []

# Button

def generate_password():

    
    counter1 = int(letters_count.get())
    counter2 = int(numbers_count.get())
    counter3 = int(specials_count.get())
    

    if var1.get() == 1 and (var2.get()==0 and var3.get()==0):

        for i in range(counter1):
            empty_array.append(letters[random.randint(0,len(letters)-1)])
    
    elif var1.get() == 0 and var2.get() == 1 and var3.get()==0:
        
        for i in range(counter2):
            empty_array.append(numbers[random.randint(0,len(numbers)-1)])
    
    elif var1.get() == 0 and var2.get() == 0 and var3.get()==1:

        for i in range(counter3):
            empty_array.append(specials[random.randint(0,len(specials)-1)])

    elif var1.get() == 1 and var2.get() == 1 and var3.get()==0:

        for i in range(counter1):
            empty_array.append(letters[random.randint(0,len(letters)-1)])
        
        for i in range(counter2):
            empty_array.append(numbers[random.randint(0,len(numbers)-1)])

    elif var1.get() == 0 and var2.get() == 1 and var3.get()==1:
        
        for i in range(counter2):
            empty_array.append(numbers[random.randint(0,len(numbers)-1)])

        for i in range(counter3):
            empty_array.append(specials[random.randint(0,len(specials)-1)])

    elif var1.get() == 1 and var2.get() == 0 and var3.get()==1:

        for i in range(counter1):
            empty_array.append(letters[random.randint(0,len(letters)-1)])
        
        for i in range(counter3):
            empty_array.append(specials[random.randint(0,len(specials)-1)])
    
    elif var1.get() == 0 and var2.get() == 0 and var3.get()==0:
        
        message = "Please choose at least one option!"
        messagebox.showerror("Failed!",message)

    elif var1.get() == 1 and var2.get() == 1 and var3.get()==1:
        
        for i in range(counter1):
            empty_array.append(letters[random.randint(0,len(letters)-1)])
        
        for i in range(counter2):
            empty_array.append(numbers[random.randint(0,len(numbers)-1)])
        
        for i in range(counter3):
            empty_array.append(specials[random.randint(0,len(specials)-1)])
    
    random.shuffle(empty_array)

    password = "".join(empty_array)

    password_field.delete(0,END)
    password_field.insert(0,password)

    empty_array.clear()
    
generate_button = Button(top_frame,text="GENERATE",font=("Verdana",10,"bold"),width=20,height=2,command=generate_password)
generate_button.place(x=250,y=250)

# Password Area

password_label = Label(bottom_frame,text="Random Password =",font=("Verdana",10,"bold"),bg="light blue")
password_label.place(x=20,y=20)

password_field = Entry(bottom_frame,width=50)
password_field.place(x=200,y=20)

master.mainloop()