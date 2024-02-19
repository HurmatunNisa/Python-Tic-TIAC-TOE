def SumOfSeries(n):
    if n==1:
        return 1
    else:
        return n + SumOfSeries(n-1)

def Series(n):
    if n==1:
        return 1
    else:
        return SumOfSeries(n)+Series(n-1)
    
answer=Series(6)
print(answer)


