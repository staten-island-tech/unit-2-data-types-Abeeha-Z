""" """ # Challenge 1
""" x = (int(input("Is it even or odd?")))
if (x%2) > 0:
    print("odd")
else:
    print("even") """


""" y = int(input("What is the bill?"))
service = input("how was the service? ")
if service == "bad":
    print(y)
if service == "okay":
    print(y + (y%15))
if service == "good":
    print(y + (y%20))
if service == "great":
    print(y + (y%25)) """


""" def allfactors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors
number = int(input("Please enter a number: "))
listfactors = allfactors(number)
print(listfactors)
 """

numx = int(input("what is the first number? "))
numy = int(input("What is the second number? "))
def gcf(numx,numy):
    if numx > numy:
        x= numy
    else:
        x= numx
        for i in range(1,x+1):
            if numx%i == 0 and numy%i == 0:
                hcf = i
        return hcf
print(gcf(numx,numy))