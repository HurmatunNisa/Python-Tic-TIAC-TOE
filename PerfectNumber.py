
def CalculateDivisors(number):
    divisors=[]
    for i in range(1,int(number/2)+1):
        if number%i == 0:
            divisors.append(i)
    return divisors       

def IsPerfectNumber():
    for number in range(1,501):
        numbers=CalculateDivisors(number)
        sum=0
        for each in numbers:
          sum+= each
        if sum == number:
            print(f"The number {number} is a Perfect Number")
    
IsPerfectNumber()