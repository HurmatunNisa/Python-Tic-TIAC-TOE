def SumOfSeries(n):
    if n==1:
        return 1
    else:
        return n**2 + SumOfSeries(n-1)
    
v=SumOfSeries(9)
print(v)