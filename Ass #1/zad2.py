ruller = "|"
label = "0"
dlug = int(input("Podaj długość miarki: "))

for cm in range(1, dlug + 1):
    ruller += "....|"
    label += str(cm).rjust(5)

ruller = ruller + "\n" + label

print(ruller)