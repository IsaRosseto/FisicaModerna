import math
h1 = 6.626e-34  
c = 3e8  
m_eletron = 9.11e-31  
e = 1.602e-19  
epsilon_0 = 8.854e-12  
pi = 3.1416
velocidade = 2.187e6  
E0 = 13.6
h = 6.626e-34 

print("***** ATOMO DE BOHR E QUANTIZAÇÃO COM PYTHON *****")
print("\nIntegrantes do grupo: Gustavo Bertoluzzi Cardoso e Isabella Vieira Silva Rosseto")
print("\nEste programa estuda o modelo de Bohr para o átomo de hidrogênio. Os cálculos incluem raio da órbita, velocidade, comprimento de onda de De Broglie do elétron, energia cinética, potencial e total. Todas as entradas e saídas são tratadas com precisão de quatro algarismos significativos, e os resultados são apresentados com notação científica quando apropriado.")

def mostrar_menu():
    print("\n***** MENU *****")
    print("1. Calcular propriedades para um número quântico específico (n)")
    print("2. Calcular a diferença de energia, frequência e comprimento de onda do fóton entre dois níveis quânticos")
    print("3. Calcular n final ou inicial dado (n inicial ou n final) e (frequência ou comprimento de onda do fóton absorvido ou emitido)")
    print("4. Calcular Efóton, ffóton, e λfóton dado Efóton em [J] ou [eV], ou vice-versa")
    print("0. Sair")

def calcular_tudo_por_n(n):
    raio_orbita = (n*n) * 5.29e-11
    raio_orbita_nm = raio_orbita * 1e9
    velocidade_eletron = velocidade / n
    energia_cinetica = 13.6 / (n*n)
    energia_potencial = -27.2 / (n*n)
    energia_total = energia_cinetica * (-1)
    comprimento_onda = h1 / (m_eletron * velocidade_eletron)
    comprimento_onda_nm = comprimento_onda * 1e9
    return {
        "raio_orbita": raio_orbita,
        "raio_orbita_nm": raio_orbita_nm,
        "velocidade_eletron": velocidade_eletron,
        "energia_cinetica": energia_cinetica,
        "energia_potencial": energia_potencial,
        "energia_total": energia_total,
        "comprimento_onda": comprimento_onda,
        "comprimento_onda_nm": comprimento_onda_nm
    }

import math

h_eV_s = 4.135667696e-15 
c = 3e8  
E0 = 13.6 

def calcular_transicao():
    nivel = input("Digite qual o nível que já possui, sendo inicial [1] ou final [2]: ")
    n = int(input(f"Digite o valor para o nível {'inicial' if nivel == '1' else 'final'}: "))
    absorve_emite = input(f"O nível {'inicial' if nivel == '1' else 'final'} absorve [1] ou emite [2]?: ")
    opcao = input("Você deseja inserir a frequência [1] ou o comprimento de onda [2]? ")
    
    if opcao == "1":
        f_THz = float(input("Digite a frequência em THz: "))
        energia_foton_eV = f_THz * h_eV_s * 1e12 / e
    elif opcao == "2":
        comprimento_nm = float(input("Digite o comprimento de onda em nm: "))
        f_Hz = c / (comprimento_nm * 1e-9)
        energia_foton_eV = f_Hz * h_eV_s / e
    else:
        print("Opção inválida.")
        return

    if absorve_emite == "1":  
        energia_total_eV = -E0 / n**2 + energia_foton_eV
    else:  # Emissão
        energia_total_eV = -E0 / n**2 - energia_foton_eV

    n_final = math.sqrt(abs(-E0 / energia_total_eV))
    print(f"O nível {'final' if nivel == '1' else 'inicial'} é aproximadamente {round(n_final)}.")
       
def propriedades(n_inicial,n_final):
        
        Energia_n1 = -13.6 / n_inicial ** 2
        Energia_n2 = -13.6 / n_final ** 2
        
        Energia_abs = Energia_n2 - Energia_n1
        Energia_abs_J = Energia_abs * 1.60218e-19
        Energia_emt = Energia_n1 - Energia_n2
        Energia_emt_J = Energia_emt * 1.60218e-19
        

        comprimento_e = ((h1 * c) / Energia_emt_J)
        comprimento_e_nm = comprimento_e * 1e9

        frequencia_e = c / comprimento_e
        frequencia_e_THz = frequencia_e / 1e12

        comprimento_a = ((h1 * c) / Energia_abs_J)
        comprimento_a_nm = comprimento_a * 1e9

        frequencia_a = c / comprimento_a
        frequencia_a_THz = frequencia_a / 1e12
        
        return{
            "energia absorvida":Energia_abs,
            "energia absorvida jaules":Energia_abs_J,
            "energia emitida":Energia_emt,
            "energia emitida jaules":Energia_emt_J,
            "comprimento emitido foton":comprimento_e,
            "comprimento emitido foton nm":comprimento_e_nm,
            "frequencia emitido":frequencia_e,
            "frequencia emitido THZ":frequencia_e_THz,

            "comprimento absorvida foton":comprimento_a,
            "comprimento absorvida foton nm":comprimento_a_nm,
            "frequencia absorvida":frequencia_a,
            "frequencia absorvida THZ":frequencia_a_THz
        }

def calcular_energia_por_frequencia_lambda(ffoton=None, lambda_foton=None):
    if ffoton is not None:
        Efoton_j = h1 * ffoton
    elif lambda_foton is not None:
        ffoton = c / (lambda_foton / 1e9)
        Efoton_j = h1 * ffoton
    else:
        raise ValueError("Frequência ou comprimento de onda deve ser fornecido.")
    
    Efoton_ev = Efoton_j / e  
    return Efoton_j, Efoton_ev

def calcular_ffoton_lambdafoton_por_efoton(Efoton_j=None, Efoton_ev=None):
    if Efoton_ev is not None:
        Efoton_j = Efoton_ev * e
    elif Efoton_j is None:
        raise ValueError("Energia do fóton deve ser fornecida em Joules ou elétrons-volts.")
    
    ffoton = Efoton_j / h1
    lambda_foton = c / ffoton
    lambda_foton = lambda_foton * 1e9
    return ffoton, lambda_foton

def executar_programa():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            n = int(input("Digite o valor de n: "))
            resultados = calcular_tudo_por_n(n)
            print("\n***** RESULTADOS *****")
            print(f"[=] Raio da órbita (rn): {resultados['raio_orbita']:.3e} m")
            print(f"[=] Raio da órbita (rn): {resultados['raio_orbita_nm']:.3e} nm")
            print(f"[=] Velocidade (vn): {resultados['velocidade_eletron']:.3e} m/s")
            print(f"[=] Comprimento de onda de De Broglie (λn): {resultados['comprimento_onda']:.3e} m")
            print(f"[=] Comprimento de onda de De Broglie (λn): {resultados['comprimento_onda_nm']:.3e} nm")
            print(f"[=] Energia cinética (Kn): {resultados['energia_cinetica']:.3e} Ev")
            print(f"[=] Energia potencial (Un): {resultados['energia_potencial']:.3e} Ev")
            print(f"[=] Energia total (En): {resultados['energia_total']:.3e} J")

        elif escolha == "2":
            n_inicial = int(input("Digite o valor de n inicial: "))
            n_final = int(input("Digite o valor de n final: "))
            resultados = propriedades(n_inicial,n_final)
            print("\n***** RESULTADOS *****")
            print("\n FOTON EMITIDO")
            print(f"[=] Energia emitida do fóton: {resultados['energia emitida jaules']:.3e} J ({resultados['energia emitida']:.3e} eV)")
            print(f"[=] Frequência do fóton: {resultados['frequencia emitido']:.3e} Hz {resultados['frequencia emitido THZ']:.3e} THZ")
            print(f"[=] Comprimento de onda do fóton: {resultados['comprimento emitido foton']:.3e} m {resultados['comprimento emitido foton nm']:.3e} nm")
            print("\n FOTON ABSORVIDO")
            print(f"[=] Energia absorvida do fóton: {resultados['energia absorvida jaules']:.3e} J ({resultados['energia absorvida']:.3e} eV)")
            print(f"[=] Frequência do fóton: {resultados['frequencia absorvida']:.3e} Hz {resultados['frequencia absorvida THZ']:.3e} THZ")
            print(f"[=] Comprimento de onda do fóton: {resultados['comprimento absorvida foton']:.3e} m {resultados['comprimento absorvida foton nm']:.3e} nm")

        elif escolha == "3":
            calcular_transicao()

        elif escolha == "4":
            escolha_4 = input("Digite 'A' para calcular Efóton por ffóton ou λfóton, ou 'B' para calcular ffóton e λfóton por Efóton: ").upper()
            if escolha_4 == "A":
                ffoton = float(input("Digite o valor de ffóton (Hz), ou deixe em branco se não souber: ") or "0")
                lambda_foton = float(input("Digite o valor de λfóton (nm), ou deixe em branco se não souber: ") or "0")
                Efoton, Efoton_ev = calcular_energia_por_frequencia_lambda(ffoton or None, lambda_foton or None)
                print("\n***** RESULTADOS *****")
                print(f"\n[=] Efóton: {Efoton:.3e} J ({Efoton_ev:.3e} eV)")
            elif escolha_4 == "B":
                Efoton_j = float(input("Digite o valor de Efóton em [J], ou deixe em branco se não souber: ") or "0")
                Efoton_ev = float(input("Digite o valor de Efóton em [eV], ou deixe em branco se não souber: ") or "0")
                ffoton, lambda_foton = calcular_ffoton_lambdafoton_por_efoton(Efoton_j or None, Efoton_ev or None)
                print("\n***** RESULTADOS *****")
                print(f"\n[=] ffóton: {ffoton:.3e} Hz")
                print(f"[=] λfóton: {lambda_foton:.3e} nm")

        elif escolha == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, por favor escolha novamente.")

executar_programa()
