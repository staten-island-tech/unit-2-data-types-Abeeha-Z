# Challenge 1
""" x = (int(input("Is it even or odd?")))
if (x%2) > 0:
    print("odd")
else:
    print("even") """
# CHallnege2
# x = (int(input("What are all the factors of this number?")))
# if (x%2)

#  def get_all_factors(n)
#         factors = []
#         for  i in range(1 + n+1)
#         if n%i == 0
#         factors.append(i)
y = int(input("What is the bill?"))
service = input("how was the service? ")
if service == "bad":
    print(y)
if service == "okay":
    print(y + (y%15))
if service == "good":
    print(y + (y%20))
if service == "great":
    print(y + (y%25))