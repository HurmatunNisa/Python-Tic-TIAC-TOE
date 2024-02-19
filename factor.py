def GetNumber():
    while True:
        try:
            number=int(input("Enter Number: "))
            return number
        except ValueError:
            print("Enter an Integerm Please Try Again ")
            
def Factors(n):
    factors=[]
    for i in range(1,int(n/2)+1):
        if n%i==0:
            factors.append(i)
            # corresponding_factor = n // i
            # if corresponding_factor not in factors:  # Check if the factors are distinct
            #     factors.append(corresponding_factor)
            if i==1:
                factors.append(n//i)
    return factors

print(Factors(GetNumber()))