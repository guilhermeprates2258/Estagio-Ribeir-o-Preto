def contar_a(texto):
    texto_lower = texto.lower()
    contagem = texto_lower.count('a')
    return contagem

# Defina a string a ser verificada
texto = input("Digite uma string para verificar a ocorrência da letra 'a': ")

quantidade = contar_a(texto)
if quantidade > 0:
    print(f"A letra 'a' ocorre {quantidade} vezes na string.")
else:
    print("A letra 'a' não ocorre na string.")
