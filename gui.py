from tkinter import *
from tkinter import ttk
from functions import *



app = Tk()
app.title('Controle de Clientes')
app.iconbitmap('folder.ico')
#app.geometry('400x250')


class Application:
    def __init__(self, master=None):
        #utilizar o get para os dados das entrys e transferir para uma string e em seguida deletar o que tinha nos campos
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

        def pesquisar_id():
            i = self.id_p.get()
            l = ler_data(i)
            print(l)
            self.nome_p.insert(0, l[0])
            self.email_p.insert(0, l[1])
            self.endereco_p.insert(0, l[2])
            


            
            


        #definição do id_atual para atualizar id na página de cadastro
        id_atual = StringVar()
        id_atual.set(get_last_id())
        
        #configs gerais do app
        self.fontePadrao = ('Arial', '10')

        #criação da primeira aba
        app_aba = ttk.Notebook(app)
        app_aba.pack()
        frame_aba_cadastro = Frame(app_aba, width=400, height=250)
        frame_aba_cadastro.pack()
        app_aba.add(frame_aba_cadastro, text='Cadastro')
        
        #containers para os widgets aba de cadastro
        #1 titulo
        self.primeiroContainer = Frame(frame_aba_cadastro)
        self.primeiroContainer['pady'] = 10
        #self.primeiroContainer['width'] = 1000
        self.primeiroContainer.pack()
        

        #2 id
        self.segundoContainer = Frame(frame_aba_cadastro)
        self.segundoContainer['padx'] = 20
        #self.segundoContainer['width'] = 350
        self.segundoContainer.pack()

        #3 nome
        self.terceiroContainer = Frame(frame_aba_cadastro)
        self.terceiroContainer['padx'] = 20
        #self.terceiroContainer['width'] = 350
        self.terceiroContainer.pack()

        #4 email
        self.quartoContainer = Frame(frame_aba_cadastro)
        self.quartoContainer['pady'] = 10
        #self.quartoContainer['width'] = 350
        self.quartoContainer.pack()

        #5 endereco
        self.quintoContainer = Frame(frame_aba_cadastro)
        self.quintoContainer['pady'] = 10
        #self.quintoContainer['width'] = 350
        self.quintoContainer.pack()

        #6 botao salvar
        self.sextoContainer = Frame(frame_aba_cadastro)
        #self.sextoContainer['pady'] = 10
        self.sextoContainer.pack()

        #widgets da aba de cadastro

        #widget do container 1
        #título da tab da cadastro centralizado?
        self.titulo = Label(self.primeiroContainer, text = 'Dados do Cliente')
        self.titulo['font'] = self.fontePadrao
        self.titulo.pack(side=LEFT)

        #widget do container 2
        #mostra o id do cliente que esta sendo cadastrado
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
        #campo de nome
        self.nomeLabel = Label(self.terceiroContainer, text='Nome')
        self.nomeLabel.pack(side = LEFT)
        self.nomeLabel['font'] = self.fontePadrao
        self.nome = Entry(self.terceiroContainer)
        self.nome['width'] = 30
        self.nome['font'] = self.fontePadrao
        self.nome.pack(side=LEFT)
        
        #widget do container 4
        #campo de email
        self.emailLabel = Label(self.quartoContainer, text='Email')
        self.emailLabel.pack(side = LEFT)
        self.emailLabel['font'] = self.fontePadrao
        self.email = Entry(self.quartoContainer)
        self.email['width'] = 30
        self.email['font'] = self.fontePadrao
        self.email.pack(side=LEFT)
        
        #widget do container 5
        #campo de endereco
        self.enderecoLabel = Label(self.quintoContainer, text='Endereco')
        self.enderecoLabel.pack(side = LEFT)
        self.enderecoLabel['font'] = self.fontePadrao
        self.endereco = Entry(self.quintoContainer)
        self.endereco['width'] = 30
        self.endereco['font'] = self.fontePadrao
        self.endereco.pack(side=LEFT)

        #widget do container 6
        #botao salvar
        self.botao_salvar = Button(self.sextoContainer)
        self.botao_salvar['command'] = get_data
        self.botao_salvar['text'] = 'Salvar dados'
        #self.email['width'] = 30
        self.botao_salvar['font'] = self.fontePadrao
        self.botao_salvar.pack(side=LEFT)

        #criação da segunda aba pesquisa dos dados
        
        frame_aba_pesquisa = Frame(app_aba, width=400, height=250)
        frame_aba_pesquisa.pack()
        app_aba.add(frame_aba_pesquisa, text='Pesquisar')
        
        #containers para os widgets aba de pesquisa
        #1 titulo mostrando pesquisa por id
        self.primeiroContainer_p = Frame(frame_aba_pesquisa)
        self.primeiroContainer_p['pady'] = 10
        #self.primeiroContainer['width'] = 1000
        self.primeiroContainer_p.pack()
        

        #2 id
        self.segundoContainer_p = Frame(frame_aba_pesquisa)
        self.segundoContainer_p['padx'] = 20
        #self.segundoContainer['width'] = 350
        self.segundoContainer_p.pack()

        #3 nome
        self.terceiroContainer_p = Frame(frame_aba_pesquisa)
        self.terceiroContainer_p['padx'] = 20
        #self.terceiroContainer['width'] = 350
        self.terceiroContainer_p.pack()

        #4 email
        self.quartoContainer_p = Frame(frame_aba_pesquisa)
        self.quartoContainer_p['pady'] = 10
        #self.quartoContainer['width'] = 350
        self.quartoContainer_p.pack()

        #5 endereco
        self.quintoContainer_p = Frame(frame_aba_pesquisa)
        self.quintoContainer_p['pady'] = 10
        #self.quintoContainer['width'] = 350
        self.quintoContainer_p.pack()

        #6 botao salvar
        self.sextoContainer_p = Frame(frame_aba_pesquisa)
        #self.sextoContainer['pady'] = 10
        self.sextoContainer_p.pack()


        ###widgets da aba de pesquisa###


        #widget do container 1
        #título da tab da pesquisa centralizado?
        self.titulo_p = Label(self.primeiroContainer_p, text = 'Pesquisa por Id')
        self.titulo_p['font'] = self.fontePadrao
        self.titulo_p.pack(side=LEFT)

        #widget do container 2
        #id
        self.idLabel_p = Label(self.segundoContainer_p, text = 'id')
        self.idLabel_p.pack(side=LEFT)
        self.idLabel_p['font'] = self.fontePadrao
        # self.id = Label(self.segundoContainer, textvariable = id_atual)
        # self.id.pack(side=LEFT)
        # self.id['font'] = self.fontePadrao         
        self.id_p = Entry(self.segundoContainer_p)
        self.id_p['width'] = 5
        self.id_p['font'] = self.fontePadrao
        self.id_p.pack(side=LEFT)
        

        
        #widget do container 3
        #nome
        self.nomeLabel_p = Label(self.terceiroContainer_p, text='Nome')
        self.nomeLabel_p.pack(side = LEFT)
        self.nomeLabel_p['font'] = self.fontePadrao
        self.nome_p = Entry(self.terceiroContainer_p)
        self.nome_p['width'] = 30
        self.nome_p['font'] = self.fontePadrao
        self.nome_p.pack(side=LEFT)
        
        #widget do container 4
        #email
        self.emailLabel_p = Label(self.quartoContainer_p, text='Email')
        self.emailLabel_p.pack(side = LEFT)
        self.emailLabel_p['font'] = self.fontePadrao
        self.email_p = Entry(self.quartoContainer_p)
        self.email_p['width'] = 30
        self.email_p['font'] = self.fontePadrao
        self.email_p.pack(side=LEFT)
        
        #widget do container 5
        #endereco
        self.enderecoLabel_p = Label(self.quintoContainer_p, text='Endereco')
        self.enderecoLabel_p.pack(side = LEFT)
        self.enderecoLabel_p['font'] = self.fontePadrao
        self.endereco_p = Entry(self.quintoContainer_p)
        self.endereco_p['width'] = 30
        self.endereco_p['font'] = self.fontePadrao
        self.endereco_p.pack(side=LEFT)

        #widget do container 6
        #botao salvar
        # self.enderecoLabel = Label(self.quintoContainer, text='Endereco')
        # self.enderecoLabel.pack(side = LEFT)
        self.botao_salvar_p = Button(self.sextoContainer_p)
        self.botao_salvar_p['command'] = pesquisar_id
        self.botao_salvar_p['text'] = 'Pesquisar Cliente'
        #self.email['width'] = 30
        self.botao_salvar_p['font'] = self.fontePadrao
        self.botao_salvar_p.pack(side=LEFT)

        




        
        






Application(app)
app.mainloop()