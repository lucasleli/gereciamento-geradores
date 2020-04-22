# NOME: Lucas dos Santos Leli RA: 1901497


class Gerador:
    def __init__(self, nome, potencia, cap_geracao, tam_tanque):
        self.__nome = nome
        self.__potencia = potencia
        self.__cap_geracao = cap_geracao
        self.__tam_tanque = tam_tanque
        self.__combustivel = 100
        self.__status = False

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, potencia):
        self.__potencia = potencia

    def get_capgeracao(self):
        return self.__cap_geracao

    def set_capgeracao(self, capacidade):
        self.__cap_geracao = capacidade

    def get_tamtanque(self):
        return self.__tam_tanque

    def set_tamtanque(self, tamanho):
        self.__tam_tanque = tamanho

    def get_combustivel(self):
        return self.__combustivel

    def abastecer(self, litros):
        combustivel_max = self.__tam_tanque - self.__combustivel
        if (litros > 0):
            if (litros <= combustivel_max):
                self.__combustivel += litros
                return f"Gerador {self.__nome} abastecido com {litros} litros."
            else:
                return "Valor ultrapassa a capacidade máxima do tanque!"
        else:
            return "O valor precisa ser maior que zero!"

    # Tipo 0 para resposta em Boolean; Tipo 1 resposta descritiva.
    def get_status(self, tipo=0):
        if (tipo == 0):
            return self.__status
        elif (tipo == 1):
            if (self.__status):
                return "Ligado"
            else:
                return "Desligado"

    def ligar(self):
        if (self.__status is False and self.__combustivel >= 50):
            self.__combustivel -= 50
            self.__status = True
            return f"Gerador {self.__nome} foi ligado com sucesso!"
        else:
            return f"O gerador {self.__nome} não tem combustível suficiente."

    def desligar(self):
        self.__status = False
        return f"O gerador {self.__nome} foi desligado com sucesso!"


g1 = Gerador('G1', 150, 12000, 700)
g2 = Gerador('G2', 85, 7000, 400)
g3 = Gerador('G3', 76, 6300, 360)
g4 = Gerador('G4', 112, 9000, 525)
geradores = [g1, g2, g3, g4]


def status_g1():
    for gerador in geradores:
        if (gerador.get_nome() == "G1"):
            return gerador.get_status()


exibir_menu = True
while(exibir_menu):
    ###############################################
    print(38 * "=")
    print("MENU PRINCIPAL")
    print("1 - Acionamento manual de gerador")
    print("2 - Status dos geradores")
    print("3 - Status dos tanques de combustível")
    print("4 - Abastecer tanque de combustível")
    print("5 - Detalhes do gerador")
    print("6 - Sair")
    print(38 * "=")
    escolha = int(input("Opção desejada: "))
    ###############################################
    if (escolha == 6):
        print("Aplicativo finalizado.")
        exibir_menu = False

    elif (escolha == 1):
        nome = input("Informe o Nome do Gerador: ")
        print(38 * "=")
        encontrados = 0
        for gerador in geradores:
            if (gerador.get_nome() == nome):
                resposta = True
                while (resposta):
                    nome = gerador.get_nome()
                    if (gerador.get_status()):
                        print(f"{nome} está Ligado. Deseja Desligar?")
                        print("1 - Sim")
                        print("2 - Não")
                        pergunta = int(input())
                        if (pergunta == 1):
                            print(gerador.desligar())
                            resposta = False
                        elif (pergunta == 2):
                            resposta = False
                        else:
                            print("Resposta inválida. Digite 1 ou 2.")
                    else:
                        print(f"{nome} está Desligado. Deseja ligar?")
                        print("1 - Sim")
                        print("2 - Não")
                        pergunta = int(input())
                        if (pergunta == 1):
                            if (nome == "G1"):
                                print(gerador.ligar())
                            elif (status_g1()):
                                print(gerador.ligar())
                            else:
                                g1 = "G1 está desligado"
                                print(f"{nome} não pode ser ligado porque", g1)
                            resposta = False
                        elif (pergunta == 2):
                            gerador.desligar()
                            resposta = False
                        else:
                            print("Resposta inválida. Digite 1 ou 2.")
                encontrados += 1
        if (encontrados == 0):
            print("Esse gerador não existe!")

    elif (escolha == 2):
        for gerador in geradores:
            nome = gerador.get_nome()
            status = gerador.get_status(1)
            print(f"{nome} - {status}")

    elif (escolha == 3):
        print("STATUS DOS TANQUES:")
        for gerador in geradores:
            nome = gerador.get_nome()
            nivel_atual = gerador.get_combustivel()
            nivel_maximo = gerador.get_tamtanque()
            alerta = ''
            if (nivel_atual < (0.2 * nivel_maximo)):
                alerta = "(ABASTECER)"

            print(f"{nome} - {nivel_atual}/{nivel_maximo} "+alerta)

    elif (escolha == 4):
        resposta = input("Nome do gerador: ")
        print(38 * "=")
        encontrados = 0
        for gerador in geradores:
            if (gerador.get_nome() == resposta):
                print(f"ABASTECIMENTO DO TANQUE {gerador.get_nome()}")
                valor_max = gerador.get_tamtanque() - gerador.get_combustivel()
                if (valor_max > 0):
                    print("Valor máximo permitido:", valor_max)
                    print("Quantos litros deseja abastecer: ")
                    print(gerador.abastecer(int(input())))
                else:
                    print(f"{gerador.get_nome()} está com o tanque cheio!")
                encontrados += 1
        if (encontrados == 0):
            print("Esse gerador não existe!")
    elif (escolha == 5):
        escolha = input("Informe o Nome do Gerador: ")
        encontrados = 0
        for gerador in geradores:
            if (gerador.get_nome() == escolha):
                cap_geracao = gerador.get_capgeracao()
                print(38 * "=")
                print("DETALHES DO GERADOR")
                print(f"Nome: {gerador.get_nome()}")
                print(f"Potência: {gerador.get_potencia()}")
                print(f"Capacidade de geração de energia: {cap_geracao}")
                print(f"Qtd de combústivel: {gerador.get_combustivel()}")
                print(f"Tamanho do tanque: {gerador.get_tamtanque()}")
                print(f"Status: {gerador.get_status(1)}")

                encontrados += 1
        if (encontrados == 0):
            print("Esse gerador não existe!")
