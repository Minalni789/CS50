def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):
    to_float = d.removeprefix('$')
    final = float(to_float)
    return final





def percent_to_float(p):
    tofloat = p.removesuffix("%")
    final = float(tofloat) / 100
    return final




main()