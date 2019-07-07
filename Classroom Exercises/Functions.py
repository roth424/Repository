def MySubName():
    print("Hello")

def MyFunction():
    return 10

MySubName()
x=MyFunction()
print(x)

def Multiply(num1,num2):
    return num1 * num2

x=Multiply(5,3)
print(x)

def House(address,sqFeet, price):
    print(address, str(sqFeet), "$" + str(price))

House("123 Street", 1000, 250000)
print(House)

def MultiplyList (numbers):
    result=1
    for number in numbers:
        result=result * number
    return result

print (MultiplyList([1,2,4,6,8,13]))