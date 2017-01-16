
# Demo von Generatoren

def dump_generator(generatorparam):
    print("Typ: ", type(generatorparam))
    print("Daten: ", generatorparam)
    print("Elemente: ", end="")
    for index in generatorparam:
        print(index, end=", ")
    print()

def div2(num):
    while num % 2 == 0:
        yield num
        num = num // 2
    yield num

dump_generator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
dump_generator(range(12)) # Generator
dump_generator(list(range(12)))
dump_generator(div2(1024))