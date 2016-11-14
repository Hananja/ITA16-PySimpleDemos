# Simple function demo

# check for prime number
def is_prime(number):
    divider = 2
    while divider < number / 2: # bis zur Hälfte
        if number % divider == 0:
            # Zahl lässt sich ohne Rest teilen
            return False
        divider = divider + 1
    return True

i = 2
while i < 100:
    if is_prime(i):
        print(i)
    i += 1

print()