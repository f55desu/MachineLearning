from sqlite3.dbapi2 import Cursor
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter.constants import END

con = sqlite3.connect("Lab8.2.db")  # подключение к базе данных
curs = con.cursor()

window = tk.Tk()
window.geometry('640x580')
font_mainLb = ('Arial', 35)
labelCreate = tk.Label(
    text= 'Создать новый аккаунт',
    font=font_mainLb
)
labelLastname = tk.Label(
    text='Фамилия'
)
entryLast = tk.Entry(
    width=50
)
labelFirstname = tk.Label(
    text='Имя'
)
entryFirst = tk.Entry(
    width=50
)
labelSecondname = tk.Label(
    text='Отчество'
)
entrySecond = tk.Entry(
    width=50
)
labelMail = tk.Label(
    text="Почта"
)
entryMail = tk.Entry(
    width=50
)
labelPassWord = tk.Label(
    text='Пароль'
)
entryPass = tk.Entry(
    width=50
)
labelBirth = tk.Label(
    text='Дата рождения'
)
spinBirthDay = ttk.Combobox(window)
for i in range(0, 30):  #Заполнение комбокса числами от 1 до 31
    spinBirthDay['values'] = tuple(list(spinBirthDay['values']) + [str(i+1)])
month = {0: 'Январь', 
         1: 'Февраль',
         2: 'Март',
         3: 'Апрель',
         4: 'Май',
         5: 'Июнь',
         6: 'Июль',
         7: 'Август',
         8: 'Сентябрь',
         9: 'Октябрь',
         10: 'Ноябрь',
         11: 'Декабрь'}
spinBirthMonth = ttk.Combobox(window)
for i in range(len(month)): #Заполнение комбокса словарём месяцев
    spinBirthMonth['values'] = tuple(list(spinBirthMonth['values']) + [month[i]])

spinBirthYear = ttk.Combobox(window)
for i in range(0, 2021-1920): #Заполнение комбокса числами от 1920 до 2021
    spinBirthYear['values'] = tuple(list(spinBirthYear['values']) + [str((i-2021)*-1)])

var = tk.IntVar()
def check():
    check = var.get()
    return check
radioMan = tk.Radiobutton(
    value=0,
    variable=var,   
    text='Мужчина',
    command=check
)
radioWoman = tk.Radiobutton(
    value=1,
    variable=var,
    text='Женщина',
    command=check
)
radioOther = tk.Radiobutton(
    value=2,
    variable=var,
    command=check,
    text='Другое'
)
font_Button= ('Arial', 14)

def click():
    last = entryLast.get()
    first = entryFirst.get()
    second = entrySecond.get()
    mail = entryMail.get()
    entrPass = entryPass.get()
    spinDay = spinBirthDay.get()
    spinMonth = spinBirthMonth.get()
    spinYear = spinBirthYear.get()
    if check() == 0:
        gender = 'Мужчина'
    if check() == 1:
        gender = 'Женщина'
    if check() == 2:
        gender = 'Другое'

    sendtoDB(last, first, second, mail, entrPass, spinDay + ' ' + spinMonth + ' ' + spinYear, (str)(gender)) # Отправляем базу данных
    
def sendtoDB(last, name, middle, mail, password, birthDate, gender):
    curs.execute(f"""INSERT INTO Persons
                  VALUES ('{last}', '{name}', '{middle}', '{mail}', '{password}', '{birthDate}', '{gender}')"""
               )
    # Сохраняем изменения
    con.commit()

saveButt = tk.Button(
    borderwidth= 3,
    width=20,
    font= font_Button,
    text='Создать аккаунт',
    command=click
)

def table():
    tableWindow = tk.Toplevel(window) # второе окно от основного
    tableWindow.geometry('1680x840')

    if search_entry.get()=='': 
        curs.execute("SELECT * FROM Persons")
        lst = curs.fetchall()
        if len(lst) == 0:  # проверка на количество записей в таблице
            messagebox.showerror('Ошибка', 'В таблице нет записей!')
            return 0
   
        # создание таблицы
        total_rows = len(lst)
        total_colums = len(lst[0])
        for i in range(total_rows):
            for j in range(total_colums):
                entry = tk.Entry(tableWindow, width=20, fg='black',
                               font=('Arial', 16, 'bold'))
                entry.grid(row=i, column=j)
                entry.insert(END, lst[i][j])
    else:    
        curs.execute(f"SELECT * FROM Persons WHERE _lastname='{search_entry.get()}' OR _name='{search_entry.get()}' OR _middlename='{search_entry.get()}'")
        list=curs.fetchall()
        if len(list) == 0:  # проверка на количество записей в таблице
            messagebox.showerror('Ошибка', 'Нет таких записей!')
            return 0

         # создание таблицы
        total_rows = len(list)
        total_colums = len(list[0])
        for i in range(total_rows):
             for j in range(total_colums):
                 entry = tk.Entry(tableWindow, width=20, fg='black',
                               font=('Arial', 16, 'bold'))
                 entry.grid(row=i, column=j)
                 entry.insert(END, list[i][j])

tableButt = tk.Button(
    borderwidth= 3,
    width=20,
    font= font_Button,
    text='Открыть таблицу',
    command=table
)

search_label = tk.Label(
    window, 
    text='Поиск'
)
search_entry = tk.Entry(
    window, 
    bg='#fff', 
    fg='#444'
)

labelCreate.pack()
labelLastname.pack()
entryLast.pack()
labelFirstname.pack()
entryFirst.pack()
labelSecondname.pack()
entrySecond.pack()
labelMail.pack()
entryMail.pack()
labelPassWord.pack()
entryPass.pack()
labelBirth.pack()
spinBirthDay.place(x= 210, y=290, width=40)
spinBirthMonth.place(x= 255, y=290, width=100)
spinBirthYear.place(x= 360, y=290, width=60)
radioMan.place(x= 175, y=320)
radioWoman.place(x= 260, y=320)
radioOther.place(x= 360, y=320)
saveButt.place(x= 205, y=350)
search_label.place(x = 300, y = 410)
search_entry.place(x = 198, y = 430, width=250)
tableButt.place(x= 205, y=460)

##lopped tkinter##
window.mainloop()