
# calc greatest common divider for two numbers
def calc_ggt(val1, val2):
    while val1 > 0 and val2 > 0:
        if val1 >= val2:
            val1 = val1 - val2
        else:
            val2 = val2 - val1
    return val1 + val2

print(calc_ggt(30,25))
