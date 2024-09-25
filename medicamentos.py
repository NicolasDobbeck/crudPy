# Função para listar todos os medicamentos
def listar_medicamentos(medicamentos):
    if not medicamentos:
        print("Nenhum medicamento cadastrado.")
        return
    print("\nLista de Medicamentos Cadastrados:")
    for medicamento in medicamentos:
        print(f"Código: {medicamento['codigo']}")
        print(f"Nome do Medicamento: {medicamento['nome']}")
        print(f"Nome Genérico: {medicamento['generico']}")
        print(f"Prescrição: {medicamento['prescricao']}")
        print(f"Data de Fabricação: {medicamento['fabricacao']}")
        print(f"Data de Validade: {medicamento['validade']}")
        print(f"Valor de Compra: R$ {medicamento['valor_compra']:.2f}")
        print('-' * 50)


# Função para inserir um novo medicamento
def inserir_medicamento(medicamentos):
    try:
        codigo = int(input("Digite o código do medicamento: "))
        nome = input("Digite o nome do medicamento: ")
        generico = input("Digite o nome genérico do medicamento: ")
        prescricao = input("Digite a prescrição do medicamento: ")
        fabricacao = input("Digite a data de fabricação (formato DD/MM/AAAA): ")
        validade = input("Digite a data de validade (formato DD/MM/AAAA): ")
        valor_compra = float(input("Digite o valor de compra do medicamento: "))

        medicamento = {
            "codigo": codigo,
            "nome": nome,
            "generico": generico,
            "prescricao": prescricao,
            "fabricacao": fabricacao,
            "validade": validade,
            "valor_compra": valor_compra
        }
        medicamentos.append(medicamento)
        print("Medicamento inserido com sucesso!")
    except ValueError as ve:
        print(f"Erro de entrada: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Função para alterar um medicamento existente
def alterar_medicamento(medicamentos):
    try:
        codigo = int(input("Digite o código do medicamento a ser alterado: "))
        medicamento = next((m for m in medicamentos if m['codigo'] == codigo), None)

        if medicamento:
            print(f"Medicamento encontrado: {medicamento['nome']}")
            nome = input("Digite o novo nome do medicamento (deixe em branco para manter o atual): ")
            generico = input("Digite o novo nome genérico (deixe em branco para manter o atual): ")
            prescricao = input("Digite a nova prescrição (deixe em branco para manter o atual): ")
            fabricacao = input("Digite a nova data de fabricação (deixe em branco para manter o atual): ")
            validade = input("Digite a nova data de validade (deixe em branco para manter o atual): ")
            valor_compra = input("Digite o novo valor de compra (deixe em branco para manter o atual): ")

            # Atualiza os campos se forem fornecidos novos valores
            if nome: medicamento['nome'] = nome
            if generico: medicamento['generico'] = generico
            if prescricao: medicamento['prescricao'] = prescricao
            if fabricacao: medicamento['fabricacao'] = fabricacao
            if validade: medicamento['validade'] = validade
            if valor_compra: medicamento['valor_compra'] = float(valor_compra)

            print("Medicamento alterado com sucesso!")
        else:
            print("Medicamento não encontrado.")
    except ValueError as ve:
        print(f"Erro de entrada: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Função para excluir um medicamento
def excluir_medicamento(medicamentos):
    try:
        codigo = int(input("Digite o código do medicamento a ser excluído: "))
        medicamento = next((m for m in medicamentos if m['codigo'] == codigo), None)

        if medicamento:
            medicamentos.remove(medicamento)
            print("Medicamento excluído com sucesso!")
        else:
            print("Medicamento não encontrado.")
    except ValueError as ve:
        print(f"Erro de entrada: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Função principal (main) com controle de execução
def main():
    medicamentos = []
    while True:
        print("\nMenu de Operações")
        print("1. Inserir medicamento")
        print("2. Alterar medicamento")
        print("3. Excluir medicamento")
        print("4. Listar medicamentos")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_medicamento(medicamentos)
        elif opcao == '2':
            alterar_medicamento(medicamentos)
        elif opcao == '3':
            excluir_medicamento(medicamentos)
        elif opcao == '4':
            listar_medicamentos(medicamentos)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
