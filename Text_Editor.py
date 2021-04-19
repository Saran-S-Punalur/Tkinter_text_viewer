"""
Simple NotePad/ Text Editor/ .tex editor / .tex primitive diary using Tkinter
https://github.com/Saran-S-Punalur/Tkinter_text_viewer
Saran S
18/04/2021 12:48:32pm
"""



import tkinter
from tkinter import filedialog
import datetime

#pyinstaller --onefile -w Tkinter_SaveTextSW.py
window = tkinter.Tk()
window.geometry("1100x800") 
window.resizable(0, 0)                 #make unresizable
window.title("Note pad")
window.iconbitmap("F:/PythonProjects/icons/blue_book.ico")
#window.configure(bg = 'blue')         #background colour
#window['background'] = '#876f78'       #background colour with hex code
#window.wm_attributes("-transparentcolor", 'saddle brown')     #make transparent
#------------------------Background image

bg = tkinter.PhotoImage(file = "F:/PythonProjects/images_sample/wood2.png")     #import image
img_label = tkinter.Label(window, image = bg)          #make image a label
img_label.place(x=0, y=0)                     #place label at origin

#  Read only r  
#  Read and Write r+  (beginning of file)
#  Write Only w   (over-written)
#  Write and Read w+  (over written)
#  Append Only a  (end of file)
#  Append and Read a+  (end of file
#======================================================================FUNCTIONS========================================================
now = datetime.datetime.now()
var1 = tkinter.IntVar()

def saved_notify():
    text_file = filedialog.askopenfilename(initialdir="c:/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
    text_file = open(text_file, 'w')
    text_file.write(tit_entry.get(1.0, "end") + cont_entry.get(1.0, "end") +  aut_entry.get(1.0, "end"))
    save_label = tkinter.Label(window, text =tit_entry.get(1.0, "end") + " saved")
    save_label.place(x=400, y= 725)
    window.after(2000, save_label.destroy)

def cleared_notify():
    aut_entry.delete(1.0, "end")
    tit_entry.delete(1.0, "end")
    cont_entry.delete(1.0, "end")
    clr_label = tkinter.Label(window, text = " Text is cleared")
    clr_label.place(x=400, y= 725)
    window.after(2000, clr_label.destroy)

def opening_notify():
    text_file = filedialog.askopenfilename(initialdir="C:/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
    text_file = open(text_file, 'r')
    the_data = text_file.read()
    cont_entry.insert("end", the_data)
    text_file.close()
    open_label = tkinter.Label(window, text = "Opening...")
    open_label.place( x= 400, y = 725)
    window.after(2000, open_label.destroy)

def add_date():
    if(var1.get()==1):
        cont_entry.insert(1.0, now)
    else:
        pass
#========================================================================================================================================
#-----------------------title
tit = tkinter.Label(window, text ="TITLE", fg = 'CadetBlue1', bg = 'saddle brown', font = 'bold')
tit.place(x=20, y=10)

tit_entry = tkinter.Text(window, bd = 5, height = 1, width =90, bg = 'bisque')
tit_entry.place(x=130,y=10)

#-----------------------Author
aut = tkinter.Label(window, text ="AUTHOR", fg = 'CadetBlue1', bg = 'saddle brown', font = 'bold')
aut.place(x=20, y=50)

aut_entry = tkinter.Text(window, bd = 5, height = 1, width =90, bg = 'bisque')
aut_entry.place(x=130,y=50)


#-----------------------Content
contnt = tkinter.Label(window, text = "CONTENT", fg = 'CadetBlue1', bg = 'saddle brown', font = 'bold')
contnt.place(x=20, y=90)

cont_entry = tkinter.Text(window,bd=5, bg = 'bisque')
cont_entry.place(x=130, y= 90, width = 950, height = 500)

#----------------------- date checkbutton

dated = tkinter.Checkbutton(window, text = "Add date and time", font = 'bold', variable = var1, command = add_date, onvalue = 1, offvalue = 0)
dated.place(x = 130, y = 625)

#-----------------------Save Button
save_btn = tkinter.Button(text = "Save", command = saved_notify)
save_btn.place(x=400, y = 675)

#-----------------------Clear Button

clr_btn = tkinter.Button(text = "Clear", command = cleared_notify)
clr_btn.place(x= 600, y = 675)

#----------------------- Open Button

opn_btn = tkinter.Button(text = "Open", command = opening_notify)
opn_btn.place(x= 800, y = 675)




window.mainloop()