import os
from utilidades.menu import conectar

caminho = 'dados\\clientes.db'
conexao = conectar(caminho)
conexao.close()
