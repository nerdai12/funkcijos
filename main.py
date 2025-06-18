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

