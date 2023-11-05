class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = True

    def pujc_auto(self):
        if self.dostupnost == True:
            self.dostupnost = False
            return f'Potvrzuji zapůjčení vozidla.'
        else:
            return f'Vozidlo není k dispozici.'
        
    def get_info(self):
        return f'Poznávací značka vozidla: {self.registracni_znacka}, typ vozidla: {self.typ_vozidla}, dostupnost: {self.dostupnost}'
    
peugot = Auto('4A2 3020', 'Peugot 403 Cabrio', 47534)
skoda = Auto('1P3 4747', 'Škoda Octavia', 41253)

vyber_auta = input('Vyberte značku vozidla (Škoda, Peugot): ')

if vyber_auta == 'Škoda':
    print(skoda.get_info())
    print(skoda.pujc_auto())
elif vyber_auta == 'Peugot':
    print(peugot.get_info())
    print(peugot.pujc_auto())
else:
    print('Litujeme, vybraná značka vozidla není k dispozici.')

#print(peugot.get_info())
#print(peugot.pujc_auto())
#print(peugot.get_info())
#print(peugot.pujc_auto())
#print(skoda.get_info())