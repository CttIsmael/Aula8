def recebe_numeros(n):
    lista1 = []
    mult = 1
    for i in range(n):
        lista1.append(int(input()))
        mult *=lista1[i]
        soma = sum(lista1)
    print(lista1)
    return soma, mult

def main():
    soma, mult =recebe_numeros(10)
    print(f'{soma}')
    print(f'{mult}')
    
if __name__ == '__main__':
    main()
