import csv

#funcao que busca o ultimo id da coluna
def get_last_id():
    csv_file = open('cadastro.csv', 'r')
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        l = line['id']
    return int(l)+1
    csv_file.close()

#funcao que append uma nova linha de dados 
def escrever_data(nome, email, endereco):
    id = get_last_id()
    csv_file = open('cadastro.csv', 'a+')
    csv_writer = csv.DictWriter(csv_file, fieldnames = ['id', 'nome', 'email', 'endereco'], delimiter=',')
    csv_writer.writerow({'id': id, 'nome': nome, 'email': email, 'endereco': endereco})
    csv_file.close()

#função que busca uma linha de dados de acordo com o id selecionado
def ler_data(index):
    csv_file = open('cadastro.csv', 'r')
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        l = line['id']
        if l == index:
            print(line['nome'], end=' ')
            print(line['email'], end=' ')
            print(line['endereco'])




