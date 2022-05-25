import os
def openFile(findingFile):
    for root, dirs, files in os.walk("C:\\Windows\\system32", topdown=False):
        for name in files:
            currName = os.path.join(name)
            if (currName == findingFile):
                file = root + '\\' + name
                print(f"File dirrectory: {file}")
                os.system(file)
app = True
while(app):
    print("1 - Notepad")
    print("2 - Paint")
    print("3 - Calculator")
    print("0 - Exit")
    choise = input("Choise your app: ")
    if (choise == "1"):
        openFile("notepad.exe")
        continue
    if (choise == "2"):
        openFile("mspaint.exe")
        continue
    if (choise == "3"):
        openFile("calc.exe")
        continue
    if (choise == "0"):
        app = False