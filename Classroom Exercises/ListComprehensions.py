flintstones=['fred', 'wilma', 'pebbles', 'dino']

newNames=[]
for name in flintstones:
    if name == 'dino':
        newNames.append(name.Upper())
    newNames.append(name.title())

print(newNames)
#line 9 replaces lines 3,4,5
newNames=[name.title() for name in flintstones]

print(newNames)
