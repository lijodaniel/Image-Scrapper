from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import datetime
import os
from tkinter import *
from tkinter import filedialog
# os.system('clear')
root = Tk()
root.title('Scrap the image')
root.geometry("600x400")
root.configure(background='#CCC')


text_label = Label(root,text="SCRAP IMAGE FROM ANY WEBSITE",font=("Calibri", 15))
text_label.pack(pady=30)

def browsetheFiles():
    folder = filedialog.askdirectory(initialdir=os.path.normpath("C://"), title="Example")
    label_folder_explorer.configure(text="Folder selected: " + folder)
    f = open("scrap/data.txt", "w")
    f.write(folder)
    f.close()

button_explore = Button(root,text = "Select folder to store",command = browsetheFiles)
button_explore.pack()

label_folder_explorer = Label(root,text = "Selected Folder path: ",width = 100, height = 4,fg = "blue")
label_folder_explorer.pack()

def hello():
    if myTextbox.get() == "":
        alert_label = Label(root, text='Enter Valid URL',fg = "red")
        alert_label.pack()
    else:
        hello_label = Label(root, text='Finished Scrape',fg = "green")
        hello_label.pack()

    htmldata = urlopen(myTextbox.get())
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')

    for item in images:
        print(item['src'])
        txt = item['src']
        y = txt.rsplit("/", 2)
        url = item['src']
        r = requests.get(url, allow_redirects=True)
        x = datetime.datetime.now()
        z = x.strftime("%f")
        f = open("scrap/data.txt", "r")
        selectedpath = f.read()
        path = selectedpath
        foldercreate = '/'+ y[1]
        folderPath = path + foldercreate
        try:
            os.mkdir(folderPath)
        except OSError as error:
            print(error)
        open(folderPath +'/' + z + '.png', 'wb').write(r.content)


enter_label = Label(root,text="Enter Website URL",font=("Calibri",  12))
enter_label.pack(pady=5)

myTextbox = Entry(root,width=40,font=("Calibri",18))
myTextbox.pack()

mybutton = Button(root,width=20,text="Submit", command=hello)
mybutton.pack(pady=20)

root.mainloop()
