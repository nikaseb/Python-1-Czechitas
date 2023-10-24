import math

def kontrola_cisla(n):
    if len(n) == 9 or (len(n) == 13 and n.startswith('+420')):
        return True
    else:
        print('Zadané telefoní číslo je neplatné.')
        exit()

tel_cis = input('Zadejte telefoní číslo: ')
kontrola_cisla(tel_cis)

def vrat_cenu(m):
    cena = math.ceil((len(m)) / 180) * 3
    return print(f'Cena je', cena, 'Kč.')    

SMS_zprava = input('Zadejte SMS zprávu: ')    
vrat_cenu(SMS_zprava)