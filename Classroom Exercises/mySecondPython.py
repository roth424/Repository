animal = input("Please enter a animal:")
number = int(input("Please enter a number:"))
answer=input(f"Do you have{number} {animal}s in your pocket? ")

if(answer == 'Y'):
    inPocket=True
else:
    inPocket=False

result=animal+str(number) + str(inPocket)
print(result)