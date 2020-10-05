def prenche0(n):
    lista = []

    for i in range(n):
        lista.append(0)
    print(lista)


def de1a_n(n):
    lista= []
    for i in range(n):
        lista.append(i+1)
    print(lista)


def usuariopreenche(n):
    lista = []
    for i in range(n):
        lista.append(int(input()))
    print(lista)


def preencheinverso(n):
    lista = []
    for i in range(n):
        x = int(input())
        lista.insert(i,x)
    lista.reverse()
    print(lista)

def main():

    n = int(input())
    prenche0(n)
    de1a_n(n)
    usuariopreenche(n)
    preencheinverso(n)

if __name__=='__main__':
    main()
