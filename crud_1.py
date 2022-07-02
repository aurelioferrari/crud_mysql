import mysql.connector
import mysql



# conexão
cond = True
while cond == True:
    database = str(input('Qual o nome do banco de dados? '))
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database=database,

        )
        cursor = conexao.cursor()
        cond = False
    except:
        print('Base de dados inexistente.\nDigite de novo.\n')

#cursor




# opção do usuário
lista_opcoes = ['C', 'R', 'U', 'D']
opcao = str(input('Selecione um comando: [c] Criar novo produto.\n[r] Ver a lista de produtos.\n'
                  '[u] Modificar o valor de um produto\n[d] Deletar um produto.')).strip().upper()[0]
while opcao not in lista_opcoes:
    opcao = str(input('Selecione um comando: [c] Criar novo produto.\n[r] Ver a lista de produtos.\n'
                      '[u] Modificar o valor de um produto\n[d] Deletar um produto.')).strip().upper()[0]
else:
    pass

# create
if opcao == 'C':
    nome_produto = str(input('Qual o nome do produto? '))
    valor = float(input('Qual o valor do produto? '))
    comando = f'insert into vendas (nome_produto, valor) values ("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()

# read
if opcao == 'R':
    while True:
        try:
            tabela = str(input('Qual o nome da tabela que você quer acessar? '))
            comando = f'select * from {tabela}'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print('-'*40)
            print(F'{"LISTA DE PRODUTOS":^40}')
            print('-' * 40)
            for i in resultado:
                print(f'{i[0]:<3} {i[1]:<20} R$ {i[2]:.2f}'.replace('.', ','))
            break
        except:
            print('Essa tabela não existe neste arquivo.')


# update
if opcao == 'U':
    while True:
        try:
            tabela = str(input('Qual o nome da tabela que você quer acessar? '))
            comando = f'select * from {tabela}'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            break
        except:
            print('Essa tabela não existe neste arquivo.')
    count = 0
    while count == 0:
        nome_produto = str(input('Qual o nome do produto que você deseja mudar o preço? '))

        for i in resultado:
            if i[1] == nome_produto:
                count += 1
        if count > 0:
            valor = float(input('Qual o novo valor do produto? '))
            comando = f'update vendas set valor = {valor} where nome_produto = "{nome_produto}"'
            cursor.execute(comando)
            conexao.commit()
        else:
            print('Esse produto não está registrado no sistema.')

# delete
if opcao == 'D':
    while True:
        try:
            tabela = str(input('Qual o nome da tabela que você quer acessar? '))
            comando = f'select * from {tabela}'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            break
        except:
            print('Essa tabela não existe neste arquivo.')
    count = 0
    while count == 0:
        nome_produto = str(input('Qual o nome do produto que você deseja deletar? '))

        for i in resultado:
            if i[1] == nome_produto:
                count += 1
        if count > 0:
            comando = f'delete from vendas where nome_produto = "{nome_produto}"'
            cursor.execute(comando)
            conexao.commit()
        else:
            print('Esse produto não está registrado no sistema.')


conexao.close()
cursor.close()