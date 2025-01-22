from multiprocessing.connection import address_type
from tkinter import*
root=Tk()
root.title("GUI APPLICATION")
root.geometry("800x500+200+80")
root.config(bg="#262626")
root.resizable(False,True)
def show_data():
    var_data.set(str(Text_field.get('1.0',END)))
    print(var_data.get())

var_data=StringVar()
Text_field=Text(root)
Text_field.place(x=50,y=200,width=400,height=150)

btn_get=Button(root,text="SHOW",font=("Time New Roman",15,"bold"),bg="gray",fg="white",activebackground="gray",activeforeground="white",cursor="hand2",command=show_data).place(x=100,y=100,width=150,height=70)

root.mainloop()