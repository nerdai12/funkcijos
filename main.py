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