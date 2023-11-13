def dodaj_element(zagniezdzona_struktura, wartosc):
    if isinstance(zagniezdzona_struktura, list):
        for i, element in enumerate(zagniezdzona_struktura):
            if isinstance(element, (list, tuple, dict)):
                dodaj_element(element, wartosc)
            elif i == len(zagniezdzona_struktura) - 1:
                # Dodawanie wartości do najbardziej zagnieżdżonej listy
                zagniezdzona_struktura.append(wartosc)
    elif isinstance(zagniezdzona_struktura, tuple):
        nowa_lista = list(zagniezdzona_struktura)
        dodaj_element(nowa_lista, wartosc)
        zagniezdzona_struktura = tuple(nowa_lista)
    elif isinstance(zagniezdzona_struktura, dict):
        for klucz, wart in zagniezdzona_struktura.items():
            dodaj_element(wart, wartosc)
    else:
        # Obsługa innych typów danych (np. int, str, itp.) - można dostosować według potrzeb
        pass

# Przykłady użycia:
lista1 = [1, [2, 3], 4]
dodaj_element(lista1, 5)
print(lista1)  # Powinno wydrukować [1, [2, 3, 5], 4]

lista2 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
dodaj_element(lista2, 9)
print(lista2)  # Powinno wydrukować [3, 4, [2, [1, 2, [7, 8, 9], 3, 4], 3, 4], 5,
