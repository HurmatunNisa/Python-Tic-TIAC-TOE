def Power(n,p):
    power=1
    for i in range(1,p+1):
       power*=n
    print(power)
    
Power(3,3)