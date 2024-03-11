# CONVERSOR DE METRO --> NANÔMETRO 

#Função para converter de metros para nanometros e vice-versa
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

#-----------------------------------------------------------------------------------------------------------------------

# CONVERSOR DE WATT --> JOULE 

#Função para converter de watt para joule e vice-versa
def converter_energia(valor, unidade_origem, unidade_destino):
    if unidade_origem == "W" and unidade_destino == "J":
        return valor * 1  # 1 watt é igual a 1 joule por segundo
    elif unidade_origem == "J" and unidade_destino == "W":
        return valor * 1  # 1 joule por segundo é igual a 1 watt
    else:
        return None

#-----------------------------------------------------------------------------------------------------------------------

# CONVERSOR DE TESLA --> MILITESLA --> MICROTESLA 

#Função para converter de metros para nanometros e vice-versa
def conversor_magnetico(valor, unidade_origem, unidade_destino, unidade):
    if unidade_origem == "T" and unidade_destino == "mT":
        return valor * 1000
    elif unidade_origem == "T" and unidade == "µT":
        return valor * 1000000
    elif unidade_origem == "mT" and unidade_destino == "T":
        return valor / 1000
    elif unidade_origem == "mT" and unidade == "µT":
        return valor * 1000
    elif unidade_origem == "µT" and unidade_destino == "T":
        return valor / 1000000
    elif unidade_origem == "µT" and unidade == "mT":
        return valor / 1000
    else:
        return "Unidades de conversão não suportadas"

#-----------------------------------------------------------------------------------------------------------------------

def exibir_menu():
    print("1. Conversor de Metros (m) e Nanometros (nm)")
    print("2. Conversor de Watt (w) e Joule (J)")
    print("3. Conversos de Tesla (T) para miliTesla (mT) e microTesla (µT)")

while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

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
        valor = float(input("Digite o valor em Tesla (T): "))
        resultado = conversor_magnetico(valor, 'T', 'mT', 'µT')
        print(f"{valor} T é igual a {resultado} mT e {resultado} µT.\n")
        resultado = conversor_magnetico(valor, 'mT', 'T', 'µT')
        print(f"{valor} mT é igual a {resultado} T e {resultado} µT.\n")
        resultado = conversor_magnetico(valor, 'µT', 'T', 'mT')
        print(f"{valor} µT é igual a {resultado} T e {resultado} mT.\n\n")