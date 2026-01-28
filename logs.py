from database import get_connection

def registrar_log(acao):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO logs (acao) VALUES (%s)",
        (acao,)
    )

    conn.commit()
    cursor.close()
    conn.close()