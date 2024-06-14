# 🌟 **Programa de Cálculo de Polarização da Luz** 🌟

Bem-vindo ao repositório do **Programa de Cálculo de Polarização da Luz**! Este projeto foi desenvolvido por Isabella Vieira Silva Rosseto, Gustavo Bertoluzzi Cardoso e Larissa Santos Fiuza.

## 📋 **Descrição**

Este programa calcula a intensidade da luz em W/cm² após passar por um ou mais polarizadores, aplicando a Lei da Metade e a Lei de Malus para simular a polarização da luz.

- **Lei da Metade**: Indica que a intensidade da luz é reduzida à metade ao passar por um polarizador.
- **Lei de Malus**: Relaciona a intensidade da luz polarizada com o ângulo do polarizador, usando a fórmula \( I = I₀ \cdot \cos²(\theta) \), onde \( \theta \) é a diferença de ângulos entre os polarizadores.

## 🚀 **Como Usar**

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/LightPolarization.git
    cd LightPolarization
    ```

2. Execute o programa:
    ```bash
    python OEM2FM.py
    ```

3. Siga as instruções no menu principal para escolher a função desejada.

## 🛠️ **Funções Principais**

### `cosseno_quadrado(angulo)`
Calcula o cosseno ao quadrado de um ângulo em graus.

### `intensidade_apos_um_polarizador(I0)`
Calcula a intensidade da luz após passar por um polarizador. A intensidade é reduzida à metade.

### `intensidade_antes_um_polarizador(I1)`
Calcula a intensidade da luz incidente com base na intensidade após um polarizador.

### `dois_polarizadores(I0, angulo1, angulo2)`
Calcula as intensidades da luz após passar por dois polarizadores.

### `tres_polarizadores(I0, angulo1, angulo2, angulo3)`
Calcula as intensidades da luz após passar por três polarizadores.

### `calcula_intensidade_incidente(I_post, angulo1, angulo2=None, angulo3=None)`
Calcula a intensidade da luz incidente a partir de intensidades medidas após 1, 2 ou 3 polarizadores.

### `fracao_luz_polarizadores(angulo1, angulo2, angulo3=None)`
Calcula a fração da luz que passa por dois ou três polarizadores com ângulos dados.

### `mostrar_informacoes()`
Exibe informações introdutórias sobre o programa.

### `menu_principal()`
Exibe um menu interativo para que o usuário escolha as opções de cálculo desejadas.

## 🌟 **Recursos Adicionais**

- **Constante Pi**: 3.1416

## 🤝 **Contribuições**

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📄 **Licença**

Este projeto está licenciado sob a [MIT License](LICENSE).

---

🌟 **Divirta-se explorando a polarização da luz!** 🌟
