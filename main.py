import random
from itertools import count


def say_hi(): #nieko nepriima ir nieko negrazina
    print("sveikuciai")

say_hi()
say_hi()
say_hi()


def say_hi_to(name): #priima kintamaji, bet nieko negrazina
    print("hi", name)

say_hi_to("Jonas")

def sim_pi(): #nieko nepriima, bet kazka grazina
    return 3.14

print(sim_pi())
sp = sim_pi()
print(sp)

def sumavimas(a,b): #priima du kintamuosius ir grazina reiksme
    return a+b

res = sumavimas(10,20)
print(res)

def make_initials(name, surname):
    return name[0] + surname[0]
print(make_initials("Jonas", "Smith"))

def calc_age(birth_year):
    return 2025 - birth_year

age = calc_age(2012)
print(age)

def calc_age(birth_year=2000):
    return 2025 - birth_year

age = calc_age()
print(age)

def print_info(name = "", surname = "", birth_year = 0):
    print("mano vardas", name, "mano pavarde", surname, "gimimo metai", birth_year)

print_info()
print_info("Naglis")
print_info(35)
print_info(surname="Mockevicius",birth_year = 1999)

print()

print("-----------------------------1 užduotis----------------------")

#Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.

def sumavimas(a,b):
    return a+b

res = sumavimas(1,5)
print(res)

print()

print("-----------------------------2 užduotis----------------------")

# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596;
# Gautą reikšmę atspausdinkite.

def sim_PISq():
    return 9.8596

print(sim_PISq())
PISq = sim_PISq()
print(PISq)

print()

print("-----------------------------3 užduotis----------------------")

#Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.;
# Gautą reikšmę atspausdinkite

def sandauga(a,b):
    return a*b

res = sandauga(2,5)
print(res)

print()

print("-----------------------------4 užduotis----------------------")

#Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.

masyvas = ["pirmas", "antras", "trečias", "ketvirtas"]
print(masyvas)
def nariai(masyvas):
    for narys in masyvas:
        print(narys, end = " ")
    print()

nariai(masyvas)

print()

print("-----------------------------5 užduotis----------------------")

#Sukurkite Funkciją kuri priima du kintamuosius, min ir max reikšmėms nustatyti ir
# sugeneruoja random int skaičių ir jį gražintų

def min_max(min_num,max_num):
    return random.randint(min_num,max_num)

skaicius = random.randint(1,10)
res = min_max(skaicius,skaicius)
print(res)

print()

print("-----------------------------6 užduotis----------------------")

#Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų.
# Funkcija priima tris kintamuosius, min, max ir length reikšmėms nustatyti

def funkcija(min_reiksme,max_reiksme, ilgis):
    masyvas = []
    for _ in range(ilgis):
        skaicius = random.randint(min_reiksme,max_reiksme)
        masyvas.append(skaicius)
    return masyvas

rnd_masyvas = funkcija(10,20,30)
print("Sugeneruotas masyvas ",rnd_masyvas)

print()

print("-----------------------------7 užduotis----------------------")

#Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį),
# susumuotų ir gražintų reikšmę.

def susumuota(rnd_masyvas):
    return sum(rnd_masyvas)

res = susumuota(rnd_masyvas)
print(res)

print()

print("-----------------------------8 užduotis----------------------")

#Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį

def vidurkis(rnd_masyvas):
    return sum(rnd_masyvas) / len(rnd_masyvas)

res = vidurkis(rnd_masyvas)
print(res)

print()

print("-----------------------------9 užduotis----------------------")

#Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas skaičius- išoriniam ciklui, antras vidiniam.

def staciakampis(x,y):
    for _ in range(y):
        for _ in range(x):
            print("*", end=" ")
        print()

staciakampis(10,4)

print()

print("-----------------------------10 užduotis----------------------")

# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”.
# (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)

def skaiciuoti_tarpus_raides(sakinys):
    tarpai = sakinys.count(' ')
    raidziu_kiekis = len(sakinys) - tarpai
    print("Sakinys: ", sakinys)
    print("Raidžių (be tarpų): ", raidziu_kiekis)
    print("Tarpų: ", tarpai)

skaiciuoti_tarpus_raides("Šiandien labai graži diena")

print()

print("-----------------------------11 užduotis----------------------")

#Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų.
#Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.

def apsuktas_sakinys(sakinys):
    return sakinys[::-1]

koduotas = apsuktas_sakinys("Rodos lietus kaupiasi")
print(koduotas)

print()

print("-----------------------------12 užduotis----------------------")

#Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabal satyr”

def apsuktas_zodis(sakinys):
    zodziai = sakinys.split()
    for zodis in zodziai:
        print(zodis[::-1], end=" ")
    print()

apsuktas_zodis("Labas rytas")

print()

print("-----------------------------13 užduotis----------------------")

#Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.

masyvas = ["A","B","C","D",1,2,3,4]

def tik_skaiciai(masyvas):
    for elementas in masyvas:
        if isinstance(elementas, (int, float)):
            print(elementas)

tik_skaiciai(masyvas)

print()

print("-----------------------------14 užduotis----------------------")

#Sukurkite funkciją, kuri iš paduoto masyvo atspausdina tik sveikuosius skaičius.
#(jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą True/False,
#kuris nuspręstų ar spausdins tik sveikuosius skaičius ar skaičius su kableliu

masyvas = [1,2.5,14,7.3,9,0.2]

def sveiki_skaiciai(masyvas):
    for elementas in masyvas:
        if isinstance(elementas, (int)):
            print("Sveiki skaičiai", elementas)
        else:
            if isinstance(elementas, (float)):
                print(elementas)


sveiki_skaiciai(masyvas)

print()

print("-----------------------------15 užduotis----------------------")

# Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių

sakinys = "Šiandien labai graži diena"

def word_count(sakinys):
    zodziai = sakinys.split()
    count = 0
    for zodis in zodziai:
        count += 1
    return count

res = word_count(sakinys)
print("Žodžių skaičius ", res)






