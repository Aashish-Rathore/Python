from tkinter import*
# from tkinter import messagebox

# root= Tk()
# root.geometry("300x200")

# #w=Label(root,text="Student-Study process",font="50")

# #w.pack()

# messagebox.showinfo("University","Tommorow is holiday")

# messagebox.showwarning("Class Teacher","Submit the assignments on time")


# messagebox.showerror("Student","I am not able to solve it")

# messagebox.askquestion("Parents", "Why do you have short attendance. Do you want to sit at home?")

# messagebox.askokcancel("Friends","will you join for coffee??")

# messagebox.askyesno("Results","Are you promoted for next class")

# messagebox.askretrycancel("Online Courses ", "Do you want to join assignments")


# root.mainloop()

# top = Tk()
# top.geometry("200x250")
# lbl= Label(top,text="A list of favourite countries...")
# listbox=Listbox(top)
# listbox.insert(1,"India")
# listbox.insert(2,"America")
# listbox.insert(3,"south korea ")
# listbox.insert(4,"new zealand")
# listbox.insert(5,"USA")

# lbl.pack()
# listbox.pack()
# top.mainloop()



#write a python programee to list of courses mca student has completed . the listbox should have vertical and horizontal scrollbar
# whatever the course  the user selects  it should be highlighted?




# win= Tk()
# win.title("Python GUI App")#Label
# Lbl=Label(win,text="Button Not Click")
# Lbl.pack()


# def click():action.configure(text="Clicked")
# Lbl.configure(foreground="red")
# Lbl.config(text='button Clicked')
# action= Button(win,text="Click Me",command = click)

# action.pack()
# win.mainloop()


# root = Tk()
# spnbox= Spinbox(root,from_ =0, to=20,values=(101,102,103,104,105))
# spnbox.pack()
# root.mainloop()

# top=Tk()
# menubar=Menu(top)
# menubar.add_command(label="Breakfast")
# menubar.add_command(label="Lunch")
# menubar.add_command(label="Dinner")
# top.config(menu=menubar)
# top.mainloop()

top=Tk()
top.title('Menu')
menubar=Menu(top)
breakfast=Menu(menubar,tearoff= 0)
breakfast.add_command(label="chapati")
breakfast.add_command(label="chole bhature")
breakfast.add_command(label="omelette")

menubar.add_cascade
(Label="breakfst",menu = breakfast)

lunch= Menu(menubar,tearoff=0)
lunch.add_command(label="paratha")


from tkinter import*
from tkinter import ttkaa
root= Tk()
tab=ttk.Treeview(root,column=("0","1","2","3"))

tab.column("#0")








main.loop()
