from itertools import product

k, m= map(int, input().split())
lst = []
for _ in range(k):
    t = [int(i)**2 for i in input().split()]
    t.pop(0)
    if len(t) > 0:
        lst.append(set(t))

sm = [sum(x) % m for x in product(*lst)]
print(max(sm))