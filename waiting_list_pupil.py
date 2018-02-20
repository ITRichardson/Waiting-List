import sqlite3
import time
from tkinter import *
import getpass

SGW_red = '#%02x%02x%02x' % (191,45,55)
text_colour = '#%02x%02x%02x' % (255,255,255)
user_name = getpass.getuser()

def submit():
    global user_name
    #user_name = e1.get()
    time_stamp = time.time()
    print(time_stamp)
    db = sqlite3.connect('waiting_list.db')
    c = db.cursor()
    c.execute('INSERT INTO tbl_waiting_list (waiting_name,waiting_time) VALUES (?,?)',(user_name,time_stamp))
    db.commit()
    db.close()
    
def delete():
    global user_name
    db = sqlite3.connect('waiting_list.db')
    c = db.cursor()
    c.execute('DELETE FROM tbl_waiting_list WHERE waiting_name=?',(user_name,))
    db.commit()
    db.close()


master = Tk()
master.configure(background = SGW_red)
master.geometry('{}x{}'.format(500, 250))
master.title("SGW Computing Dept - Help System v.1.0")
Label(master, text="SGW Computing - Help System",background = SGW_red,foreground = text_colour,font=("Calibri", 16, "bold")).place(x=105,y=20)
#Label(master, text="Enter Your Name",background = SGW_red,foreground = text_colour,font=("Calibri", 12, "bold")).place(x=180,y=70)
master.resizable(width=False, height=False)
#e1 = Entry(master)
#e1.insert(END, getpass.getuser())
#e1.place(x=180,y=100)
submit_button = Button(master, text="Help Me!", width=16, command=submit).place(x=180,y=130)
delete_button = Button(master, text="Help Not Needed!", width=16, command=delete).place(x=180,y=160)
mainloop()




