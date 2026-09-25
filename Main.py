from enum import Enum
import json
class TipoAtivo(Enum):
    NOTEBOOK_INTEL = 1
    NOTEBOOK_DEll = 2
    HD_EXTERNO = 3
    SERVIDOR = 4
try:
    with open("inventario.json", "r") as ficheiro:
        base_de_dados = json.load(ficheiro)
except FileNotFoundError:
    base_de_dados = {}
while True:
    print("\n---sistema de cadastro de ativos---")
    print("1 - Cadastrar Ativo")
    print("2 - Consultar Ativo")
    print("3 - Atualizar Ativo")
    print("4 - Remover Ativo")
    print("5 - Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            id_do_ativo = input("Digite o ID do ativo: ")
            nome_do_ativo = input("Digite o nome do ativo: ")
            tipo_do_ativo = input("Digite o tipo do ativo: ")
            responsavel_pelo_ativo = input("Digite o responsável pelo ativo: " )
            setor_do_ativo = input("Digite o setor do ativo: ")
            ficha_do_ativo = {
                "id": id_do_ativo,
                "nome": nome_do_ativo,
                "tipo": tipo_do_ativo,
                "responsavel": responsavel_pelo_ativo,
                "setor": setor_do_ativo
            }
            base_de_dados[id_do_ativo] = ficha_do_ativo
            with open("inventario.json", "w") as ficheiro:
                json.dump(base_de_dados, ficheiro, indent=4)
            print(f"---Ativo com Id {id_do_ativo} cadastrado com sucesso!---")
           
        elif opcao == 2:
            tipo_de_busca = int(input("Deseja buscar por:\n1 - ID\n2 - Nome\nEscolha: "))
            if tipo_de_busca == 1:
                id_busca = input("Qual o ID que deseja buscar? ")
                if id_busca in base_de_dados:
                    ativo = base_de_dados[id_busca]
                    print(f"Ativo encontrado:\nID: {id_busca}\nNome do ativo: {ativo['nome']} \nTipo do ativo: {ativo['tipo']}\nResponsável pelo ativo: {ativo['responsavel']}\nSetor do ativo: {ativo['setor']}")
                else:
                    print("A busca falhou. Ativo não encontrado.")   
            elif tipo_de_busca == 2:
                    nome_busca = input("Qual o nome do Ativo que deseja buscar? ")
                    encontrado = False
                    for ativo in base_de_dados.values():
                        if ativo['nome'] == nome_busca:
                            print(f"Nome do ativo: {ativo['nome']}\nID do ativo: {ativo['id']}\nTipo do ativo: {ativo['tipo']}\nResponsável pelo ativo: {ativo['responsavel']}\nSetor do ativo: {ativo['setor']}")
                            encontrado = True
                            break
                    if encontrado == False:
                        print("Ativo não encontrado na base de dados.")
            else:
                print("Ativo não encontrado na base de dados.")
        elif opcao == 3:
            id_busca = input("Digite o ID do ativo que deseja atualizar: ")
            if id_busca in base_de_dados:
                ativo_encontrado = base_de_dados[id_busca]
                try:
                    opcao_alterar = int(input(f"O que deseja alterar:\n1 - nome\n2 - tipo\n3 - responsavel\n4 - setor"))
                    if opcao_alterar == 1:
                        novo_nome = input("Digite o novo nome, ")
                        ativo_encontrado['nome']= novo_nome
                    elif opcao_alterar == 2:
                        tipo_escolhido = int(input("Escolha o novo tipo:\n1 - SERVIDOR\n2 - NOTEBOOK\n3 - HD_EXTERNO\n4 - ROTEADOR\nEscolha: "))
                        novo_tipo = TipoAtivo(tipo_escolhido).name
                        ativo_encontrado['tipo'] = novo_tipo
                    elif opcao_alterar == 3:
                        novo_responsavel = input("Digito o novo responsavel, ")
                        ativo_encontrado['responsavel']= novo_responsavel
                    elif opcao_alterar == 4:
                        novo_setor = input("Digite o novo setor, ")
                        ativo_encontrado['setor']= novo_setor
                    else:print("Opção invalidá, escolha uma opção de 1 a 4")
                    with open("inventario.json", "w") as ficheiro:
                        json.dump(base_de_dados, ficheiro, indent=4)
                except ValueError:
                    print("Erro: Por favor, digite apenas númeors inteiros!")
            else:
                print("Ativo não encontrado na base de dados.")
        elif opcao == 4:
            try:
                id_busca = input("Digite o Id do ativo que deseja remover: ")
                if id_busca in base_de_dados:
                    confimacao = input(f"Tem certeza de que deseja excluir esse o ID {id_busca}? (S/N): ").lower()
                    if confimacao == "s":
                        del base_de_dados[id_busca]
                        print("Ativo removido com sucesso!")
                        with open("inventario.json", "w") as ficheiro:
                            json.dump(base_de_dados, ficheiro, indent=4)
                    else:        
                        print("Exclusão cancelada")
                else:        
                    print("Erro: ativo não encontrado na base de dados")
            except ValueError:        
                print("Erro: Por favor, digite apenas números inteiros para o ID!")
        elif opcao == 5:
            print("encerrando o sistema...")
            break
        else:
            print("Opção não reconhecida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
