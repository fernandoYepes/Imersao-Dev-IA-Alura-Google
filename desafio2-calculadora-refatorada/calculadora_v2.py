# Código refatorado da calculadora com testes automatizados simulando entradas do terminal

def calculadora_core(inputs):
    """
    Função adaptada para receber um iterador/lista de entradas para permitir
    a execução e validação dos testes automatizados via Code Execution.
    """
    input_iter = iter(inputs)
    def mock_input(prompt=""):
        val = next(input_iter)
        return val

    output_lines = []
    def mock_print(*args, **kwargs):
        output_lines.append(" ".join(str(a) for a in args))

    while True:
        mock_print("\n" + "=" * 25)
        mock_print("   CALCULADORA SIMPLES   ")
        mock_print("=" * 25)
        mock_print("1 - Adição (+)")
        mock_print("2 - Subtração (-)")
        mock_print("3 - Multiplicação (*)")
        mock_print("4 - Divisão (/)")
        mock_print("5 - Porcentagem (%)")
        mock_print("6 - Sair")
        mock_print("=" * 25)

        opcao = mock_input("Escolha uma opção (1 a 6): ")

        if opcao == "6":
            mock_print("\nEncerrando a calculadora. Até mais!")
            break

        if opcao in ("1", "2", "3", "4", "5"):
            num1 = float(mock_input("Digite o primeiro número: "))
            num2 = float(mock_input("Digite o segundo número: "))

            if opcao == "1":
                resultado = num1 + num2
                mock_print(f"\nResultado: {num1} + {num2} = {resultado}")
            elif opcao == "2":
                resultado = num1 - num2
                mock_print(f"\nResultado: {num1} - {num2} = {resultado}")
            elif opcao == "3":
                resultado = num1 * num2
                mock_print(f"\nResultado: {num1} * {num2} = {resultado}")
            elif opcao == "4":
                if num2 == 0:
                    mock_print("\n[Erro] Não é possível dividir nenhum número por zero!")
                else:
                    resultado = num1 / num2
                    mock_print(f"\nResultado: {num1} / {num2} = {resultado}")
            elif opcao == "5":
                # Lógica: num2% de num1 (ex: 20% de 200 = 40.0)
                resultado = (num1 * num2) / 100
                mock_print(f"\nResultado: {num2}% de {num1} = {resultado}")
        else:
            mock_print("\n[Aviso] Opção inválida! Digite um número de 1 a 6.")

    return "\n".join(output_lines)

# 1. Teste da nova feature: Porcentagem (25% de 200 = 50.0)
teste_porcentagem_input = ["5", "200", "25", "6"]
saida_porcentagem = calculadora_core(teste_porcentagem_input)

# 2. Teste de regressão: Adição (10 + 15 = 25.0) e Divisão por zero
teste_regressao_input = ["1", "10", "15", "4", "50", "0", "6"]
saida_regressao = calculadora_core(teste_regressao_input)

print("--- [TESTE FEATURE: PORCENTAGEM] ---")
print(saida_porcentagem)

print("\n--- [TESTE REGRESSÃO: ADIÇÃO E DIVISÃO POR ZERO] ---")
print(saida_regressao)