def microwave():    
    return "I am microwave, I am hot"

def refigrator():
    return "I am refigrator, I am cold"

result =  microwave() + refigrator()
print( result)

print( refigrator() )


def name(first, middle, last):
    print("My name is " + first + " " + middle + " " + last)

name("Ali", "Haider", "Kasim")

name(last="Kasim", first="Arif", middle="Tajuddin")

name(middle="Haider", last="Kasim", first="Ali")

name(middle="haider", last="kasim", first="ali")


def add(*args):
    sum = 0
    for i in args:
        sum += i      
    return sum
print(add(88585,546,22))