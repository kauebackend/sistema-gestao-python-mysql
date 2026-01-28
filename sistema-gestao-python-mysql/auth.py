import hashlib
from database import get_connection
from logs import registrar_log

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar_usuario(nome, email, senha):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha) VALUES (%s,%s,%s)",
        (nome, email, hash_senha(senha))
    )

    conn.commit()
    registrar_log("Usuário cadastrado")
    cursor.close()
    conn.close()

def login(email, senha):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM usuarios WHERE email=%s AND senha=%s",
        (email, hash_senha(senha))
    )

    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user