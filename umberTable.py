# number=int(input("Enter Number: "))
# for x in range(1,13):
#     print(f"{number}  *  {x}   =   {number*x}")


def GetNumber():
    while True:
      try:
         number=int(input("Enter Number: "))
         return number
      except ValueError:
        print(" The value you entered is not and integer")

def Table():
    try:
        numberForTable = GetNumber()
        for x in range(1,13):
            print(f"{numberForTable}  *  {x}   =   {numberForTable*x}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
       
Table()