def primeiro(lista):
    return lista[0]

def segundo(lista):
    return lista[1]

def terceiro(lista):
    return lista[2]

def quarto(lista):
    return lista[3]

def ultimo(lista):
    return lista[-1]

nome = ["Alan", "Michael", "da", "Conceição", "Rodrigues", "Miranda"]

print("Digite um número de 1 a 5, logo abaixo:")
print()
numero = int(input("Número: "))

if numero == 1:
    print(primeiro(nome))
    
elif numero == 2:
    print(segundo(nome))
    
elif numero == 3:
    print(terceiro(nome))
    
elif numero == 4:
    print(quarto(nome))
    
elif numero == 5:
    print(ultimo(nome))
    
else:
    print("Númmero Inválido.")
