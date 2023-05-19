import sqlite3


def conectar(conexao):
    conexao = sqlite3.connect(conexao)
    conexao.cursor()
    # print('Conectado')
    return conexao


def executar(dados, conexao):
    fet = None
    try:
        res = conectar(conexao)
        fet = res.execute(dados)
        res.commit()
    except:
        res = True

    return res, fet


def criar_tabela(dados, conexao):
    res = executar(dados, conexao)
    # print(res) so pra ver oque é :-/
    if res[0] == True:
        print('ERRO')


def ver_dados(dados, conexao):
    res = executar(dados,conexao)
    fet = res[1].fetchall()
    return fet


def add_or_att_dados(dados, conexao):
    executar(dados, conexao)
