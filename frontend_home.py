from tkinter import *
import backend_home
def get_selected_row(event):
    global index
    index=list1.curselection()[0]
    """selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])"""

def view_command():
    list1.delete(0,END)
    for row in backend_home.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend_home.search(Client_Name_text.get(),Address_text.get(),Year_text.get(),Rent_text.get(), Deposit_text.get()):
        list1.insert(END,row)

def add_command():
    backend_home.insert(Client_Name_text.get(),Address_text.get(),Year_text.get(),Rent_text.get(), Deposit_text.get())
    list1.delete(0,END)
    list1.insert(END,(Client_Name_text.get(),Address_text.get(),Year_text.get(),Rent_text.get(), Deposit_text.get()))

def delete_command():
    backend_home.delete(index)

def update_command():
    backend_home.update(index,Client_Name_text.get(),Address_text.get(),Year_text.get(),Rent_text.get(), Deposit_text.get())

window=Tk()
window.configure()


window.geometry("850x450")
window.wm_title("Home Rental Management")

lspace=Label(window,text="")
lspace.grid(row=0,column=0)

l1=Label(window,text="Client Name",background="#00ffaa")
l1.grid(row=1,column=0)


Client_Name_text=StringVar()
e1=Entry(window,textvariable=Client_Name_text)
e1.grid(row=1,column=1)

l2=Label(window,text="Address",bg="#00ffaa")
l2.grid(row=1,column=3)


Address_text=StringVar()
e2=Entry(window,textvariable=Address_text)
e2.grid(row=1,column=4)


lspace1=Label(window,text="")
lspace1.grid(row=2,column=0)

l3=Label(window,text="Year",bg="#00ffaa")
l3.grid(row=3,column=0)

Year_text=StringVar()
e3=Entry(window,textvariable=Year_text)
e3.grid(row=3,column=1)

l4=Label(window,text="Rent",bg="#00ffaa")
l4.grid(row=3,column=3)

Rent_text=StringVar()
e4=Entry(window,textvariable=Rent_text)
e4.grid(row=3,column=4)


l5=Label(window,text="Deposit",bg="#00ffaa")
l5.grid(row=3,column=6)

Deposit_text=StringVar()
e5=Entry(window,textvariable=Deposit_text)
e5.grid(row=3,column=7) 


lspace2=Label(window,text="")
lspace2.grid(row=5,column=0)

lspace3=Label(window,text="")
lspace3.grid(row=5,column=4)




list1=Listbox(window, height=20,width=100,bg="#333333",fg="white")
list1.grid(row=8,column=0,rowspan=8,columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=8,column=6,rowspan=8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,bg="#00ffaa",command=view_command)
b1.grid(row=10,column=9)

b2=Button(window,text="Search entry", width=12,bg="#00ffaa",command=search_command)
b2.grid(row=11,column=9)

b3=Button(window,text="Add entry", width=12,bg="#00ffaa",command=add_command)
b3.grid(row=12,column=9)

b4=Button(window,text="Select & Update", width=12,bg="#00ffaa",command=update_command)
b4.grid(row=13,column=9)

b5=Button(window,text="Select & Delete", width=12,bg="#00ffaa",command=delete_command)
b5.grid(row=14,column=9)

b6=Button(window,text="Close", width=12,bg="#00ffaa",command=window.destroy)
b6.grid(row=15,column=9)

window.mainloop()
