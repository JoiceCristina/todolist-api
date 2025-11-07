#importa a conexao criada
from conexao import get_conexao

#importa a biblioteca psycopg2
from psycopg2.extras import RealDictCursor

#importa o jason flask para retornar os dados 
from flask import jsonify

def buscar_tarefas():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
         "SELECT id, nome, descricao FROM tarefas;"
    )
       
    #buscar todos os registros na tabela
    tarefas = cursor.fetchall()

    #fecha as conexões
    cursor.close()
    conn.close()

    return jsonify(tarefas)