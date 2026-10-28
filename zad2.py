def multiplaier(x):
    return x * 2


listaLiczb = [1, 2, 3, 4, 5]
for i in listaLiczb:
    print(multiplaier(i))
pomnozonaLista = [multiplaier(i) for i in listaLiczb]
print("Pomnożona lista:", pomnozonaLista)
