def com_reais(n):
    reais = []
    for i in range(n):
        reais.append(float(input()))
      
    reais.reverse()    
    print(reais)


def notas_media(n):
    notas = []
    media = 0
    for i in range(n):
        notas.append(float(input()))
        media = sum(notas)/len(notas)
    print(notas)
    if n ==0:
        print("SEM NOTAS")
    else:
        print(f'{media:.1f}')


def letras(n):
    letras = []
    consoante= []
    vog = 0
    for i in range(n):
        let = input()[0]
        letras.append(let)
    for v in letras:
        if v.upper() in 'AEIOU':
            vog +=1
        elif v.upper() in 'BCDFGHJKLMNPQRSTVXYZW':
            consoante.append(v)
    print(vog)
    print(consoante)
                    
def main():
    n = int(input())
    com_reais(n)
    notas_media(n)
    letras(n)

if __name__=='__main__':
    main()
