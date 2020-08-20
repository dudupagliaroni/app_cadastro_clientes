from tkinter import *
from functions import *


app = Tk()
app.title('Marcador de Gado')
app.geometry('400x250')

class InfoBox(Frame):
    def __init__(self, app, info):
        Frame.__init__(self, app)
        self.nome_label = Label(self, text=info)
        self.nome_entry = Entry(self)
        self.nome_label.pack(side = LEFT)
        self.nome_entry.pack()

panel_nome = InfoBox(app, 'NAME')  
panel_nome.pack()
panel_nome = InfoBox(app, 'EMAIL')  
panel_nome.pack()
panel_nome = InfoBox(app, 'ENDEREÇO')  
panel_nome.pack()

app.mainloop()