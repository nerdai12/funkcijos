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

print()

print("-----------------------------16 užduotis----------------------")

#Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean.
#Funkcija gražina prafiltruotą masyvą.
#Kai antras parametras True/tik poriniais skaičiais, False/tik neporiniais skaičiais.

masyvas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
poriniai = True

def filtruotas_masyvas(masyvas,poriniai):
    rezultatas = []
    for skaicius in masyvas:
        if poriniai and skaicius % 2 == 0:
            rezultatas.append(skaicius)
        elif not poriniai and skaicius % 2 != 0:
            rezultatas.append(skaicius)
    return rezultatas

res = filtruotas_masyvas(masyvas,poriniai)
print(res)
print()

print()

print("-----------------------------17 užduotis----------------------")

#Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis



def number_is_prime (num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(number_is_prime(14))
print(number_is_prime(5))

print()

print("-----------------------------18 užduotis----------------------")

#Sukurkite funkciją kuri priima du argumentus.
#Gražina pirmąjį skaičių pakeltą laipsniu tokiu kaip antras skaičius

def pakelta_laipsniu(a,b):
    return a ** b

print(pakelta_laipsniu(2,5))

print()

print("-----------------------------19 užduotis----------------------")

#Sukurkite funkciją kuri priima skaičių masyvą ir gražina tik nepasikartojančius elementus

masyvas = [random.randint(1,10) for _ in range(15)]
print(masyvas)

def nesikartoja(masyvas):
    rezultatas = []
    for skaicius in masyvas:
        if masyvas.count(skaicius) == 1:
            rezultatas.append(skaicius)
    return rezultatas

print(nesikartoja(masyvas))

print()

print("-----------------------------20 užduotis----------------------")

# Sukurkite funkciją kuri priima tekstą ir atspausdina tekste daugiausiai pasikartojantį simbolį.

text = "Sukurkite funkciją kuri priima tekstą ir atspausdina tekste daugiausiai pasikartojantį simbolį"

def daugiausiai_pasikartojantis(text):
    daznis = {}
    for simbolis in text:
        daznis[simbolis] = daznis.get(simbolis, 0) + 1
        dazniausias = max(daznis, key=daznis.get)
        kiek = daznis[dazniausias]
    print("Dažniausiai pasikartojantis simbolis  yra '", str(dazniausias), "' ir pasikartoja ", kiek, " kartų")


daugiausiai_pasikartojantis(text)

print()

print("-----------------------------21 užduotis----------------------")

# Sukurkite funkciją kuri priima tekstą ir atspausdina jame esantį ilgiausią žodį.

text = "Sukurkite funkciją kuri priima tekstą ir atspausdina jame esantį ilgiausią žodį"

def longest_word(text):
    zodziai = text.split()
    ilgiausias = ""
    for zodis in zodziai:
        if len(zodis) > len(ilgiausias):
            ilgiausias = zodis
    print("Ilgiausias žodis: ", ilgiausias)

longest_word(text)


print()

print("-----------------------------Sunkesni 1 užduotis----------------------")

#Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje
#pridedant “---” pradžioje ir gale. PVZ (---labas---)

text = "Parašykite funkciją, kurios argumentas būtų tekstas"

def tekstas_su_priedais(text):
    print("---", text, "---")

tekstas_su_priedais(text)

print()

print("-----------------------------Sunkesni 2 užduotis----------------------")

#Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu.
#Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75].

def generate_rnd_str(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

string = generate_rnd_str(10)
print(string)

i = 0

while i < len(string):
    if string[i].isdigit():
        buffer = ""
        while i < len(string) and string[i].isdigit():
            buffer += string[i]
            i += 1
        print("[", buffer, "]", sep="")
    else:
        print(string[i])
        i += 1

print()

print("-----------------------------Sunkesni 3 užduotis----------------------")

#Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas dalijasi be liekanos
#(išskyrus vienetą ir patį save). Pvz padavus 10 turi grąžinti 2,  o padavus 20 gražintų 4

def dalikliu_kiekis(a):
    kiek = 0
    for i in range(2,a):
        if a % i == 0:
            kiek += 1
    return kiek

dalikliu_kiekis(10)
print(dalikliu_kiekis(10))
print(dalikliu_kiekis(20))

print()

print("-----------------------------Sunkesni 4 užduotis----------------------")

#Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77.
#Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją

masyvas = [random.randint(33,77) for _ in range(100)]
print(masyvas)
surusiuotas = sorted(masyvas, key=dalikliu_kiekis, reverse=True)
print(surusiuotas)

print()

print("-----------------------------Sunkesni 5 užduotis----------------------")

#Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 333 iki 777.
#Naudodami 3 uždavinio funkciją iš masyvo suskaičiuokite kiek yra pirminių skaičių

masyvas = [random.randint(333,777) for _ in range(100)]
print(masyvas)

pirminiu_kiekis = 0
for skaicius in masyvas:
    if dalikliu_kiekis(skaicius) == 0: #skaicius yra pirminis
        pirminiu_kiekis += 1
print("pirminių skaičių kiekis: ", pirminiu_kiekis)

print()

print("-----------------------------Sunkesni 8 užduotis----------------------")

#Sugeneruokite masyvą iš trijų elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 33.
#Jeigu tarp trijų paskutinių elementų yra nors vienas ne pirminis skaičius,
#prie masyvo pridėkite dar vieną elementą- atsitiktinį skaičių nuo 1 iki 33.
#Vėl patikrinkite pradinę sąlygą ir jeigu reikia pridėkite dar vieną elementą.
#Kartokite, kol sąlyga nereikalaus pridėti elemento.

masyvas = [random.randint(1,33) for _ in range(3)]
print(masyvas)
