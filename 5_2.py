def main():
    

    purchase =  float(input("введите величину покупки: "))
    print()
    print(f"Сумма покупки равна:   {purchase}")
    print()
    federal_tax = get_federal_tax(purchase)
    print()
    print(f"Сумма федерального налога равна:   {federal_tax}")
    print()
    region_tax = get_region_tax(purchase)
    print()
    print(f"Сумма регионального налога равна:   {region_tax}")
    print()
    all_t = all_tax (federal_tax, region_tax)
    print()
    print(f"Сумма всех налогов:   {all_t}")
    print()
    all_p = all_prod(federal_tax, region_tax, purchase)
    print()
    print(f"Сумма покупки и налогов равна:   {all_p}")
    print()
def get_federal_tax(purchase):
    y = purchase * 0.05
    return y

def get_region_tax(purchase):
    z= purchase * 0.025
    return z

def all_tax(federal_tax, region_tax):
    q = federal_tax + region_tax
    return q

def all_prod(federal_tax, region_tax, purchase):
    w = federal_tax + region_tax + purchase
    return w

