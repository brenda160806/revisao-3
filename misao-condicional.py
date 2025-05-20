# Solicita o nome do agente
nome = input("Digite o nome do agente: ")

# Solicita a nota do agente
try:
    nota = float(input("Digite a nota final do agente (0 a 10): "))

    # Verifica a classificação com base na nota
    if 9.0 <= nota <= 10.0:
        classificacao = "Excelente "
    elif 7.0 <= nota <= 8.9:
        classificacao = "Bom "
    elif 5.0 <= nota <= 6.9:
        classificacao = "Regular "
    elif 3.0 <= nota <= 4.9:
        classificacao = "Ruim "
    elif 0.0 <= nota <= 2.9:
        classificacao = "Crítico "
    else:
        classificacao = "Nota inválida "

    # Exibe a mensagem final
    print(f"Agente {nome}, sua classificação é: {classificacao} (nota: {nota})")

except ValueError:
    print("Entrada inválida! A nota deve ser um número.")