def GetNumber():
    while True:
      try:
         number=int(input("Enter Number: "))
         return number
      except ValueError:
        print(" The value you entered is not and integer")

n = GetNumber()
def Fibonacci(n):
   if n<=0:
       return []
   if n==1:
       return [0]
   if n==2:
       return [0,1]
   else:
       fib=Fibonacci(n-1)
       fib.append(fib[-1]+fib[-2])
       return fib
print(Fibonacci(n))