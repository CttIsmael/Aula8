def par_impar(n):
    numero = []
    par = []
    impar = []
    for i in range(n):
        numero.append(int(input()))
    for v in numero:
        if v %2 ==0:
            par.append(v)
        else:
            impar.append(v)
    print(f'{numero}')
    print(f'{par}')
    print(f'{impar}')


def main():
    par_impar(20)

if __name__=='__main__':
    main()
