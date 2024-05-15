import math

def cosseno_quadrado(angulo):
    """Calcula o cosseno ao quadrado de um ângulo em graus."""
    return (math.cos(math.radians(angulo))) ** 2

def intensidade_apos_um_polarizador(I0):
    """
    Calcula a intensidade da luz após passar por um polarizador.
    A intensidade é reduzida à metade, conforme a Lei da Metade.
    """
    return I0 / 2

def intensidade_antes_um_polarizador(I1):
    """
    Calcula a intensidade da luz incidente com base na intensidade após um polarizador.
    A intensidade incidente é o dobro da intensidade medida após o polarizador, revertendo a Lei da Metade.
    """
    return I1 * 2

def dois_polarizadores(I0, angulo1, angulo2):
    """
    Calcula e exibe as intensidades da luz após passar por dois polarizadores.
    Utiliza a Lei de Malus para determinar a intensidade após o segundo polarizador, baseando-se na diferença de ângulos.
    """
    I1 = intensidade_apos_um_polarizador(I0)
    I2 = I1 * cosseno_quadrado(angulo2 - angulo1)
    return I1, I2

def tres_polarizadores(I0, angulo1, angulo2, angulo3):
    """
    Calcula e exibe as intensidades da luz após passar por três polarizadores.
    Aplica a Lei de Malus sequencialmente para cada par de polarizadores.
    """
    I1 = intensidade_apos_um_polarizador(I0)
    I2 = I1 * cosseno_quadrado(angulo2 - angulo1)
    I3 = I2 * cosseno_quadrado(angulo3 - angulo2)
    return I1, I2, I3

def calcula_intensidade_incidente(I_post, angulo1, angulo2=None, angulo3=None):
    """
    Calcula a intensidade da luz incidente a partir de intensidades medidas após 1, 2 ou 3 polarizadores.
    Utiliza a Lei de Malus para reverter os efeitos dos polarizadores, ajustando pela diferença de ângulos.
    """
    if angulo2 is None:
        return intensidade_antes_um_polarizador(I_post)
    elif angulo3 is None:
        I1 = I_post / cosseno_quadrado(angulo2 - angulo1)
        return intensidade_antes_um_polarizador(I1)
    else:
        I2 = I_post / cosseno_quadrado(angulo3 - angulo2)
        I1 = I2 / cosseno_quadrado(angulo2 - angulo1)
        return intensidade_antes_um_polarizador(I1)

def fracao_luz_polarizadores(angulo1, angulo2, angulo3=None):
    """
    Calcula a fração da luz que passa por dois ou três polarizadores com ângulos dados.
    """
    I1 = 0.5
    I2 = I1 * cosseno_quadrado(angulo2 - angulo1)
    if angulo3 is None:
        return I2
    else:
        I3 = I2 * cosseno_quadrado(angulo3 - angulo2)
        return I3

def mostrar_informacoes():
    print("\nBem-vindo ao Programa de Cálculo de Polarização da Luz")
    print("Este programa calcula a intensidade da luz em W/cm² após passar por um ou mais polarizadores,")
    print("aplicando a Lei da Metade e a Lei de Malus para simular a polarização da luz.")
    print("A Lei da Metade indica que a intensidade da luz é reduzida à metade ao passar por um polarizador.")
    print("A Lei de Malus, por sua vez, relaciona a intensidade da luz polarizada com o ângulo do polarizador,")
    print("usando a fórmula I = I₀ * cos²(θ), onde θ é a diferença de ângulos entre os polarizadores.")
    print("\nDesenvolvido por:")
    print("- Isabella Vieira Silva Rosseto")
    print("- Gustavo Bertoluzzi Cardoso")
    print("- Larissa Santos Fiuza")
    print("\nUtilize o menu principal para escolher a função desejada do programa e seguir as instruções na tela.")

def menu_principal():
    mostrar_informacoes()
    while True:
        print("\nMenu Principal:")
        print("1. Calcular intensidade após polarizadores")
        print("2. Calcular intensidade incidente")
        print("3. Calcular fração de luz apenas com teta θ")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            I0 = float(input("Insira a intensidade da luz não polarizada (I0) em W/cm²: "))
            num_polarizadores = int(input("Número de polarizadores (1, 2, ou 3): "))
            angulo1 = float(input("Ângulo do primeiro polarizador (graus): "))
            if num_polarizadores == 1:
                resultado = intensidade_apos_um_polarizador(I0)
                print(f"Intensidade após um polarizador: {resultado} W/cm²")
            elif num_polarizadores == 2:
                angulo2 = float(input("Ângulo do segundo polarizador (graus): "))
                I1, I2 = dois_polarizadores(I0, angulo1, angulo2)
                print(f"Intensidade após o primeiro polarizador (I1): {I1} W/cm²")
                print(f"Intensidade após o segundo polarizador (I2): {I2} W/cm²")
            elif num_polarizadores == 3:
                angulo2 = float(input("Ângulo do segundo polarizador (graus): "))
                angulo3 = float(input("Ângulo do terceiro polarizador (graus): "))
                I1, I2, I3 = tres_polarizadores(I0, angulo1, angulo2, angulo3)
                print(f"Intensidade após o primeiro polarizador (I1): {I1} W/cm²")
                print(f"Intensidade após o segundo polarizador (I2): {I2} W/cm²")
                print(f"Intensidade após o terceiro polarizador (I3): {I3} W/cm²")

        elif escolha == '2':
            num_polarizadores = int(input("Número de polarizadores utilizados (1, 2, ou 3): "))
            I_post = float(input("Intensidade da luz medida após o último polarizador (em W/cm²): "))
            angulo1 = float(input("Ângulo do polarizador 1 (graus): "))
            if num_polarizadores == 1:
                I0 = calcula_intensidade_incidente(I_post, angulo1)
            elif num_polarizadores == 2:
                angulo2 = float(input("Ângulo do polarizador 2 (graus): "))
                I0 = calcula_intensidade_incidente(I_post, angulo1, angulo2)
            elif num_polarizadores == 3:
                angulo2 = float(input("Ângulo do polarizador 2 (graus): "))
                angulo3 = float(input("Ângulo do polarizador 3 (graus): "))
                I0 = calcula_intensidade_incidente(I_post, angulo1, angulo2, angulo3)
            print(f"Intensidade da luz incidente estimada (I0): {I0} W/cm²")

        elif escolha == '3':
            num_polarizadores = int(input("Número de polarizadores (2 ou 3): "))
            angulo1 = float(input("Ângulo do primeiro polarizador (graus): "))
            angulo2 = float(input("Ângulo do segundo polarizador (graus): "))
            if num_polarizadores == 2:
                fracao = fracao_luz_polarizadores(angulo1, angulo2)
                print(f"Fração da intensidade da luz que passa pelos dois polarizadores: {fracao:.3f}")
            elif num_polarizadores == 3:
                angulo3 = float(input("Ângulo do terceiro polarizador (graus): "))
                fracao = fracao_luz_polarizadores(angulo1, angulo2, angulo3)
                print(f"Fração da intensidade da luz que passa pelos três polarizadores: {fracao:.3f}")

        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
