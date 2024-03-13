unidades = {"1": "T", "2": "mT", "3": "µT"}


# CONVERSOR DE METRO --> NANÔMETRO 

# Função para converter de metros para nanômetros e vice-versa
def converter_comprimento(valor, unidade_origem, unidade_destino):
    if unidade_origem.lower() == 'metros' and unidade_destino.lower() == 'nanometros':
        # 1 metro é igual a 1.000.000.000 nanômetros
        resultado = valor * 1e9
        return resultado
    elif unidade_origem.lower() == 'nanometros' and unidade_destino.lower() == 'metros':
        # 1 nanômetro é igual a 1e-9 metros
        resultado = valor * 1e-9
        return resultado
    else:
        return "Unidades de origem ou destino inválidas."

# CONVERSOR DE WATT --> JOULE 

# Função para converter de watt para joule e vice-versa
def converter_energia(valor, unidade_origem, unidade_destino):
    if unidade_origem == "W" and unidade_destino == "J":
        return valor * 1  # 1 watt é igual a 1 joule por segundo
    elif unidade_origem == "J" and unidade_destino == "W":
        return valor * 1  # 1 joule por segundo é igual a 1 watt
    else:
        return None


def conversor_magnetico(valor, opcao_origem, opcao_destino):
    fatores = {"1": 1, "2": 1e3, "3": 1e6}
    unidades = {"1": "T", "2": "mT", "3": "µT"}
    
    try:
        unidade_origem = unidades[opcao_origem]
        unidade_destino = unidades[opcao_destino]
        return valor * fatores[opcao_destino] / fatores[opcao_origem]
    except KeyError:
        return "Opções de unidade inválidas."

def conversor_frequencia(valor, unidade_origem, unidade_destino):
    fatores = {"Hz": 1, "kHz": 1e3, "MHz": 1e6}
    
    try:
        return valor * fatores[unidade_destino] / fatores[unidade_origem]
    except KeyError:
        return "Unidades de conversão não suportadas."

def exibir_menu():
    print("1. Conversor de Metros (m) e Nanômetros (nm)")
    print("2. Conversor de Watt (W) e Joule (J)")
    print("3. Conversor de Tesla (T) para miliTesla (mT) e microTesla (µT)")
    print("4. Conversor de Hertz (Hz) para KiloHertz (kHz) e MegaHertz (MHz)")

while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada (ou 's' para sair): ")

    if escolha == "s":
        break

    try:
        if escolha == "1":
            valor = float(input("Digite o valor em metros: "))
            resultado = converter_comprimento(valor, 'metros', 'nanometros')
            print(f"{valor} metros é igual a {resultado} nanômetros.\n")
            valor = float(input("Digite o valor em nanômetros: "))
            resultado = converter_comprimento(valor, 'nanometros', 'metros')
            print(f"{valor} nanômetros é igual a {resultado} metros.\n")
    
        elif escolha == "2":
            valor = float(input("Digite o valor em Watt (W): "))
            resultado = converter_energia(valor, "W", "J")
            if resultado is not None:
                print(f"{valor} W é igual a {resultado} J.\n")
            else:
                print("Conversão não suportada.\n")
            valor = float(input("Digite o valor em Joule (J): "))
            resultado = converter_energia(valor, "J", "W")
            if resultado is not None:
                print(f"{valor} J é igual a {resultado} W.\n")
            else:
                print("Conversão não suportada.\n")

        elif escolha == "3":
            opcao_origem = input("Escolha a opção de unidade de origem (1 para T, 2 para mT, 3 para µT): ")
            opcao_destino = input("Escolha a opção de unidade de destino (1 para T, 2 para mT, 3 para µT): ")
            valor = float(input(f"Digite o valor em {unidades[opcao_origem]}: "))
            resultado = conversor_magnetico(valor, opcao_origem, opcao_destino)
            print(f"{valor:.2e} {unidades[opcao_origem]} é igual a {resultado:.2e} {unidades[opcao_destino]}.\n")

        elif escolha == "4":
            unidade_origem = input("Digite a unidade de origem (Hz, kHz ou MHz): ")
            unidade_destino = input("Digite a unidade de destino (Hz, kHz ou MHz): ")
            valor = float(input(f"Digite o valor em {unidade_origem}: "))
            resultado = conversor_frequencia(valor, unidade_origem, unidade_destino)
            print(f"{valor:.2e} {unidade_origem} é igual a {resultado:.2e} {unidade_destino}.\n")

        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
