print("zadanie 1")
def wyswietlListe(lista):
    for i in lista:
        print(i)
listaImion = ["adam","mirek","pawel","leszek","rafal"]
wyswietlListe(listaImion)
print("\nzadanie 2a")
def multiplaier(x):
    return x * 2
listaLiczb = [1,2,3,4,5]
for i in listaLiczb:
    print(multiplaier(i))
pomnozonaLista = [multiplaier(i) for i in listaLiczb]
print("\nzadanie 2b")
print("Pomnożona lista:", pomnozonaLista)
print("\nzadanie 3")
listaLiczb2 = list(range(10))
def wyswietlParzyste(lista):
    for i in lista:
        if i % 2 == 0:
            print(i)
wyswietlParzyste(listaLiczb2)
print("\nzadanie 4")
def wyswietlcodrugi(lista):
    for i in range(0,len(lista),2):
        print(lista[i])
wyswietlcodrugi(listaLiczb2)