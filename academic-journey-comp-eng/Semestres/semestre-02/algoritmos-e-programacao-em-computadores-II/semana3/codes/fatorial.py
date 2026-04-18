def fatorial(n):
    # Caso Base: se n for 0 ou 1, o fatorial é 1
    if n <= 1:
        return 1
    # Caso Recursivo: n * fatorial do número anterior
    else:
        return n * fatorial(n - 1)

print(fatorial(5))  # Saída: 120