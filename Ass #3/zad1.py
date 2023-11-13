import json

with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

trams = {}
# TODO stops_used = {}

print(data)
for tram in data['tramwaje']:
    linia = int(tram['linia'])
    przystanki = [przystanek['nazwa'][:-3] for przystanek in tram['przystanek']]
    trams[linia] = tuple(przystanki)

print(trams)

with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(trams, file, ensure_ascii=False)


'''print("Obsługiwane przystanki")
for przystanek in stops_used:
    print(przystanek)'''