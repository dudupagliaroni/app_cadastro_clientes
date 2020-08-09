from tkinter import *
from tkinter import ttk
from functions import *

#utilizar o get para os dados das entrys e transferir para uma string e em seguida deletar o que tinha nos campos
def get_data():
    id_atual.set(get_last_id()+1)
    nome_data = str(nome.get())
    email_data = str(email.get())
    endereco_data = str(endereco.get())
    nome.delete(0,END)
    email.delete(0, END)
    endereco.delete(0, END)
    
    #utilizar o botão de salvar dados para ativar a função de escrever os dados no csv        
    escrever_data(nome_data, email_data, endereco_data)

#função que busca por id e insert as informações retornadas nas entrys
def pesquisar_id():
    i = id_p.get()
    l = ler_data(i)
    print(l)
    nome_p.delete(0, END)
    email_p.delete(0, END)
    endereco_p.delete(0, END)
    nome_p.insert(0, l[0])
    email_p.insert(0, l[1])
    endereco_p.insert(0, l[2])

app = Tk()
app.title('Controle de Clientes')
app.iconbitmap('folder.ico')
#app.geometry('500x250')

#criação da primeira aba
app_aba = ttk.Notebook(app)
app_aba.pack()
frame_aba_cadastro = Frame(app_aba, width=500, height=250)
frame_aba_cadastro.pack()
app_aba.add(frame_aba_cadastro, text='Cadastro')
#configs gerais do app
app_fonte_padrao = ('Arial', '10')

#definição do id_atual para atualizar id na página de cadastro
id_atual = StringVar()
id_atual.set(get_last_id())

#containers para os widgets aba de cadastro
#1 titulo
primeiroContainer = Frame(frame_aba_cadastro)
primeiroContainer['pady'] = 10
#primeiroContainer['width'] = 1000
primeiroContainer.pack()

#2 id
segundoContainer = Frame(frame_aba_cadastro)
segundoContainer['padx'] = 10
#segundoContainer['width'] = 350
segundoContainer.pack()

#3 nome
terceiroContainer = Frame(frame_aba_cadastro)
terceiroContainer['padx'] = 10
#terceiroContainer['width'] = 350
terceiroContainer.pack()

#4 email
quartoContainer = Frame(frame_aba_cadastro)
quartoContainer['pady'] = 10
#quartoContainer['width'] = 350
quartoContainer.pack()

#5 endereco
quintoContainer = Frame(frame_aba_cadastro)
quintoContainer['pady'] = 10
#quintoContainer['width'] = 350
quintoContainer.pack()

#6 botao salvar
sextoContainer = Frame(frame_aba_cadastro)
#sextoContainer['pady'] = 10
sextoContainer.pack()

##widgets da aba de cadastro##

#widget do container 1
#título da tab da cadastro centralizado?
titulo = Label(primeiroContainer, text = 'Cadastro de Clientes')
titulo['font'] = app_fonte_padrao
titulo.pack(side=LEFT)

#widget do container 2
#mostra o id do cliente que esta sendo cadastrado
idLabel = Label(segundoContainer, text = 'Número do cadastro: ')
idLabel.pack(side=LEFT)
idLabel['font'] = app_fonte_padrao
id = Label(segundoContainer, textvariable = id_atual)
id.pack(side=LEFT)
id['font'] = app_fonte_padrao         

#widget do container 3
#campo de nome
nomeLabel = Label(terceiroContainer, text='Nome')
nomeLabel.pack(side = LEFT)
nomeLabel['font'] = app_fonte_padrao
nome = Entry(terceiroContainer)
nome['width'] = 30
nome['font'] = app_fonte_padrao
nome.pack(side=LEFT)

#widget do container 4
#campo de email
emailLabel = Label(quartoContainer, text='Email')
emailLabel.pack(side = LEFT)
emailLabel['font'] = app_fonte_padrao
email = Entry(quartoContainer)
email['width'] = 30
email['font'] = app_fonte_padrao
email.pack(side=LEFT)

#widget do container 5
#campo de endereco
enderecoLabel = Label(quintoContainer, text='Endereco')
enderecoLabel.pack(side = LEFT)
enderecoLabel['font'] = app_fonte_padrao
endereco = Entry(quintoContainer)
endereco['width'] = 30
endereco['font'] = app_fonte_padrao
endereco.pack(side=LEFT)

#widget do container 6
#botao salvar
botao_salvar = Button(sextoContainer)
botao_salvar['command'] = get_data
botao_salvar['text'] = 'Salvar dados'
#email['width'] = 30
botao_salvar['font'] = app_fonte_padrao
botao_salvar.pack(side=LEFT, pady=10)

##criação da segunda aba pesquisa dos dados##
#############################################

frame_aba_pesquisa = Frame(app_aba, width=500, height=250)
frame_aba_pesquisa.pack()
app_aba.add(frame_aba_pesquisa, text='Pesquisa')

#containers para os widgets aba de pesquisa
#1 titulo mostrando pesquisa por id
primeiroContainer_p = Frame(frame_aba_pesquisa)
primeiroContainer_p['pady'] = 10
#primeiroContainer['width'] = 1000
primeiroContainer_p.pack()

#2 id
segundoContainer_p = Frame(frame_aba_pesquisa)
segundoContainer_p['padx'] = 10
#segundoContainer['width'] = 350
segundoContainer_p.pack()

#3 nome
terceiroContainer_p = Frame(frame_aba_pesquisa)
terceiroContainer_p['padx'] = 10
#terceiroContainer['width'] = 350
terceiroContainer_p.pack()

#4 email
quartoContainer_p = Frame(frame_aba_pesquisa)
quartoContainer_p['pady'] = 10
#quartoContainer['width'] = 350
quartoContainer_p.pack()

#5 endereco
quintoContainer_p = Frame(frame_aba_pesquisa)
quintoContainer_p['pady'] = 10
#quintoContainer['width'] = 350
quintoContainer_p.pack()

#6 botao salvar
sextoContainer_p = Frame(frame_aba_pesquisa)
# sextoContainer['pady'] = 10
sextoContainer_p.pack()


###widgets da aba de pesquisa###


#widget do container 1
#título da tab da pesquisa centralizado?
titulo_p = Label(primeiroContainer_p, text = 'Pesquisar por Número do Cadastro')
titulo_p['font'] = app_fonte_padrao
titulo_p.pack(side=LEFT)

#widget do container 2
#id
idLabel_p = Label(segundoContainer_p, text = 'Número do Cadastro: ')
idLabel_p.pack(side=LEFT)
idLabel_p['font'] = app_fonte_padrao 
id_p = Entry(segundoContainer_p)
id_p['width'] = 5
id_p['font'] = app_fonte_padrao
id_p.pack(side=LEFT)

#widget do container 3
#nome
nomeLabel_p = Label(terceiroContainer_p, text='Nome')
nomeLabel_p.pack(side = LEFT)
nomeLabel_p['font'] = app_fonte_padrao
nome_p = Entry(terceiroContainer_p)
nome_p['width'] = 30
nome_p['font'] = app_fonte_padrao
nome_p.pack(side=LEFT)

#widget do container 4
#email
emailLabel_p = Label(quartoContainer_p, text='Email')
emailLabel_p.pack(side = LEFT)
emailLabel_p['font'] = app_fonte_padrao
email_p = Entry(quartoContainer_p)
email_p['width'] = 30
email_p['font'] = app_fonte_padrao
email_p.pack(side=LEFT)

#widget do container 5
#endereco
enderecoLabel_p = Label(quintoContainer_p, text='Endereco')
enderecoLabel_p.pack(side = LEFT)
enderecoLabel_p['font'] = app_fonte_padrao
endereco_p = Entry(quintoContainer_p)
endereco_p['width'] = 30
endereco_p['font'] = app_fonte_padrao
endereco_p.pack(side=LEFT)

#widget do container 6
#botao salvar
# enderecoLabel = Label(quintoContainer, text='Endereco')
# enderecoLabel.pack(side = LEFT)
botao_salvar_p = Button(sextoContainer_p)
botao_salvar_p['command'] = pesquisar_id
botao_salvar_p['text'] = 'Pesquisar Cliente'
#email['width'] = 30
botao_salvar_p['font'] = app_fonte_padrao
botao_salvar_p.pack(side=LEFT, pady=10)

 

app.mainloop()