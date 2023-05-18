import sqlite3


def conectar(arquivo):
    conexao = sqlite3.connect(arquivo)
    conexao.cursor()
    # print('Conectado')
    return conexao


def executar(dados):
    fet = None
    try:
        res = conectar()
        fet = res.execute(dados)
        res.commit()
    except:
        res = True

    return res, fet


def criar_tabela(dados):
    res = executar(dados)
    # print(res) so pra ver oque é :-/
    if res[0] == True:
        print('ERRO')


def ver_dados(dados):
    res = executar(dados)
    fet = res[1].fetchall()
    return fet


def add_or_att_dados(dados):
    executar(dados)
