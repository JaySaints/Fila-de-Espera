from tkinter import *
from tkinter import messagebox
from WinConnServer import *
import datetime

db = ConnectionDB()

# Area create funtions and actions
def set_tb(name_tb):
    if(name_tb == 1):
        aux='list_AM'
    if(name_tb == 2):
        aux = 'list_PM'
    return aux

def update():
    show_users()

def add_list():
    if( in_entry.get() == '' or  in_entry.get() == ' '):
        messagebox.showerror('Obrigatório!', 'Preencha o Campo Nome.')
    else:
        db.add_user(str(set_tb(tab.get())), str(in_entry.get()).lower())
        in_entry.delete(0, END)
        update()

def show_users():
    row = db.select_user(str(set_tb(tab.get())))
    listbox_1.delete(0, END)
    listbox_2.delete(0, END)
    listbox_3.delete(0, END)
    if(tab.get() == 1):
        turno = Label(master, text="MANHÃ", bg="#ff9900", fg="#000000")
        turno.grid(row=1, column=0)
    if(tab.get() == 2):
        turno = Label(master, text="TARDE", bg="#33cc33", fg="#000000", padx=5)
        turno.grid(row=1, column=0)
    i=0
    while i < len(row):
        listbox_1.insert(END, ("{} -".format(row[i][0]) ) )
        listbox_2.insert(END, ("{}".format(str(row[i][1]).upper() ) ) )
        listbox_3.insert(END, ("{}".format(row[i][2]) ) )
        i+=1

def remove_list():
    db.remove_user(str(set_tb(tab.get())), str(l1_entry.get()).lower())
    l1_entry.delete(0, END)
    update()

def select_item(event):
    try:
        global select_item
        index = listbox_2.curselection()[0]
        select_item = listbox_2.get(index)
        l1_entry.delete(0, END)
        l1_entry.insert(END, select_item)
    except IndexError:
        pass

# Area create widgts in Application
app = Tk()
app.title("FILA DE ESPERA")
app.geometry("443x360")
app.maxsize(443, 360)

frame = LabelFrame(app, bg="#999999")
frame.grid(row=0, column=0)

# Section add
master = LabelFrame(frame, text="Adicionar a Fila", padx=5, pady=5, bg="#336699")
fin = LabelFrame(master, text="Nome", padx=5, pady=5)
in_text = StringVar()
in_entry = Entry(fin, textvariable= in_text, borderwidth=1, width=25, bg='#ffffff', fg='#000000')
in_entry.grid(row=0, column=1, padx=5, pady=5)
# Button Enter
in_btn = Button(fin, text="Enter", bg='#000000', fg="#ffffff", width=8, font=('bold', 10), command=lambda: add_list())
in_btn.grid(row=0, column=2, padx=5, pady=5)
fin.grid(row=0, column=0)
master.grid(row=0, column=0, padx=10)

# Buttons Radios
fradio = LabelFrame(master, text="A.M || P.M", padx=5, pady=5)
tab = IntVar()
Radiobutton(fradio, text='A.M', variable=tab, value=1, command= lambda: update()).pack()
Radiobutton(fradio, text='P.M', variable=tab, value=2, command= lambda: update()).pack()
tab.set('1')
fradio.grid(row=0, column=3)

# LISTBOX
fbox = LabelFrame(frame, padx=5, pady=5, bg="#336699")
listbox_1 = Listbox(fbox, width=4, height=10, border=0)
listbox_1.grid(row=2, column=0)
listbox_2 = Listbox(fbox, width=22, height=10, border=0)
listbox_2.grid(row=2, column=1, columnspan=1)
listbox_3 = Listbox(fbox, width=22, height=10, border=0)
listbox_3.grid(row=2, column=2)
fbox.grid(row=1, column=0)

# Bind select in information_list
listbox_2.bind('<<ListboxSelect>>', select_item)

# Set name
faction = LabelFrame(frame, padx=5, pady=5, bg="#336699")
l1_text = StringVar()
l1_label = Label(faction, text="Nome.:", font=('bold', 10), bg="#336699")
l1_label.grid(row=8, column=0, stick=E)
l1_entry = Entry(faction, textvariable= l1_text, borderwidth=1, width=20, bg='#ffffff', fg='#606060')
l1_entry.grid(row=8, column=1, stick=W)
# Set buttons remove
l1_btn = Button(faction, text="Remover", bg='#ff0000', fg="#ffffff", font=('bold', 10), command=remove_list)
l1_btn.grid(row=8, column=3, padx=5, stick=W)
faction.grid(row=2, column=0)

# Foother
ffoo = LabelFrame(frame, pady=5, padx=5, bg="#336699")
dt = datetime.datetime.now()
foother_1 = Label(ffoo, text=str(dt.strftime('%d/%b/%Y - By P.J.S.')), bg="#336699")
foother_1.pack()
ffoo.grid(row=3, column=0, sticky=W+E)

show_users()
app.mainloop()
