lista = [1, 2, 3, 4, 2, 1, 3, 4, 3]
rimuovere = []
for i in range(len(lista)):
    if lista[i] == 3:
        rimuovere.append(i)

for i in range(len(rimuovere)):
    lista.pop(rimuovere[i])

print(lista)