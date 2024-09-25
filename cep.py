import requests


# Função para buscar endereço pelo CEP
def buscar_cep(cep):
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            dados = response.json()
            if 'erro' not in dados:
                return {
                    "cep": dados['cep'],
                    "logradouro": dados['logradouro'],
                    "bairro": dados['bairro'],
                    "cidade": dados['localidade'],
                    "estado": dados['uf']
                }
            else:
                print("CEP inválido!")
        else:
            print("Erro na consulta do CEP!")
    except Exception as e:
        print(f"Erro ao acessar API: {e}")
    return None


# Função para listar todos os registros
def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\nLista de Clientes Cadastrados:")
    for cliente in clientes:
        print(f"Código: {cliente['codigo']}, Nome: {cliente['nome']}, CPF: {cliente['cpf']}, Idade: {cliente['idade']}")
        print(
            f"Endereço: {cliente['endereco']['logradouro']}, {cliente['endereco']['numero']}, {cliente['endereco']['bairro']}, {cliente['endereco']['cidade']}, {cliente['endereco']['estado']}, CEP: {cliente['endereco']['cep']}")
        print(f"Limite de crédito: {cliente['limite_credito']}")
        print('-' * 50)


# Função para criar um novo cliente
def inserir_cliente(clientes):
    try:
        codigo = int(input("Digite o código do cliente: "))
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        idade = int(input("Digite a idade do cliente: "))

        # Consulta do CEP
        cep = input("Digite o CEP: ")
        endereco = buscar_cep(cep)
        if not endereco:
            print("Erro ao inserir endereço. Operação cancelada.")
            return

        numero = input("Digite o número do endereço: ")
        endereco['numero'] = numero

        limite_credito = float(input("Digite o limite de crédito: "))

        cliente = {
            "codigo": codigo,
            "nome": nome,
            "cpf": cpf,
            "idade": idade,
            "endereco": endereco,
            "limite_credito": limite_credito
        }
        clientes.append(cliente)
        print("Cliente inserido com sucesso!")
    except ValueError as ve:
        print(f"Erro de entrada: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Função para alterar um cliente existente
def alterar_cliente(clientes):
    try:
        codigo = int(input("Digite o código do cliente a ser alterado: "))
        cliente = next((c for c in clientes if c['codigo'] == codigo), None)

        if cliente:
            print(f"Cliente encontrado: {cliente['nome']}")
            nome = input("Digite o novo nome do cliente (deixe em branco para manter o atual): ")
            cpf = input("Digite o novo CPF do cliente (deixe em branco para manter o atual): ")
            idade = input("Digite a nova idade do cliente (deixe em branco para manter o atual): ")
            alterar_endereco = input("Deseja alterar o endereço? (1-SIM / 0-NÃO): ")

            if alterar_endereco == '1':
                cep = input("Digite o novo CEP: ")
                endereco = buscar_cep(cep)
                if endereco:
                    numero = input("Digite o novo número do endereço: ")
                    endereco['numero'] = numero
                    cliente['endereco'] = endereco
                else:
                    print("Erro ao atualizar endereço.")

            limite_credito = input("Digite o novo limite de crédito (deixe em branco para manter o atual): ")

            # Atualiza os campos se forem fornecidos novos valores
            if nome: cliente['nome'] = nome
            if cpf: cliente['cpf'] = cpf
            if idade: cliente['idade'] = int(idade) if idade.isdigit() else cliente['idade']
            if limite_credito: cliente['limite_credito'] = float(limite_credito) if limite_credito else cliente[
                'limite_credito']

            print("Cliente alterado com sucesso!")
        else:
            print("Cliente não encontrado.")
    except ValueError as ve:
        print(f"Erro de entrada: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Função para excluir um cliente
def excluir_cliente(clientes):
    try:
        codigo = int(input("Digite o código do cliente a ser excluído: "))
        cliente = next((c for c in clientes if c['codigo'] == codigo), None)

        if cliente:
            clientes.remove(cliente)
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado.")
    except ValueError as ve:
        print(f"Erro de entrada: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Função principal (main) com match-case
def main():
    clientes = []
    while True:
        print("\nMenu de Operações")
        print("1. Inserir cliente")
        print("2. Alterar cliente")
        print("3. Excluir cliente")
        print("4. Listar clientes")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                inserir_cliente(clientes)
            case '2':
                alterar_cliente(clientes)
            case '3':
                excluir_cliente(clientes)
            case '4':
                listar_clientes(clientes)
            case '0':
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
