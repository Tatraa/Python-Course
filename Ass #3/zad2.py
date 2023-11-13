def odwracanie_iteracyjne(L, left, right):
    if L is None or left < 0 or right >= len(L) or left >= right:
        return

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odwracanie_iteracyjne(lista, 2, 6)
print(lista)


def odwracanie_rekurencyjne(L, left, right):
    if L is None or left < 0 or right >= len(L) or left >= right:
        return

    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjne(L, left + 1, right - 1)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odwracanie_rekurencyjne(lista, 2, 6)
print(lista)