from tkinter import *
from functions import *



app = Tk()
app.title('Marcador de Gado')
app.geometry('400x250')


class Application:
    def __init__(self, master=None):
        #utilizar o Get para pegar os dados das entrys e em seguida deletar o que tinha nos campos
        def get_data():
            id_atual.set(get_last_id()+1)
            nome_data = str(self.nome.get())
            email_data = str(self.email.get())
            endereco_data = str(self.endereco.get())
            self.nome.delete(0,END)
            self.email.delete(0, END)
            self.endereco.delete(0, END)
            
            #utilizar o botão de salvar dados para escrever os dados no csv        
            escrever_data(nome_data, email_data, endereco_data)

        #definição do id_atual para atualizar id na página de cadastro
        id_atual = StringVar()
        id_atual.set(get_last_id())
        
        #configs gerais do app
        self.fontePadrao = ('Arial', '10')
        
        #containers para os widgets aba de cadastro
        #1 titulo
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer['width'] = 1000
        self.primeiroContainer.pack()

        #2 id
        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer['width'] = 350
        self.segundoContainer.pack()

        #3 nome
        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer['width'] = 350
        self.terceiroContainer.pack()

        #4 email
        self.quartoContainer = Frame(master)
        self.quartoContainer['pady'] = 10
        self.quartoContainer['width'] = 350
        self.quartoContainer.pack()

        #5 endereco
        self.quintoContainer = Frame(master)
        self.quintoContainer['pady'] = 10
        self.quintoContainer['width'] = 350
        self.quintoContainer.pack()

        #6 botao salvar
        self.sextoContainer = Frame(master)
        self.sextoContainer['pady'] = 10
        self.sextoContainer.pack()

        #widgets da aba de cadastro

        #widget do container 1
        #título da tab da cadastro centralizado?
        self.titulo = Label(self.primeiroContainer, text = 'Dados do Gado')
        self.titulo['font'] = self.fontePadrao
        self.titulo.pack()

        #widget do container 2
        #id
        self.idLabel = Label(self.segundoContainer, text = 'id')
        self.idLabel.pack(side=LEFT)
        self.idLabel['font'] = self.fontePadrao
        self.id = Label(self.segundoContainer, textvariable = id_atual)
        self.id.pack(side=LEFT)
        self.id['font'] = self.fontePadrao         
        # self.id = Entry(self.segundoContainer)
        # self.id['width'] = 5
        # self.id['font'] = self.fontePadrao
        # self.id.pack(side=LEFT)
        # self.id.insert(0, get_last_id())

        
        #widget do container 3
        #nome
        self.nomeLabel = Label(self.terceiroContainer, text='Nome')
        self.nomeLabel.pack(side = LEFT)
        self.nomeLabel['font'] = self.fontePadrao
        self.nome = Entry(self.terceiroContainer)
        self.nome['width'] = 30
        self.nome['font'] = self.fontePadrao
        self.nome.pack(side=LEFT)
        
        #widget do container 4
        #email
        self.emailLabel = Label(self.quartoContainer, text='Email')
        self.emailLabel.pack(side = LEFT)
        self.emailLabel['font'] = self.fontePadrao
        self.email = Entry(self.quartoContainer)
        self.email['width'] = 30
        self.email['font'] = self.fontePadrao
        self.email.pack(side=LEFT)
        
        #widget do container 5
        #endereco
        self.enderecoLabel = Label(self.quintoContainer, text='Endereco')
        self.enderecoLabel.pack(side = LEFT)
        self.enderecoLabel['font'] = self.fontePadrao
        self.endereco = Entry(self.quintoContainer)
        self.endereco['width'] = 30
        self.endereco['font'] = self.fontePadrao
        self.endereco.pack(side=LEFT)

        #widget do container 6
        #botao salvar
        # self.enderecoLabel = Label(self.quintoContainer, text='Endereco')
        # self.enderecoLabel.pack(side = LEFT)
        self.botao_salvar = Button(self.sextoContainer)
        self.botao_salvar['command'] = get_data
        self.botao_salvar['text'] = 'Salvar dados'
        #self.email['width'] = 30
        self.botao_salvar['font'] = self.fontePadrao
        self.botao_salvar.pack(side=LEFT)

        




        
        






Application(app)
app.mainloop()