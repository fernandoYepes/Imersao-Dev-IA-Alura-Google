def calculadora():
    while True:
        # 1. Exibição do menu de opções
        print("\n" + "=" * 25)
        print("   CALCULADORA SIMPLES   ")
        print("=" * 25)
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Sair")
        print("=" * 25)

        # 2. Leitura da opção escolhida pelo usuário
        opcao = input("Escolha uma opção (1 a 5): ")

        # Verifica se o usuário quer encerrar o programa
        if opcao == "5":
            print("\nEncerrando a calculadora. Até mais!")
            break

        # Verifica se a opção digitada é válida antes de pedir os números
        if opcao in ("1", "2", "3", "4"):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # 3. Lógica das operações matemáticas
            if opcao == "1":
                resultado = num1 + num2
                print(f"\nResultado: {num1} + {num2} = {resultado}")

            elif opcao == "2":
                resultado = num1 - num2
                print(f"\nResultado: {num1} - {num2} = {resultado}")

            elif opcao == "3":
                resultado = num1 * num2
                print(f"\nResultado: {num1} * {num2} = {resultado}")

            elif opcao == "4":
                # Tratamento de erro: divisão por zero
                if num2 == 0:
                    print("\n[Erro] Não é possível dividir nenhum número por zero!")
                else:
                    resultado = num1 / num2
                    print(f"\nResultado: {num1} / {num2} = {resultado}")

        else:
            print("\n[Aviso] Opção inválida! Digite um número de 1 a 5.")


# Ponto de entrada do script
if __name__ == "__main__":
    calculadora()