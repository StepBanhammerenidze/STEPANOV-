from tkinter import *
list_ = ["11","12","13","14","16"]
foto_list=["11.png","12.png","13.png","14.png"]
global can, pc
def list_to_txt(event):
    global can, pc
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    print(lbox.get(valik[0]))
    can.delete(ALL)
    pc = PhotoImage(file=foto_list[valik[0]])
    print(foto_list[valik[0]])
    can.create_image(0,0,image=pc,anchor=NW)
   

def txt_to_list(event):
    text=text.get(0.0,END)
    text=text[-2:-1]
    if text--"/n":
        pass
    else:
        foto_list.append(text)
        lbox.config(height=len(foto_list))
        lbox.insert(END,text)
        txt.delete(0.0,END)
        text-""

def opisanie():
    text = txt.get(0.0, END)
    print(list(text))
    if text=="11.png\n":
        ttt="BMW WAS \BEATIFUL \FAST \n 22000 Euro "
    elif text=="12.png\n":
        ttt="BMW FAST \n LOW \n FAST CAR \n 11500 Euro "
    elif text=="13.png\n":
        ttt="BMW MID\n MID CAR \n SLOW \n 8200 Euro "
    elif text=="14.png\n":
        ttt="BMW CLASSIC \n MID \n MID \n NORMAL \n 63400 Euro "
    opis.config(text=ttt)



win=Tk()
lbox=Listbox(win,width=20,height=len(foto_list),selectmode=SINGLE)
for element in foto_list:
    lbox.insert(END,element)

lbox.grid()
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=5,width=30,wrap=WORD)
txt.grid(row=2)
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=200,height=200,bg="white")
pc = PhotoImage(file="")#220px-PelobatesFuscus.png
foto=PhotoImage(file="12.png")
bt=Button(text='CARS', command=opisanie).grid(row=1, column=8)#, command=op
opis=Label(win, text="", width=110, height=20)
opis.grid(row=1, column=1)
can.grid(row=1, column=15)
win.mainloop()
