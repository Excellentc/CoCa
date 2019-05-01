from tkinter import *
from tkinter.messagebox import *
import pickle #сохранение,вывод,записывать данные
from tkinter import ttk


root = Tk()
root.geometry("600x350+200+300")
root.resizable(True, True)
root.title("CoCa")

fraem1= Frame(root,width=250, height=300, bg="orange", bd=10)
button_newproject = Button(fraem1, text="NEW PROJECT", command=lambda: save_w1(), width=20).grid(row=0, column=1)
button_oldprojects = Button(fraem1, text="PROJECTS", width=20).grid(row=1, column=1)
button_calculator = Button(fraem1, text="CALCULATOR VOLUMES", width=20).grid(row=2, column=1)
button_profile = Button(fraem1, text="USER PROFILE", command=lambda: user_profile(), width=20).grid(row=3, column=1)

fraem11= Frame(root, width=250, height=300, bg="blue")

fraem2= Frame(root, width=250, height=300, bg="green", bd=10)
text_login = Label(fraem2, text="CHANGE LOGIN").grid(row=0, column=1)
ent_text_login = Entry(fraem2).grid(row=1, column=1)
text_email = Label(fraem2, text="CHANGE E-MAIL").grid(row=2, column=1)
ent_text_email = Entry(fraem2).grid(row=3, column=1)
text_password = Label(fraem2, text="CHANGE PASSWORD").grid(row=4, column=1)
ent_text_password = Entry(fraem2).grid(row=5, column=1)
text_pass_confirm = Label(fraem2, text="CONFIRM PASSWORD").grid(row=6, column=1)
ent_text_pass_confirm = Entry(fraem2).grid(row=7, column=1)
text_metric = Label(fraem2, text=" INPUT DEBUG SYSTEM").grid(row=8, column=1)
ent_text_metric = Entry(fraem2).grid(row=9, column=1)
text_metric_ = Label(fraem2, text="м/см/мм").grid(row=10, column=1)
button_back_start = Button(fraem2, text="BACK", command=lambda: start_win(), width=20).grid(row=11, column=1)
button_save_start = Button(fraem2, text="SAVE", width=20).grid(row=12, column=1)

fraem22= Frame(root, width=250, height=300, bg="yellow", bd=30)

def start_win (): #Стартовое окно
    fraem1.grid(row=0,column=0, columnspan=5, rowspan=10)
    fraem11.grid(row=0,column=6, columnspan=5, rowspan=10)
    fraem2.grid_remove()
    fraem22.grid_remove()

def user_profile ():
    fraem1.grid_remove()
    fraem11.grid_remove()
    fraem2.grid(row=0,columnspan=4, rowspan=4)
    fraem22.grid(row=0,column=5,rowspan=4)

def rubashka_w1 ():

    text_qv1= Label(root, text="Длина стены")
    text_qv1w = Entry(root, width=5)
    text_qv2= Label(root, text="Высота стены")
    text_qv2w= Entry(root, width=5)
    text_qv3= Label(root, text="Расстояние слева до двери")
    text_qv3w = Entry(root,width=5)
    text_qv4= Label(root, text="Высота двери")
    text_qv4w = Entry(root,width=5)
    text_qv5= Label(root, text="Ширина двери")
    text_qv5w = Entry(root,width=5)
    text_qv6= Label(root, text="Высота над дверью до потолка")
    text_qv6w = Entry(root,width=5)
    button_save= Button(root, text="ОК", command= lambda: save_w1(), width=10)


    text_qv1.grid(row=1,column=1, columnspan=5, sticky='w')
    text_qv1w.grid(row=1,column=6)
    text_qv2.grid(row=2,column=1, columnspan=5, sticky= "w")
    text_qv2w.grid(row=2,column=6 )
    text_qv3.grid(row=3,column=1, columnspan=5, sticky="w")
    text_qv3w.grid(row=3,column=6 )
    text_qv4.grid(row=4,column=1, columnspan=5,sticky="w")
    text_qv4w.grid(row=4,column=6 )
    text_qv5.grid(row=5,column=1, columnspan=5,sticky="w")
    text_qv5w.grid(row=5,column=6 )
    text_qv6.grid(row=6,column=1, columnspan=5,sticky="w")
    text_qv6w.grid(row=6,column=6 )
    button_save.grid(row=7,column=5)


#    def save_w1():
   #      f = open("Date.txt", "wb")
 #       pickle.dump(wall_date, f)
#        f.close

start_win()
root.mainloop()