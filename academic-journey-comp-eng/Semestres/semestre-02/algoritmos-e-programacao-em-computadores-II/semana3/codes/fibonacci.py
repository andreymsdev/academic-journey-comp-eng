def fibonacci(n):
    # Caso Base: os dois primeiros termos são 0 e 1
    if n <= 1:
        return n
    # Caso Recursivo: soma dos dois termos anteriores
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Exemplo: O 6º termo da sequência
print(fibonacci(6))  # Saída: 8