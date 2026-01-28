from auth import cadastrar_usuario, login
from tasks import criar_tarefa, listar_tarefas, atualizar_status, excluir_tarefa

def menu_inicial():
    print("\n=== SISTEMA DE GESTÃO ===")
    print("1 - Cadastrar usuário")
    print("2 - Login")
    print("0 - Sair")
    return input("Escolha: ")

def menu_usuario(nome):
    print(f"\n=== Bem-vindo, {nome} ===")
    print("1 - Criar tarefa")
    print("2 - Listar minhas tarefas")
    print("3 - Atualizar status da tarefa")
    print("4 - Excluir tarefa")
    print("5 - Logout")
    return input("Escolha: ")

while True:
    opcao = menu_inicial()

    if opcao == "1":
        cadastrar_usuario(
            input("Nome: "),
            input("Email: "),
            input("Senha: ")
        )
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        user = login(input("Email: "), input("Senha: "))

        if not user:
            print("Login inválido")
            continue

        while True:
            opc_user = menu_usuario(user["nome"])

            if opc_user == "1":
                criar_tarefa(
                    input("Título: "),
                    input("Descrição: "),
                    user["id"]
                )
                print("Tarefa criada!")

            elif opc_user == "2":
                tarefas = listar_tarefas(user["id"])
                if not tarefas:
                    print("Nenhuma tarefa encontrada.")
                for t in tarefas:
                    print(f"{t['id']} - {t['titulo']} [{t['status']}]")

            elif opc_user == "3":
                atualizar_status(
                    input("ID da tarefa: "),
                    input("Novo status (pendente/concluida): "),
                    user["id"]
                )
                print("Status atualizado!")

            elif opc_user == "4":
                excluir_tarefa(
                    input("ID da tarefa: "),
                    user["id"]
                )
                print("Tarefa excluída!")

            elif opc_user == "5":
                print("Logout realizado.")
                break

            else:
                print("Opção inválida.")

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")