s = input()
uc, lc, od, ev = [], [], [], []
le = len(s)

def process_char(c):
    if c.isdigit():
        ev.append(c) if int(c) % 2 == 0 else od.append(c)
    else:
        uc.append(c) if c.isupper() else lc.append(c)


if le == 1:
    print(s)

for i in range(le // 2):
    f, l = s[i], s[le - 1 - i]
    process_char(f)
    process_char(l)

if le % 2 == 1:
    m = s[le // 2]
    process_char(m)

k = ''.join(sorted(lc)) + ''.join(sorted(uc)) + ''.join(sorted(od)) + ''.join(sorted(ev))
print(k)