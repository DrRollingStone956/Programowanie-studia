def check_if_even(x):
    if x % 2 == 0:
        return True
    else: return False
my_number = check_if_even(43)
if my_number == True:
    print("Liczba parzysta")
elif my_number == False:
    print("Liczba nieparzysta")