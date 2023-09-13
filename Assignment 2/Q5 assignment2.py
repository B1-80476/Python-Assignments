
def SI_Interest_amt(amt,yr,rate):
    interest=amt*yr*rate/100
    print(f"Your SI interest is={interest}")
    total=amt+interest
    print(f"Your Total Amount is={total}")



SI_Interest_amt(10000,1,10)


