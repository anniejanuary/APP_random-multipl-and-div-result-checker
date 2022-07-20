#tabliczka mnozenia, podaje zakres do ilu ma mnozyc np do 5 i ma pokazac operacje i wyniki

import random

x=random.randint(1,6)
y=random.randint(1,6)

print(f"Enter multiplication product of {x} and {y}")
multiplication=int(input())

if multiplication == x*y:
    print("The product is correct")
else:
    print("The product is incorrect")
        
print(f"Enter the complete division result of {x} and {y}")
division=int(input())

if division == x//y:
    print("Division result correct")
else:
    print("Division result incorrect")
