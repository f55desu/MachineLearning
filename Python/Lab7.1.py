import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('640x480')
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
    spinBirthYear['values'] = tuple(list(spinBirthYear['values']) + [str(i+1920)])

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

    f = open('E:\\大学\\Python\\Lab7.2.txt', 'a')
    f.write(f"Аккаунт:\n Фамилия: {last}\n Имя: {first}\n Отчество: {second}\n Почта: {mail}\n Пароль: {entrPass}\n Дата рождения: {spinDay} {spinMonth} {spinYear}\n Пол: {gender}\n")


saveButt = tk.Button(
    borderwidth= 3,
    width=20,
    font= font_Button,
    text='Создать аккаунт',
    command=click
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

##lopped tkinter##
window.mainloop()