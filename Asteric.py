
def Paramid1() :
    for i in range(5,0,-1):
        for j in range(1,6):
            if i<=j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        
Paramid1()

def Paramid2() :
    for i in range(1,6):
        for j in range(1,6):
            if i<=j:
                print("*",end="")
        print()
Paramid2()

def Paramid3() :
    for i in range(1,6):
        for j in range(1,6):
            if i>=j:
                print("*",end="")
        print()
Paramid3()

def Paramid1() :
    for i in range(1,6):
        for j in range(1,6):
            if i<=j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        
Paramid1()

height=8
for i in range(1,height+1):
    print("*"*i)
    
for i in range(height,0,-1):
      print(" "*(height-i) + "*"*i)

for i in range(1,height+1):
      print(" "*(height-i) + "*"*i)
      
for i in range(8,0,-1):
      print("*"*i)
      
for i in range(1,height+1):
      print(" "*(height-i) + "*"*i+ "*"*(i-1))