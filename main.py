# Recebe a string como entrada
string = input("Digite uma string: ")

# Inicializa uma variável vazia para armazenar a string invertida
string_invertida = ""

# Intera através da string a partir do último caractere até o primeiro, adicionando cada caractere à string invertida
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

# Imprime a string invertida
print("A string invertida é:", string_invertida)
