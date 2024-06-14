import time

velocidade_luz = 3e8
pi = 3.14159265358979323846

# Mensagem de Abertura
print("\nBem-vindo ao Programa de Análise de Ondas Eletromagnéticas!")
print("Desenvolvido por Isabella Vieira Silva Rosseto (RA: 22.222.036-0) e Gustavo Bertoluzzi Cardoso (RA: 22.123.016-2)\n")
print("Este programa permite calcular propriedades de ondas eletromagnéticas, como frequência, comprimento de onda,")
print("número de onda, frequência angular, campo elétrico, campo magnético e intensidade da onda.\n")


# TIPO DE ONDA - FREQUENCIA
def determinar_tipo_onda(comprimento_freq):
    tipo_onda = ""
    if(comprimento_freq < 3e-11):
        tipo_onda = "Raio Gama"
    elif(3e-11 <= comprimento_freq <= 3e-08):
        tipo_onda = "Raio-X"
    elif(4e-07 >= comprimento_freq > 3e-08):
        tipo_onda = "Ultravioleta"
    elif(7e-07 >= comprimento_freq > 4e-07):
        tipo_onda = "Luz Visível"
    elif(1e-03 >= comprimento_freq > 7e-07):
        tipo_onda = "Infravermelho"
    elif(3e-01 >= comprimento_freq > 1e-03):
        tipo_onda = "Microondas"
    elif(comprimento_freq > 3e-01):
        tipo_onda = "Rádio"
    return tipo_onda

# UNIDADE DA FREQUENCIA
def determinar_unidade(comprimento_freq, tipo_onda):
    unidade_comprimento_freq = 0
    unidade = " "
    if(tipo_onda == "Rádio"):
        unidade_comprimento_freq = comprimento_freq
        unidade = "m"
    elif(tipo_onda == "Microondas"):
        unidade_comprimento_freq = comprimento_freq * 1000
        unidade = "mm"
    elif(tipo_onda == "Infravermelho"):
        unidade_comprimento_freq = comprimento_freq * 1e+06
        unidade = "um"
    else:
        unidade_comprimento_freq = comprimento_freq * 1e+09
        unidade = "nm"
    return unidade_comprimento_freq, unidade

def calcular_frequencia(freq):
    comprimento_freq = velocidade_luz / freq
    k = 2 * pi / comprimento_freq
    w = 2 * pi * freq

    tipo_onda = determinar_tipo_onda(comprimento_freq)

    valor_unidade, unidade = determinar_unidade(comprimento_freq, tipo_onda)

    print("\n********** RESULTADOS **********")
    print(f"Comprimento da onda: {valor_unidade:.2e} {unidade}")
    print(f"Sua Frequência é de: {freq:.2e} Hz")
    print(f"Seu K (numero de ondas) é: {k:.2e} rad/m")
    print(f"Seu W (frequencia angular) é: {w:.2e} rad/s")
    print("Tipo de onda: %s" % tipo_onda)
    print("\n******************************")
    time.sleep(1)


# UNIDADE DO COMPRIMENTO
def obter_unidade_comprimento():
    while True:
        print("*** Unidades ***")
        print("[1] - Nânometro")
        print("[2] - Micrometro")
        print("[3] - Milimetro")
        print("[4] - Metro")
        print("[5] - Kilômetro")
        print("[0] - Sair")
        opcao = int(input("* Digite a opção da unidade desejada: "))
        if opcao >= 1 or opcao <= 5:
            if opcao == 1:
                comprimento = float(input("* Digite o valor do Comprimento da onda: "))
                unidade = "Nanômetros(nm)"
                comprimento /= 1e+09
                calcular_comprimento(comprimento, unidade)
                break
            elif opcao == 2:
                comprimento = float(input("* Digite o valor do Comprimento da onda: "))
                unidade = "Micrômetros(um)"
                comprimento /= 1e+06
                calcular_comprimento(comprimento, unidade)
                break
            elif opcao == 3:
                comprimento = float(input("* Digite o valor do Comprimento da onda: "))
                unidade = "Milímetro(mm)"
                comprimento /= 1000
                calcular_comprimento(comprimento, unidade)
                break
            elif opcao == 4:
                comprimento = float(input("* Digite o valor do Comprimento da onda: "))
                unidade = "Metros(m)"
                calcular_comprimento(comprimento, unidade)
                break
            elif opcao == 5:
                unidade = "Kilômetros(Km)"
                comprimento = comprimento * 1000
                calcular_comprimento(comprimento, unidade)
                break
            elif opcao == 0:
                print("Saindo...")
                time.sleep(1)
                break
        else:
            print("\n*** Opção inválida! Digite novamente os dados! ***")
            continue

# TIPO DE ONDA - COMPRIMENTO
def determinar_tipo_onda_comprimento(frequencia):
    tipo_onda = ""
    if(frequencia < 1e+09):
        tipo_onda = "Rádio"
    elif(1e+09 <= frequencia <= 3e+11):
        tipo_onda = "Microondas"
    elif(4.29e+14 >= frequencia > 3e+11):
        tipo_onda = "Infravermelho"
    elif(7.5e+14 >= frequencia > 4.29e+14):
        tipo_onda = "Luz visível"
    elif(1e+16 >= frequencia > 7.5e+14):
        tipo_onda = "Ultravioleta"
    elif(1e+19 >= frequencia > 1e+16):
        tipo_onda = "Raio-X"
    elif(frequencia > 1e+19):
        tipo_onda = "Raio Gama"
    return tipo_onda

# CALCULAR O COMPRIMENTO
def calcular_comprimento(comprimento, unidade):
    # Fórmulas do Comprimento:
    frequencia = velocidade_luz / comprimento
    k = 2 * pi / comprimento
    t = 1 / frequencia
    w = 2 * pi / t
    tipo_onda = determinar_tipo_onda_comprimento(frequencia)

    print("\n********** RESULTADOS **********")
    print("Tipo de onda: %s" % tipo_onda)
    print(f"Com seu comprimento de: {comprimento} {unidade}")
    print(f"Sua frequência é: {frequencia:0.2e} Hz")
    print(f"Seu k (numero de ondas) é: {k:0.2e} rad/m")
    print(f"Seu w (frequencia angular) é: {w:0.2e} rad/s")
    print("\n******************************")
    time.sleep(1)


# Calcular número de onda
def calcular_numero_onda(numero_onda):
    comprimento_onda = 2 * pi / numero_onda
    frequencia = velocidade_luz / comprimento_onda
    w = 2 * pi * frequencia

    print("\n********** RESULTADOS **********")
    print("Tipo de onda: ", determinar_tipo_onda(comprimento_onda))
    print(f"Sua Frequência é de: {frequencia:0.2e} Hz")
    print(f"Seu Comprimento é de: {comprimento_onda:0.2e} m")
    print(f"Seu K (numero de ondas) é: {numero_onda:0.2e} rad/m")
    print(f"Seu W (frequencia angular) é: {w:0.2e} rad/s")
    print("\n******************************")
    time.sleep(1)

def calcular_frequencia_angular(frequencia_angular):
    frequencia = frequencia_angular / (2 * pi)
    comprimento_angular = velocidade_luz / frequencia
    k = (2 * pi) / comprimento_angular
    comprimento_onda = comprimento_angular

    print("\n********** RESULTADOS **********")
    print("Tipo de onda: ", determinar_tipo_onda(comprimento_onda))
    print(f"Sua frequência é de: {frequencia:0.2e} Hz")
    print(f"Seu Comprimento é de: {comprimento_onda:0.2e} m")
    print(f"Seu K (numero de ondas) é: {k:0.2e} rad/m")
    print(f"Seu W (frequencia angular) é: {frequencia_angular:0.2e} rad/s")
    print("\n******************************")
    time.sleep(1)

# Calcular intensidade
def calcular_intensidade(entrada, valor):
    if entrada.lower() == 'em':
        cMag = valor / velocidade_luz
        intensidade = (valor * cMag) / (2 * (4 * 10**-7 * pi))
        print("\n********** RESULTADOS **********")
        print(f"Intensidade: {intensidade:.2f} W/m²")
        print(f"Campo Magnetico: {cMag:.2e} T")
        print(f"Campo Eletrico: {valor:.2e} V/m")
        print("\n******************************")
    elif entrada.lower() == 'bm':
        cEle = valor * velocidade_luz
        intensidade = (valor * cEle) / (2 * (4 * pi * 10**-7))
        print("\n********** RESULTADOS **********")
        print(f"Intensidade: {intensidade:.2f} W/m²")
        print(f"Campo Eletrico: {cEle:.2e} V/m")
        print(f"Campo Magnético: {valor:.2e} T")
        print("\n******************************")
        time.sleep(1)
    elif entrada.lower() == 'i':
        cMag = (2 * valor * (4 * pi * 10**-7)/ velocidade_luz)**0.5
        cEle = cMag * velocidade_luz
        print("\n********** RESULTADOS **********")
        print(f"Campo Elétrico: {cEle:.2e} V/m")
        print(f"Campo Magnético: {cMag:.2e} T")
        print(f"Intensidade: {valor:.2f} W/m²")
        print("\n******************************")
        time.sleep(1)
    else:
        print("Unidade inválida. Por favor, utilize 'em' para campo elétrico ou 'bm' para campo magnético.")

def menu():
    while True:
        print("\n*Escolha uma das opções:\n [c] - Entrar com comprimento de onda\n [f] - Entrar com frequência\n [w] - Entrar com frequência angular\n [k] - Entrar com número de onda\n [i] - Calcular intensidade,campo magnético ou campo elétrico\n [s] - Sair \n")
        opcao = input(">> ")

        if opcao == "f" or opcao == "F":
            frequencia = float(input("Digite o valor da Frequência da onda em Hz: "))
            calcular_frequencia(frequencia)

        elif opcao == 'c' or opcao == 'C':
            obter_unidade_comprimento()

        elif opcao == "I" or opcao == "i":
            entrada = input("Digite a entrada (I, BM ou EM): ")
            valor = float(input("Digite o valor: "))
            calcular_intensidade(entrada, valor)

        elif opcao == "k" or opcao == "K":
            numero_onda = float(input("Insira o número de onda desejado (rad/m): "))
            calcular_numero_onda(numero_onda)

        elif opcao == 'w' or opcao == 'W':
            frequencia_angular = float(input("Insira a Frequência Angular (rad/s): "))
            calcular_frequencia_angular(frequencia_angular)

        elif opcao == 's' or opcao == 'S':
            print("Encerrando...")
            time.sleep(1)
            break

menu()
