# przykład wypisywania elementów listy i kasowania ich od razu
lista_t = ['Python', 'jest super', 'językiem programowania' ]
while lista_t:
	element = lista_t[0]
	del(lista_t[0])
	print(element,end=' ')
# efekt przykładowego wywołania
# Python jest super językiem programowania

# podobny przykład z klauzulą else
lista_t = ['Python', 'jest super', 'językiem programowania']
while lista_t:
	element = lista_t[0]
	del(lista_t[0])
	print(element, end=' ')
else:
	print('| koniec.')
	print('Tu pusta lista', lista_t)

# efekt przykładowego wywołania
# Python jest super językiem programowania | koniec.
# Tu pusta lista []


lista_ocen = []
ocena = 999
while ocena:
    ocena = int(input("Podaj liczbę całkowitą ('0' zakończy): "))
    if ocena > 0:
        lista_ocen.append(ocena)
else:
    print("Wprowadzono dane:", lista_ocen)

# efekt przykładowego wywołania
# Podaj liczbę całkowitą ('0' zakończy): 3
# Podaj liczbę całkowitą ('0' zakończy): 6
# Podaj liczbę całkowitą ('0' zakończy): 2
# Podaj liczbę całkowitą ('0' zakończy): 4
# Podaj liczbę całkowitą ('0' zakończy): 0
# Wprowadzono dane: [3, 6, 2, 4]



# teraz przykład z break
lista_ocen = []
ocena = 999
while ocena:
    ocena = int(input("Podaj liczbę całkowitą ('0' zakończy, '-1' przerwie): "))
    if ocena > 0:
        lista_ocen.append(ocena)
    if ocena == -1:
        break
else:
    print("Wprowadzono dane:", lista_ocen)

# efekt przykładowego wywołania
# Podaj liczbę całkowitą ('0' zakończy, '-1' przerwie): 4
# Podaj liczbę całkowitą ('0' zakończy, '-1' przerwie): 4
# Podaj liczbę całkowitą ('0' zakończy, '-1' przerwie): 3
# Podaj liczbę całkowitą ('0' zakończy, '-1' przerwie): -1
