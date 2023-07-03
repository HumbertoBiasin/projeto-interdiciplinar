"""
CURSO: ADS - Análise e Desenvolvimento de Sistema
Componentes: 

PO - Robson S. Fukuda
DEVS - Gustavo Zani - 33608504
       Humberto Biasin - 33731012
       Paulo Matias de Araújo - 33608652
       Erick Madureira- 33596557
       Erick Idalino - 33749116
       Pedro Rafael - 33602930
       Mayron Vieira - 33627975

Disciplinas envolvidas: Programação de computadores e Organização e Arquitetura de Computadores

Versão do Aplicativo - 1.0
"""

while True:
    # pede ao usuário para inserir um número decimal
    decimal = int(input("\nDigite um número decimal: "))

    # permite ao usuário escolher para qual base converter o número
    print("Escolha para qual base você quer converter o número:\n")
    print("1 - Binário")
    print("2 - Octal")
    print("3 - Hexadecimal")
    print("4 - Sair")

    opcao = int(input("\nDigite a opção desejada: \n"))

    # verifica a opção escolhida pelo usuário
    if opcao == 1:
        # converte para binário e imprime o resultado
        binario = ""
        quociente = decimal

        while quociente != 0:
            resto = quociente % 2
            quociente = quociente // 2
            binario = str(resto) + binario

        print(f"\nO número {decimal} em binário é: {binario}\n")
    elif opcao == 2:
        # converte para octal e imprime o resultado
        octal = ""
        quociente = decimal

        while quociente != 0:
            resto = quociente % 8
            quociente = quociente // 8
            octal = str(resto) + octal

        print(f"\nO número {decimal} em octal é: {octal}\n")
    elif opcao == 3:
        # converte para octal e imprime o resultado
        hexadecimal = ""
        quociente = decimal

        while quociente != 0:
            resto = quociente % 16
            if resto < 10:
              hexadecimal = str(resto) + hexadecimal
            else:
              hexadecimal = chr(ord('A') + resto - 10) + hexadecimal
            quociente = quociente // 16

        print(f"\nO número {decimal} em hexadecimal é: {hexadecimal}\n")
    elif opcao == 4:
        # sai do programa
        print("Saindo do programa...")
        break
    else:
        # caso a opção escolhida não seja válida
        print("Opção inválida. Por favor, tente novamente.\n")

    # pergunta ao usuário se deseja fazer um novo cálculo
    resposta = input("\nDeseja fazer outro cálculo? (s/n) \n")

    if resposta.lower() != "s":
        # sai do loop se o usuário não quiser fazer outro cálculo
        print("\nSaindo do programa...")
        break