import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter as tk

def create_or_connect_db(dbname):
    conn = sqlite3.connect(dbname)
    return conn


conn = create_or_connect_db('mydatabase.db')


def insert_data_table(c,name, salary, department, position, hireDate):
    c.cursor().execute("""INSERT INTO employees(name, salary, department, position, hireDate) VALUES(
                                '{}','{}','{}','{}','{}');
    """.format(name, salary, department, position, hireDate))
    c.commit()



def select_all_data(c):
    rec = c.cursor().execute("""SELECT * from employees""")
    records = rec.fetchall()
    for i in range(0,len(records)):
        lbl_tab6 = Label(tab2, text=records[i][0])
        lbl_tab6.grid(column=0, row=i+1, sticky=W)
        lbl_tab7 = Label(tab2, text=records[i][1])
        lbl_tab7.grid(column=1, row=i+1, sticky=W)
        lbl_tab8 = Label(tab2, text=records[i][2])
        lbl_tab8.grid(column=2, row=i+1, sticky=W)
        lbl_tab9 = Label(tab2, text=records[i][3])
        lbl_tab9.grid(column=3, row=i+1, sticky=W)
        lbl_tab10 = Label(tab2, text=records[i][4])
        lbl_tab10.grid(column=4, row=i+1, sticky=W)
def show_all():
    select_all_data(conn)



window = Tk()
window.title("tkinter GUI")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)
btn10 = Button(tab2, text="Обновить", command=show_all)
btn10.grid(column=5, row=0)

def show_but():
    name = text.get(1.0, END)
    salary = text2.get(1.0, END)
    department = text3.get(1.0, END)
    position = text4.get(1.0, END)
    hireDate = text5.get(1.0, END)
    insert_data_table(conn,name, salary, department, position, hireDate)
    success_lable.grid(column=0, row=13)
    success_lable.after(2000, success_lable.grid_remove)


tab_control.add(tab1, text='Добавить работника')
tab_control.add(tab2, text='Посмотреть всех сотрудников')

lbl = Label(tab1, text="Привет, попробуй изменить данные")
lbl.grid(column=0, row=0, sticky=W)

lbl1 = Label(tab1, text="Имя", width="20")
lbl1.grid(column=0, row=1)
lbl2 = Label(tab1, text="Заработная плата", width="20")
lbl2.grid(column=0, row=3)
lbl3 = Label(tab1, text="Департамент", width="20")
lbl3.grid(column=0, row=5)
lbl4 = Label(tab1, text="Позиция", width="20")
lbl4.grid(column=0, row=7)
lbl5 = Label(tab1, text="Дата наима", width="20")
lbl5.grid(column=0, row=9)
lbl5 = Label(tab1, text="* нужно заполнить все поля", width="20")
lbl5.grid(column=0, row=12)

text = tk.Text(tab1, width=25, height=5, wrap=WORD)
text.grid(column=1, row=1)
ttk.Separator(tab1,orient=HORIZONTAL).grid( column=0, columnspan=99,row=2, sticky="ew")
text2 = tk.Text(tab1, width=25, height=5, wrap=WORD)
text2.grid(column=1, row=3)
ttk.Separator(tab1,orient=HORIZONTAL).grid( column=0, columnspan=99,row=4, sticky="ew")
text3 = tk.Text(tab1, width=25, height=5, wrap=WORD)
text3.grid(column=1, row=5)
ttk.Separator(tab1,orient=HORIZONTAL).grid( column=0, columnspan=99,row=6, sticky="ew")
text4 = tk.Text(tab1, width=25, height=5, wrap=WORD)
text4.grid(column=1, row=7)
ttk.Separator(tab1,orient=HORIZONTAL).grid( column=0, columnspan=99,row=8, sticky="ew")
text5 = tk.Text(tab1, width=25, height=5, wrap=WORD)
text5.grid(column=1, row=9)

success_lable = Label(tab1, text="Успешно изменили!", width="20")


btn5 = Button(tab1, text="Изменить для всех*", command=show_but)
btn5.grid(column=1, row=12)

lbl_tab = Label(tab2, text="Имя")
lbl_tab.grid(column=0, row=0, sticky=W)
lbl_tab2 = Label(tab2, text="Зарплата")
lbl_tab2.grid(column=1, row=0, sticky=W)
lbl_tab3 = Label(tab2, text="Департамент")
lbl_tab3.grid(column=2, row=0, sticky=W)
lbl_tab4 = Label(tab2, text="Позиция")
lbl_tab4.grid(column=3, row=0, sticky=W)
lbl_tab5 = Label(tab2, text="Дата найма")
lbl_tab5.grid(column=4, row=0, sticky=W)



tab_control.pack(fill='both')
window.mainloop()