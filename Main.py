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
    print("5 - Cadastrar vulnerabilidade")
    print("6 - Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            id_do_ativo = input("Digite o ID do ativo (apenas números): ")
            while not id_do_ativo.isdigit():
                id_do_ativo = input("Entrada inválida. Digite o ID do ativo (apenas números): ")
            nome_do_ativo = input("Digite o nome do ativo: ")
            while nome_do_ativo.strip() == "":  # corrigido: .strip() rejeita nome só com espaço
                nome_do_ativo = input("Nome não pode ser vazio. Digite o nome do ativo: ")
            tipo_input = input("Digite o tipo do ativo:\n1 - NOTEBOOK_INTEL\n2 - NOTEBOOK_DEll\n3 - HD_EXTERNO\n4 - SERVIDOR\nEscolha: ")
            while not tipo_input.isdigit() or int(tipo_input) not in [1, 2, 3, 4]:  # corrigido: valida antes de converter, evita crash com entrada em branco/invalida
                tipo_input = input("Tipo inválido. Digite o tipo do ativo:\n1 - NOTEBOOK_INTEL\n2 - NOTEBOOK_DEll\n3 - HD_EXTERNO\n4 - SERVIDOR\nEscolha: ")
            tipo_do_ativo = int(tipo_input)
            responsavel_pelo_ativo = input("Digite o responsável pelo ativo: " )
            while responsavel_pelo_ativo.strip() == "":  # corrigido: .strip() rejeita responsavel só com espaço
                responsavel_pelo_ativo = input("Responsável não pode ser vazio. Digite o responsável pelo ativo: ") 
            setor_do_ativo = input("Digite o setor do ativo: ")
            while setor_do_ativo.strip() == "":  # corrigido: .strip() rejeita setor só com espaço
                setor_do_ativo = input("Setor não pode ser vazio. Digite o setor do ativo: ")
            ficha_do_ativo = {
                "id": id_do_ativo,
                "nome": nome_do_ativo,
                "tipo": tipo_do_ativo,
                "responsavel": responsavel_pelo_ativo,
                "setor": setor_do_ativo,
                "vulnerabilidade": []
            }
            base_de_dados[id_do_ativo] = ficha_do_ativo
            with open("inventario.json", "w") as ficheiro:
                json.dump(base_de_dados, ficheiro, indent=4)
            print(f"---Ativo com Id {id_do_ativo} cadastrado com sucesso!---")
           
        elif opcao == 2:
            ativo_encontrado = None
            tipo_de_busca = int(input("Deseja buscar por:\n1 - ID\n2 - Nome\nEscolha: "))
            if tipo_de_busca == 1:
                id_busca = input("Qual o ID que deseja buscar? ")
                if id_busca in base_de_dados:
                    ativo_encontrado = base_de_dados[id_busca]
                else:
                    print("A busca falhou. Ativo não encontrado.")   
            elif tipo_de_busca == 2:
                    nome_busca = input("Qual o nome do Ativo que deseja buscar? ")
                    for ativo in base_de_dados.values():
                        if ativo['nome'] == nome_busca:
                            ativo_encontrado = ativo
                            break
                    if ativo_encontrado is None:
                        print("Ativo não encontrado na base de dados.")
            else:
                print("Opção de busca inválida.")
            if ativo_encontrado is not None:
                print(f"ID: {ativo_encontrado['id']}")
                print(f"Nome: {ativo_encontrado['nome']}")
                print(f"Tipo: {TipoAtivo(ativo_encontrado['tipo']).name}")
                print(f"Responsável: {ativo_encontrado['responsavel']}")
                print(f"Setor: {ativo_encontrado['setor']}")
                if ativo_encontrado['vulnerabilidade']:
                    print("Vulnerabilidades:")
                    for vulnerabilidade in ativo_encontrado['vulnerabilidade']:
                        print(f"- Descrição: {vulnerabilidade['descricao']}, Categoria: {vulnerabilidade['categoria']}, Severidade: {vulnerabilidade['severidade']}, Status: {vulnerabilidade['status']}")
                else:
                    print("Nenhuma vulnerabilidade cadastrada para este ativo.")            
        elif opcao == 3:
            id_busca = input("Digite o ID do ativo que deseja atualizar: ")
            if id_busca in base_de_dados:
                ativo_encontrado = base_de_dados[id_busca]
                try:
                    opcao_alterar = int(input(f"O que deseja alterar:\n1 - nome\n2 - tipo\n3 - responsavel\n4 - setor\nEscolha: "))
                    if opcao_alterar == 1:
                        novo_nome = input("Digite o novo nome: ")
                        while novo_nome.strip() == "":
                            novo_nome = input("Nome não pode ser vazio. Digite o novo nome: ")
                        ativo_encontrado['nome']= novo_nome
                    elif opcao_alterar == 2:
                        tipo_input = input("Digite o novo tipo do ativo:\n1 - NOTEBOOK_INTEL\n2 - NOTEBOOK_DEll\n3 - HD_EXTERNO\n4 - SERVIDOR\nEscolha: ")
                        while not tipo_input.isdigit() or int(tipo_input) not in [1, 2, 3, 4]:
                            tipo_input = input("Tipo inválido. Digite o novo tipo do ativo:\n1 - NOTEBOOK_INTEL\n2 - NOTEBOOK_DEll\n3 - HD_EXTERNO\n4 - SERVIDOR\nEscolha: ")
                        ativo_encontrado['tipo'] = int(tipo_input)
                    elif opcao_alterar == 3:
                        novo_responsavel = input("Digite o novo responsável: ")
                        while novo_responsavel.strip() == "":
                            novo_responsavel = input("Responsável não pode ser vazio. Digite o novo responsável: ")
                        ativo_encontrado['responsavel']= novo_responsavel
                    elif opcao_alterar == 4:
                        novo_setor = input("Digite o novo setor: ")
                        while novo_setor.strip() == "":
                            novo_setor = input("Setor não pode ser vazio. Digite o novo setor: ")
                        ativo_encontrado['setor']= novo_setor
                    else:print("Opção invalidá, escolha uma opção de 1 a 4")
                    with open("inventario.json", "w") as ficheiro:
                        json.dump(base_de_dados, ficheiro, indent=4)
                except ValueError:
                    print("Erro: Por favor, digite apenas números inteiros!")
            else:
                print("Ativo não encontrado na base de dados.")
        elif opcao == 4:
            try:
                id_busca = input("Digite o Id do ativo que deseja remover: ")
                while not id_busca.isdigit():
                    id_busca = input("Erro: Por favor, digite apenas números inteiros para o ID: ")
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
            id_busca = input("Digite o ID do ativo que deseja cadastrar a vulnerabilidade: ")
            if id_busca in base_de_dados:
                descricao_vuln = input("Descrição da vulnerabilidade: ")
                while descricao_vuln.strip() == "":
                    descricao_vuln = input("Descrição não pode ser vazia. Digite a descrição da vulnerabilidade: ")
                categoria_vuln = input("Categoria: ")
                while categoria_vuln.strip() == "":
                    categoria_vuln = input("Categoria não pode ser vazia. Digite a categoria: ")    
                severidade_vuln = input("Severidade (Baixa/Média/Alta/Crítica): ")
                while severidade_vuln not in ["Baixa", "Média", "Alta", "Crítica"]:
                    severidade_vuln = input("Severidade inválida. Digite a severidade (Baixa/Média/Alta/Crítica): ")    
                status_vuln = input("Status (Aberta/Em tratamento/Corrigida): ")
                while status_vuln not in ["Aberta", "Em tratamento", "Corrigida"]:
                    status_vuln = input("Status inválido. Digite o status (Aberta/Em tratamento/Corrigida): ")
                nova_vulnerabilidade = {
                    "descricao": descricao_vuln,
                    "categoria": categoria_vuln,
                    "severidade": severidade_vuln,
                    "status": status_vuln
                }
                base_de_dados[id_busca]["vulnerabilidade"].append(nova_vulnerabilidade)
                with open("inventario.json", "w") as ficheiro:
                    json.dump(base_de_dados, ficheiro, indent=4)
                    print("Vulnerabilidade cadastrada com sucesso!")
            else:
                print("Ativo não encontrado na base de dados.")
        elif opcao == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção não reconhecida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")