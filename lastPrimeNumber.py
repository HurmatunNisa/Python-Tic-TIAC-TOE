def GetNumber():
    while True:
      try:
         number=int(input("Enter Number: "))
         return number
      except ValueError:
        print(" The value you entered is not and integer")


def IsPrime(number, i):
    if i==1:
        return True
    elif number%i==0:
        return False
    else:
        return IsPrime(number, i-1)
        
    
        
def lastPrimeNumber():
    number=GetNumber()
    for i in range(number,1,-1):
        indicator = IsPrime(i, i-1)
        if indicator:
            print(i)
            break
   
lastPrimeNumber()               