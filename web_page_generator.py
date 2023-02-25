
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title('Web Page Generator')
        self.btn = Button(self.master, text='Default HTML Page', width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))

        self.btn = Button(self.master, text='Submit Custom Text', width=30, height=2, command=self.customHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))

   
       #this creates the box to type in
        e = Entry(root, width=50)
        e.grid()

        
        #function that connects input box to do something with input
    def get_data():
        label.config(text= e.get())




    def customHTML(self):
        htmlText = (get_data)
        htmlFile = open('index.html', 'w')
        htmlContent = '<html>\n<body>\n<h1>' + htmlText + '</html>\n</body>\n</h1>'
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab('index.html')

        


        #this will run if they click on default thing
    def defaultHTML(self):
        htmlText = 'Stay tuned for our amazing summer sale!'
        htmlFile = open('index.html', 'w')
        htmlContent = '<html>\n<body>\n<h1>' + htmlText + '</html>\n</body>\n</h1>'
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab('index.html')






if __name__=='__main__':
    root= tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
