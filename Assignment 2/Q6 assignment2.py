
def CI_Interest_amt(principle,yr,rate):
    half_cal=(1+rate/100)**yr
    Total=principle*half_cal
    print(f"Your Total Amount is={Total}")
    interest=Total-principle
    print(f"Your CI interest is={interest}")



CI_Interest_amt(10000,2,10)