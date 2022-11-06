import random

def gameWin(comp, you):
    if comp == you: #if two values are equal, declare a tie!
        return None

    #check all the possiblities when computer choose s    
    elif comp =='s':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    #check all the possiblities when computer choose w
    elif comp =='w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    #check all the possiblities when computer choose g          
    elif comp =='g':
        if you == 's':
            return False
        elif you == 'w':
            return True             

print("Comp Turn: Snake(s) Water(r) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp ='s'
elif randNo == 2:
    comp = 'w'
elif randNo ==3:
    comp = 'g'    

# print(randNo)

# a = input("Comp Turn: Snake(s) Water(r) or Gun(g)?")
you = input("Your Turn: Snake(s) Water(r) or Gun(g)?")

a = gameWin(comp, you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("The game is tie")
elif a:
    print("you win")    
else:
    print("you lose")
