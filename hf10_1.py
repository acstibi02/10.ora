lista1 = []
lista2 = []
szemelyek = {}
enter = ''
def bekeres_es_eltarolas(lista1:list,lista2:list,szemelyek:dict,enter:str):
    i = 0
    while i <= 4:
        seged1 = input("Add meg az első személy nevét: ")
        seged2 = int(input("Add meg az első személy telefonszámát: "))
        seged3 = seged1,seged2
        lista2.append(seged3)
        lista1.append(seged1)
        lista1.append(seged2)
        i += 1
    i = 1
    for i in range(len(lista1)):
        if type(lista1[i]) == int and type(lista1[i-1]) == str:
            szemelyek[lista1[i-1]] = lista1[i]
    return enter
print(bekeres_es_eltarolas(lista1,lista2,szemelyek,enter))

def kiiras(lista2:list,enter:str):
    lista2.sort()
    for j in range(len(lista2)):
        k = 1
        for k in range(len(lista2[j])):
            if not k % 2:
                print(lista2[j][k], lista2[j][k + 1])
    return enter
print(kiiras(lista2,enter))

def mi_a_szamod(szemelyek:dict,enter:str):
    nev = input("Kinek a telefonszámát szeretnéd?: ")
    if nev in szemelyek:
        print(szemelyek[nev])
    else:
        print("Sajnos nincs ilyen név rögzítve.")
    return enter
print(mi_a_szamod(szemelyek,enter))