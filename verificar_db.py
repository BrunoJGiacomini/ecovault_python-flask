""""
import sqlite3

conexao = sqlite3.connect("instance/ecovault.db")

cursor = conexao.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tabelas = cursor.fetchall()

print("Tabelas encontradas:")

for tabela in tabelas:
    print(tabela)

conexao.close()
"""
""""
import sqlite3

conexao = sqlite3.connect("instance/ecovault.db")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conexao.close()
"""
"""
import sqlite3

conexao = sqlite3.connect("instance/ecovault.db")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM ecopontos")

ecopontos = cursor.fetchall()

for ecoponto in ecopontos:
    print(ecoponto)

conexao.close()
"""

import sqlite3

conexao = sqlite3.connect("instance/ecovault.db")

cursor = conexao.cursor()

cursor.execute("""
SELECT
    d.id,
    u.nome,
    e.nome,
    d.material,
    d.quantidade,
    d.pontos_gerados
FROM descartes d
INNER JOIN usuarios u
ON d.usuario_id = u.id
INNER JOIN ecopontos e
ON d.ecoponto_id = e.id
""")

dados = cursor.fetchall()

print("\n=== HISTÓRICO DE DESCARTES ===\n")

for item in dados:
    print(item)

conexao.close()