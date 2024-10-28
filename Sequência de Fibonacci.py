# 1) Verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return n == b or n == 0

# Defina o número a ser verificado
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")