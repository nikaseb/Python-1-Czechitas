sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input('Zadejte kód součástky: ')
ks = int(input('Zadejte množství: '))

if kod not in sklad:
    print('Součástka není skladem.')
else:
    if sklad[kod] < ks:
        print(f'Požadované množství ks součástky není na skladu dostupné. Lze vydat pouze množství na skladě.')
        sklad.pop(kod)
    else:
        print('Požadované množství ks je na skladě.')
        sklad[kod] -= ks

print(sklad)