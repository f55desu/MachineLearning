# ЗАЩИЩЕНО АВТОРСКИМ ПРАВОМ © Taldykin Corp.

from colorama import *

#text = input("Введите текст: ")
f = open('C:\\Stuff\大学\\Python\\Lab5.2.txt', 'r')
text = f.read()
findingStr = input("Введите искомую строку: ")

text = text.replace(findingStr, Fore.YELLOW + findingStr + Style.RESET_ALL)

print(text)