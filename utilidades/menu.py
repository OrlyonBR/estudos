from utilidades.funçoes import *
#from os import system as sistema

def tela():
    arq = str(input('Abrir arquivo (caminho/arquivo.db):')).strip()
    while True:
        res = str(input(f'{"-=" * 8}MENU{"-=" * 8}'
                        f'\n1 - CRIAR TABELA'
                        f'\n2 - ADICIONAR DADOS'
                        f'\n3 - VER TABELA'
                        f'\n4 - PESQUISAR NA TABELA'
                        f'\n5 - ATUALIZAR DADOS'
                        f'\n6 - APAGAR TABELA'
                        f'\n7 - MUDAR ARQUIVO'
                        f'\n7 - SAIR'
                        f'\nOPÇÃO: '))

        if res == '1':
            nome_tab = str(input('Nome da tabela: ')).strip().upper()
            lista_dados = list()

            while True:
                # Recebe os dados para colocar na tabela Exemplo: NOME, TELEFONE, E-MAIL
                nome_dados = str(input('Nome dos dados: ')).strip().upper()
                per = str(input('Adicionar mais dados [S/N]:')).upper()
                lista_dados.append(nome_dados)
                if per == 'N':
                    break

            # Pega os dados e formata para o tipo sqlite3 Exemplo: ('nome', 'telefone', 'email')
            dados = str()
            for dado in lista_dados:
                if dado == lista_dados[-1]:
                    dados = dados + f"'{dado}'"
                else:
                    dados = dados + f"'{dado}', "

            #print(dados) exibe como ficaram os dados

            criar_tabela(f'''CREATE TABLE {nome_tab}({dados})''', arq)

        elif res == '2':
            print(ver_dados('SELECT name FROM sqlite_master;', arq))
            res = str(input('Qual Tabela: ')).strip().upper()
            #nome tabelas
            res2 = (ver_dados(f'PRAGMA table_info({res})', arq))
            dados = list()
            for dado in res2:
                dados.append(dado[1])
            #dados tabela
            valores = str()
            for c in dados:
                res2 = str(input(f'{c}: ')).strip()
                if c == dados[-1]:
                    valores = valores + f"'{res2}'"
                else:
                    valores = valores + f"'{res2}', "

            teste = str()
            for dado in dados:
                if dado == dados[-1]:
                    teste = teste + f"{dado}"
                else:
                    teste = teste + f"{dado}, "

            add_or_att_dados(f'INSERT INTO {res} ({teste}) VALUES ({valores})', arq)

        elif res == '3':
            try:
                print(ver_dados('SELECT name FROM sqlite_master;', arq))
                res = str(input('Qual Tabela: ')).upper()
                #mostra o nome da tabela
                res2 = (ver_dados(f'PRAGMA table_info({res})', arq))

                for c in res2:
                   print(f'[{c[1]:^18}]', end='')

                #mostra os dados da tabela
                res = ver_dados(f'SELECT * FROM {res}', arq)
                print()
                for c in res:
                    for cont in c:
                        print(f'[{cont:^18}]', end='')
                    print()
                print()

            except:
                print(f'{"-=" * 5}>A tabela não tem dados<{"-=" * 5}')

        elif res == '4':
            print(ver_dados('SELECT name FROM sqlite_master;', arq))
            res = str(input('Qual Tabela: ')).upper()
            res2 = ver_dados(f'PRAGMA table_info({res})', arq)
            for c in res2:
                print(f'[{c[1]:^18}]', end=' ')

            res3 = str(input('\nQual coluna: ')).strip().upper()
            res4 = str(input('Pesquisar: ')).strip()
            #print(f"SELECT * FROM {res} WHERE {res2} LIKE '{res3}%'")
            res = ver_dados(f"SELECT * FROM {res} WHERE {res3} LIKE '%{res4}%'", arq)
            for c in res2:
                print(f'[{c[1]:^18}]', end='')
            print()
            for c in res:
                for cont in c:
                    print(f'[{cont:^18}]', end='')
                print()
        elif res == '5':
            print(ver_dados('SELECT name FROM sqlite_master;', arq))
            res = str(input('Qual Tabela: ')).strip().upper()
            res2 = (ver_dados(f'PRAGMA table_info({res})', arq))

            for c in res2:
                print(f'[{c[1]:^18}]', end='')

            res3 = ver_dados(f'SELECT * FROM {res}', arq)
            print()
            for c in res3:
                for cont in c:
                    print(f'[{cont:^18}]', end='')
                print()

            res4 = str(input('Atualizar: ')).strip()
            res5 = str(input('Para: ')).strip()
            res6 = str(input('Coluna: ')).strip().upper()
            #print(f"UPDATE {res} SET {res6} = '{res5}' WHERE {res6} = '{res4}'")
            add_or_att_dados(f"UPDATE {res} SET {res6} = '{res5}' WHERE {res6} = '{res4}'", arq)

        elif res == '6':
            print('Ainda não foi feita')

        elif res == '7':
            arq = str(input('Qual arquivo (caminho/arquivo.db):')).strip()

        elif res == '8':
            print(f'{"-=" * 5}>PROGRAMA ENCERRADO<{"-=" * 5}')
            break
