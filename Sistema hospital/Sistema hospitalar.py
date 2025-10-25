pacientes = {} #Lista dos pacientes = Global


def exibir_menu (): #Menus
    print("=== Sistema Hospitalar ===")
    print("1. Cadastrar Paciente")
    print("2. Consultar Paciente")
    print("3. Médicos Disponíveis")
    print("4. Sair")
    
    opcoes_validas = ['1', '2', '3', '4']
    while True:
        escolha = input("Selecione uma opção: ")

        if escolha == '1':
            cadastrar_paciente(pacientes)
        elif escolha == '2':
            consultar_paciente(pacientes)
        elif escolha == '3':
            listar_medicos()
        elif escolha == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


def cadastrar_paciente(db): #Cadastrar pacientes para o bd

    nome = input("Digite o nome do paciente: ")
    if nome in db:
        print(f"Cliente {nome}, já esta cadastrado.")
        return
    
    idade = input("Digite a idade do paciente: ")

    db[nome] = {
        "Nome": nome,
        "Idade": idade
    }
    print(f"Paciente {nome}, idade {idade}, cadastrado com sucesso!")


def consultar_paciente(db): #Procurar pacientes no bd
    nome = input("Digite o nome do paciente que deseja consultar: ")
    print(f"Consultando informações do paciente {nome}...")

    if nome in db:
        pacientes = db[nome]

        print(f"Nome: {nome}")
        print(f"Idade: {pacientes}")
    else:
        print("Paciente não encontrado!")


def listar_medicos():#Listar médicos
    medicos = ["Dr. Silva", "Dra. Souza", "Dr. Costa"]
    print("Médicos Disponíveis:")
    for medico in medicos:
        print(medico)


if __name__ == "__main__": #Bota o código para rodar ksksksk
    exibir_menu()