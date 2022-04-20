class Shop:  # Funções básicas da loja (todos os clientes e todos os produtos)
    def __init__(self):
        self.client = client  # self.client recebe a variavel dicionario onde fica armazenado os clientes
        self.product = product  # self.product recebe a variavel dicionario onde fica armazenado os produtos
        # Estrutura de um dicionario = {chave:valor} -> No cliente está {cpf:{"Nome":"Nome_Qualquer"},{"Email":"email@email"},{"Senha":123546},{Credito:1000}}
        # Cada chave do dicionario me retorna um valor. Um dicionario não pode ter duas chaves iguais, por isso criei a lista de clientes e produtos com dicionarios.
        # Porque codigo de produtos e cpf não podem se repetir.
        # Se eu acessar o CPF do dicionario vai me retornar todos os dados daquele cliente (vai me retornar outro dicionario). Caso eu queira algo especifico, vou ter que chamar o dicionario -> cpf e o que eu quero
        # Exemplo quero o email dicionario->cpf->email = client[123.567.789-00]["Email"] e assim vai...

    def all_clients(self):  # Exibir todos os clientes
        if not (len(self.client)):  # Verifica se tem algo no dicionario
            print("--------| Nenhum Cliente Cadastrado |--------")
        else:
            for i in self.client:  # Para todos i(Cpf) dentro do self.client:

                print("----------------------------------")
                print("Nome:", self.client[i]["Nome"])  # Dicionario[Cpf][Nome] me retorna o nome
                print("CPF:", i)  # I é meu cpf
                print("Email:", self.client[i]["Email"])  # Dicionario[Cpf][Email] me retorna o email
                print("Senha:", self.client[i]["Senha"])  # Dicionario[Cpf][Senha] me retorna o Senha
                print("Credito:", self.client[i]["Credito"])  # Dicionario[Cpf][Credito] me retorna o credito
                print("----------------------------------")

    def todos_produtos(self):  # Exibir todos os produtos
        for i in self.product:
            #  :<12 (12 é o numero máximo de caracteres) serve para justificar o texto à esquerda
            print(f"Cod:{i}\t\t{self.product[i]['Nome_Produto']:<12} R${self.product[i]['Preço']:.2f} ")  # :


class CheckCredentials:
    @staticmethod  # Metodo estatico, é como funções normais mas organizadas dentro de classes (Fica mais organizado)
    def cpf_ok():
        while True:
            try:
                cpf_original = input("CPF:")
                cpf = cpf_original.replace(".", "").replace("-", "")  # Pega e tira os . e - do CPF
                soma_a = 0

                for i in range(9):
                    soma_a += int(cpf[i]) * (10 - i)  # Faz a primeira conta do digito verificador
                if (soma_a % 11) < 2:
                    soma_a = 0
                else:
                    soma_a = 11 - soma_a % 11
                cpf_valido = cpf.replace(cpf[9], str(soma_a))
                soma_b = 0

                for x in range(10):
                    soma_b += int(cpf_valido[x]) * (11 - x)  # Faz a segunda conta do digito verficiador
                if (soma_b % 11) < 2:
                    soma_b = 0
                else:
                    soma_b = 11 - soma_b % 11

                cpf_valido = cpf_valido.replace(cpf_valido[-1], str(soma_b))
                if cpf != cpf_valido:  # Verifica se o cpf digitado é válido
                    print("CPF Inválido!")
                    continue
                else:
                    return cpf_original
            except (ValueError,
                    IndexError):  # tratamento de erro quando for  digitado CPF errado
                print("CPF Inválido!")
                continue

    @staticmethod
    def nome_ok():
        while True:
            nome = input("Nome:")
            if not (nome.isalpha()):  # Procura se na string só tem letras
                print("Somente Letras!")
                continue
            else:
                return nome

    @staticmethod
    def senha_ok():
        while True:
            senha = input("Senha:")
            if len(senha) != 6:  # Senha definida como tamanho 6
                print("Apenas uma senha de 6 digitos é válido!")
                continue
            else:
                return senha

    @staticmethod
    def email_ok():
        while True:
            email = input("Email:")
            if email.find("@") and email.find(
                    "@") != -1:  # Procura o "@" dentro da string email. O find quando dá False retorna -1.
                return email
            else:
                print("Email inválido!")
                continue


class CreateAccount:
    def __init__(self):
        print("-> Cadastro <-")
        cpf = CheckCredentials.cpf_ok()
        for i in client:
            if i == cpf:  # Verifica se CPF já está cadastrado
                print("Esse CPF já está Cadastrado!")
                break
        else:
            email = CheckCredentials.email_ok()
            for x in client:
                if client[x]["Email"] == email:  # Verifica se email já está cadastrado
                    print("Esse email está em uso")
                    break

            else:

                client[cpf] = {"Email": email,
                               "Senha": CheckCredentials.senha_ok(),  # Pede a senha com verificação
                               "Nome": CheckCredentials.nome_ok(),  # Pede nome com verificação
                               "Credito": 1000}


class Login:
    def __init__(self):
        print("-> Login <-")
        self.login_bem_sucedido = False
        self.cpf = None
        try:
            if not len(client):  # Procura se tem alguem cadastrado
                print("--------| Nenhum Cliente Cadastrado |--------")
            else:
                login_cpf = CheckCredentials.cpf_ok()
                for i in client:
                    if login_cpf == i:  # Procura o cpf no banco de dados (client)

                        print("|CPF Encontrado|")
                        login_email = CheckCredentials.email_ok()
                        if login_email == client[i]["Email"]:  # Procura o Email no banco de dados (client)
                            login_senha = CheckCredentials.senha_ok()
                            if login_senha == client[i]["Senha"]:  # Verifica a senha da conta no banco de dados
                                print("|Logado com Sucesso|")
                                self.login_bem_sucedido = True
                                self.cpf = i
                                break
                            else:
                                print("Senha Incorreta!")
                                break
                        else:
                            print("Email Incorreto!")
                            break
                else:
                    print("CPF não encontrado")

        except ValueError:
            print("Usuário não encontrado!")


class Buy(Login):
    def __init__(self):
        super().__init__()  # Herda os  'self' do login
        if self.login_bem_sucedido:
            print("Estou logado")
            carrinho_cliente = []
            quanto_gastou = 0  # Quanto gastou na compra
            while True:

                print(
                    "(1) ao (20) = Comprar\n'carrinho' = Ver o Carrinho\n'produtos' = Todos os Produtos\n'sair' = Sair da Loja")
                opcao = input(":")
                if opcao.lower() == "sair":  # opcao.lower transforma tudo em minusculo, caso seja escrito em maiusculo.
                    print("Saindo da Loja...")
                    break
                elif opcao.lower() == "carrinho":
                    print("-------------------------")
                    print("Seu carrinho de compras...\n")
                    for x in carrinho_cliente:
                        print(x)
                    print("-------------------------")
                    print(f"Total da compra R${quanto_gastou}")
                    print(f"Saldo Restante:R${client[self.cpf]['Credito']}")
                    print("-------------------------")
                elif opcao.lower() == "produtos":
                    Shop().todos_produtos()
                    print("-------------------------")
                else:
                    try:
                        if client[self.cpf]["Credito"] - product[opcao]["Preço"] >= 0:  # Verifica se pode comprar
                            carrinho_cliente.append(
                                str(f"Cod:{opcao}\tP:{product[opcao]['Nome_Produto']:<12} \tR${product[opcao]['Preço']:}"))  # Cria uma string e joga na lista "carrinho_cliente"
                            client[self.cpf]["Credito"] -= product[opcao]["Preço"]  # Desconta da conta
                            quanto_gastou += product[opcao]["Preço"]  # Soma quanto gastou
                        else:
                            print("Saldo insuficiente...!")
                    except KeyError:
                        print(
                            "Ops...Essa opção não existe no sistema!")  # Quando é digitado uma OPCAO que não existe
        else:
            print("Usuário não logado!")


class Pay(Login):
    def __init__(self):
        super().__init__()  # Herda os 'self' do Login
        print("-> Pagar a divida <-")
        try:
            divida = abs(client[self.cpf]["Credito"] - 1000)  # Faz conta para ver quanto é a divida
            divida_paga = str(client[self.cpf]["Credito"] + divida)  # Soma para o credito ficar 1000 novamente
            print(f"Seu Saldo: R${client[self.cpf]['Credito']}\nSua Divida: R${divida}")
            client[self.cpf]["Credito"] = divida_paga  # Atualiza o credito
            if divida == 0:  # Verifica se não está devendo nada
                print("Você não está devendo nada!")
            else:
                print("$$$$$$$$$$$ Divida Paga $$$$$$$$$$$")
                print(f"Seu Saldo Agora é R${client[self.cpf]['Credito']}")
        except KeyError:
            print("Erro no Login...!")  # Quando não tem nenhum cliente cadastrado.


class SalvarAutomatico:  # Salva e importa os contatos automaticamente, sem perder nenhum dado de um cliente
    @staticmethod  # Metodos estáticos pois não tem nenhuma necessidade de declarar o 'self'
    def salvar():
        with open("clientes.txt", "w") as salvar_clientes:  # Criou um arquivo chamado "clientes.txt" no modo writer
            for i in client:
                salvar_clientes.write(i + ",")  # CPF
                salvar_clientes.write(client[i]["Email"] + ",")  # Email
                salvar_clientes.write(client[i]["Senha"] + ",")  # Senha
                salvar_clientes.write(client[i]["Nome"] + ",")  # Nome
                salvar_clientes.write(str(client[i]["Credito"]) + "\n")  # Credito
                # O For está na mesma ordem do cadastro
                # A escrita em arquivos acontece tudo na mesma linha, por isso tive que colocar um \n

    @staticmethod
    def importar():
        with open("clientes.txt", "r") as importar_clientes:
            clientes = importar_clientes.read().splitlines()  # Separa por linhas (\n) cada cliente em listas
            for i in clientes:
                var = i.split(
                    ",")  # Separa cada informação do cliente separados por virgula e transforma em indices da lista
                client[var[0]] = dict(Email=var[1], Senha=var[2], Nome=var[3],
                                      Credito=int(var[4]))  # Mesma Ordem do Cadastro


client = {}  # Esta organizado assim: {cpf:{"Email":email@email,"Senha":123546,"Nome":Fulano}
product = {"1": {"Nome_Produto": "Acabate", "Preço": 1}, "2": {"Nome_Produto": "Beterraba", "Preço": 2},
           "3": {"Nome_Produto": "Cebola", "Preço": 3}, "4": {"Nome_Produto": "Dado", "Preço": 4},
           "5": {"Nome_Produto": "Elefante", "Preço": 5}, "6": {"Nome_Produto": "Fogo", "Preço": 6},
           "7": {"Nome_Produto": "Gasolina", "Preço": 7}, "8": {"Nome_Produto": "Helicoptero", "Preço": 8},
           "9": {"Nome_Produto": "Isqueiro", "Preço": 9}, "10": {"Nome_Produto": "Jacaré", "Preço": 10},
           "11": {"Nome_Produto": "Kiwi", "Preço": 11}, "12": {"Nome_Produto": "Laranja", "Preço": 12},
           "13": {"Nome_Produto": "Maracuja", "Preço": 13}, "14": {"Nome_Produto": "Navio", "Preço": 14},
           "15": {"Nome_Produto": "Ovo", "Preço": 15}, "16": {"Nome_Produto": "Prato", "Preço": 16},
           "17": {"Nome_Produto": "Queijo", "Preço": 17}, "18": {"Nome_Produto": "Rato", "Preço": 18},
           "19": {"Nome_Produto": "Sapato", "Preço": 19}, "20": {"Nome_Produto": "Tenis", "Preço": 1000}}
#  Fica mais organizado desse jeito. Para cada codigo (1 ao 20) eu tenho nome do produto e o preço. Basta acessar:
#  Exemplo product["1"] = me retorna {"Nome_Produto": "Acabate", "Preço": 1}. product["1"]["Nome_Produto"] me retorna Abacate.
#  product["1"]["Preço"] me retorna 1 (o preço dele).


#  Verifica se esse módulo é o __main__. Normalmente é usado quando são feito scripts.
#  É interessante usar por exemplo quando tu quer utilizar algumas funções do programar, usando o import em outro projeto, sem executar o programa.
if __name__ == "__main__":
    while True:
        SalvarAutomatico().importar()
        print("(1)Comprar\n(2)Cadastrar\n(3)Pagar Divida\n(4)Todos os Produtos\n(5)Todos os Clientes\n(99)Sair")
        opcao_sistema = input(":")
        if opcao_sistema == "1":
            Buy()
        elif opcao_sistema == "2":
            CreateAccount()
        elif opcao_sistema == "3":
            Pay()
        elif opcao_sistema == "4":
            Shop().todos_produtos()
        elif opcao_sistema == "5":
            Shop().all_clients()
        elif opcao_sistema == "99":
            break
        else:
            print("Opção não encontrada no sistema!")
        print("--------------------------")
        SalvarAutomatico().salvar()
