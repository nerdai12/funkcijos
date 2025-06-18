import random


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