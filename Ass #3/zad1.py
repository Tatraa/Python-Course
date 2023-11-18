import json

with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

trams = {}

print(data)
for tram in data['tramwaje']:
    linia = int(tram['linia'])
    przystanki = [przystanek['nazwa'][:-3] for przystanek in tram['przystanek']]
    trams[linia] = tuple(przystanki)

print(trams)

with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(trams, file, ensure_ascii=False)


data_tramwaje = data["tramwaje"]
sorted_tr = sorted(data_tramwaje, key=lambda tram: len(tram["przystanek"]), reverse=True)
for tram in sorted_tr:
    numer_lini = tram["linia"]
    tram_stops = tram["przystanek"]
    print(f" Linia: {numer_lini} - {len(tram_stops)} przystanków")


all_stops = set()
for tram in data_tramwaje:
    tram_stops = tram["przystanek"]
    for stop in tram_stops:
        all_stops.add(stop["nazwa"])


print(f"Liczba różnych przystanków: {len(all_stops)}")