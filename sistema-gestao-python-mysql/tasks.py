from database import get_connection
from logs import registrar_log

def criar_tarefa(titulo, descricao, usuario_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefas (titulo, descricao, usuario_id) VALUES (%s,%s,%s)",
        (titulo, descricao, usuario_id)
    )

    conn.commit()
    registrar_log("Tarefa criada")
    cursor.close()
    conn.close()

def listar_tarefas(usuario_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, titulo, status FROM tarefas WHERE usuario_id=%s",
        (usuario_id,)
    )

    tarefas = cursor.fetchall()
    cursor.close()
    conn.close()
    return tarefas

def atualizar_status(tarefa_id, status, usuario_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tarefas SET status=%s WHERE id=%s AND usuario_id=%s",
        (status, tarefa_id, usuario_id)
    )

    conn.commit()
    registrar_log("Status da tarefa atualizado")
    cursor.close()
    conn.close()

def excluir_tarefa(tarefa_id, usuario_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tarefas WHERE id=%s AND usuario_id=%s",
        (tarefa_id, usuario_id)
    )

    conn.commit()
    registrar_log("Tarefa excluída")
    cursor.close()
    conn.close()