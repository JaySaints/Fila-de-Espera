from tkinter import *
from WinConnClient import *

db = ConnectionDB()

def clear_list():
    db.commit_cnx()
    n1_entry.delete(0, END)
    n2_entry.delete(0, END)
    n3_entry.delete(0, END)
    n4_entry.delete(0, END)
    n5_entry.delete(0, END)
    n6_entry.delete(0, END)
    n7_entry.delete(0, END)
    n8_entry.delete(0, END)
    n9_entry.delete(0, END)
    n10_entry.delete(0, END)

    h1_entry.delete(0, END)
    h2_entry.delete(0, END)
    h3_entry.delete(0, END)
    h4_entry.delete(0, END)
    h5_entry.delete(0, END)
    h6_entry.delete(0, END)
    h7_entry.delete(0, END)
    h8_entry.delete(0, END)
    h9_entry.delete(0, END)
    h10_entry.delete(0, END)




def show_list(tab):
    clear_list()
    if("list_AM" == tab):
        back_color = '#76c7fc'
        Label(client, text="MANHÃ", pady=10, bg=back_color).grid(row=0, column=0, stick=W+E)
    if("list_PM" == tab):
        back_color = '#faaa49'
        Label(client, text="TARDE", pady=10, bg=back_color).grid(row=0, column=0, stick=W+E)
    row = db.select_user(tab)
    client.configure(background=back_color)
    try:
        n1_entry.insert(0,str(row[0][0]))
        n2_entry.insert(0,str(row[1][0]))
        n3_entry.insert(0,str(row[2][0]))
        n4_entry.insert(0,str(row[3][0]))
        n5_entry.insert(0,str(row[4][0]))
        n6_entry.insert(0,str(row[5][0]))
        n7_entry.insert(0,str(row[6][0]))
        n8_entry.insert(0,str(row[7][0]))
        n9_entry.insert(0,str(row[8][0]))
        n10_entry.insert(0,str(row[9][0]))
    except Exception as e:
        pass
    try:
        h1_entry.insert(0,str(row[0][1]))
        h2_entry.insert(0,str(row[1][1]))
        h3_entry.insert(0,str(row[2][1]))
        h4_entry.insert(0,str(row[3][1]))
        h5_entry.insert(0,str(row[4][1]))
        h6_entry.insert(0,str(row[5][1]))
        h7_entry.insert(0,str(row[6][1]))
        h8_entry.insert(0,str(row[7][1]))
        h9_entry.insert(0,str(row[8][1]))
        h10_entry.insert(0,str(row[9][1]))
    except Exception as e:
        pass

###############################################################################
client = Tk()
client.title("Fila para Despacho")
client.geometry("384x310")
client.maxsize(384, 310)
global back_color
back_color = ''

master = LabelFrame(client, pady=10, padx=10)

n1_text = StringVar()
n1_label = Label(master, text='1.:')
n1_label.grid(row=0, column=0)
n1_entry = Entry(master, textvariable=n1_text)
n1_entry.grid(row=0, column=1)
h1_text = StringVar()
h1_entry = Entry(master, textvariable=h1_text)
h1_entry.grid(row=0, column=2)

n2_text = StringVar()
n2_label = Label(master, text='2.:')
n2_label.grid(row=1, column=0)
n2_entry = Entry(master, textvariable=n2_text)
n2_entry.grid(row=1, column=1)
h2_text = StringVar()
h2_entry = Entry(master, textvariable=h2_text)
h2_entry.grid(row=1, column=2)

n3_text = StringVar()
n3_label = Label(master, text='3.:')
n3_label.grid(row=2, column=0)
n3_entry = Entry(master, textvariable=n3_text)
n3_entry.grid(row=2, column=1)
h3_text = StringVar()
h3_entry = Entry(master, textvariable=h3_text)
h3_entry.grid(row=2, column=2)

n4_text = StringVar()
n4_label = Label(master, text='4.:')
n4_label.grid(row=3, column=0)
n4_entry = Entry(master, textvariable=n4_text)
n4_entry.grid(row=3, column=1)
h4_text = StringVar()
h4_entry = Entry(master, textvariable=h4_text)
h4_entry.grid(row=3, column=2)

n5_text = StringVar()
n5_label = Label(master, text='5.:')
n5_label.grid(row=4, column=0)
n5_entry = Entry(master, textvariable=n5_text)
n5_entry.grid(row=4, column=1)
h5_text = StringVar()
h5_entry = Entry(master, textvariable=h5_text)
h5_entry.grid(row=4, column=2)

n6_text = StringVar()
n6_label = Label(master, text='6.:')
n6_label.grid(row=5, column=0)
n6_entry = Entry(master, textvariable=n6_text)
n6_entry.grid(row=5, column=1)
h6_text = StringVar()
h6_entry = Entry(master, textvariable=h6_text)
h6_entry.grid(row=5, column=2)

n7_text = StringVar()
n7_label = Label(master, text='7.:')
n7_label.grid(row=6, column=0)
n7_entry = Entry(master, textvariable=n7_text)
n7_entry.grid(row=6, column=1)
h7_text = StringVar()
h7_entry = Entry(master, textvariable=h7_text)
h7_entry.grid(row=6, column=2)

n8_text = StringVar()
n8_label = Label(master, text='8.:')
n8_label.grid(row=7, column=0)
n8_entry = Entry(master, textvariable=n8_text)
n8_entry.grid(row=7, column=1)
h8_text = StringVar()
h8_entry = Entry(master, textvariable=h8_text)
h8_entry.grid(row=7, column=2)

n9_text = StringVar()
n9_label = Label(master, text='9.:')
n9_label.grid(row=8, column=0)
n9_entry = Entry(master, textvariable=n9_text)
n9_entry.grid(row=8, column=1)
h9_text = StringVar()
h9_entry = Entry(master, textvariable=h9_text)
h9_entry.grid(row=8, column=2)

n10_text = StringVar()
n10_label = Label(master, text='10.:')
n10_label.grid(row=9, column=0)
n10_entry = Entry(master, textvariable=n10_text)
n10_entry.grid(row=9, column=1)
h10_text = StringVar()
h10_entry = Entry(master, textvariable=h10_text)
h10_entry.grid(row=9, column=2)

master.grid(row=1, column=0)

btn_label = LabelFrame(client)

btn = Button(btn_label, text='ATUALIZAR', bg='#e1cc06', command= lambda: show_list(tab.get()))
btn.grid(row=0, column=1, stick=W+E, pady=10, padx=10)

global tab
tab = StringVar()
fradio = LabelFrame(btn_label)
Radiobutton(fradio, text='A.M', variable=tab, value='list_AM', command=lambda: show_list(tab.get())).grid(row=2, column=1)
Radiobutton(fradio, text='P.M', variable=tab, value='list_PM', command=lambda: show_list(tab.get())).grid(row=3, column=1)
tab.set('list_AM')
fradio.grid(row=0, column=0)

btn_label.grid(row=2, column=0)



show_list(tab.get())
client.mainloop()
