import sqlite3
import time
from tkinter import *
from tkinter import ttk
import threading

SGW_red = '#%02x%02x%02x' % (191,45,55)
text_colour = '#%02x%02x%02x' % (255,255,255)


def clear_list():
    print("Clear List")


master = Tk()
master.configure(background=SGW_red)
master.geometry('{}x{}'.format(512, 768))
master.title("SGW Computing Dept - Help System v.1.0")
Label(master, text="SGW Computing - The Waiting List", background=SGW_red,foreground=text_colour, font=("Calibri", 16, "bold")).place(x=105, y=20)
master.resizable(width=False, height=False)

listbox = ttk.Treeview(master,selectmode="none",height = 25)
listbox["columns"] = ("user_name","time")
listbox.heading("#0",text = "ID")
listbox.column("#0",width=1, stretch=NO)
listbox.heading("user_name",text = "Name")
listbox.column("#1",width=200, stretch=NO)
listbox.heading("time",text = "Time")
listbox.column("time",width=150, stretch=NO)
listbox.place(x = 20, y = 60)

while True:
    db = sqlite3.connect('waiting_list.db')
    c = db.cursor()
    c.execute('SELECT waiting_name,waiting_time FROM tbl_waiting_list ORDER BY waiting_time ASC')
    table = c.fetchall()
    db.close()
    i = 0
    for row in table:
        user_name,time_stamp = row
        display_time = time.strftime(("%H:%M:%S"),time.gmtime(time_stamp))
        listbox.insert("",i,values = (user_name,display_time))
        i+=1
    listbox.update()
    Button(master, text="Clear The List", width=16, command=clear_list).place(x=190, y=740)
    time.sleep(0.01)
    for i in listbox.get_children():
        listbox.delete(i)









