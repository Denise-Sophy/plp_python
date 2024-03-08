#question one
def calculate_discount(price,discount_percent):

    if discount_percent>20:
         c=price-(price*discount_percent/100)
         return c
    else:
     return price
c=3000
d=25
e=calculate_discount(c,d)


  #question two
def calculate_discount():
    a=int(input("enter the original price: "))
    b=int(input("Enter the discount: "))
    c=a-(a*b/100)
    if b>0:
       print(c)
    else:
     print(a)
calculate_discount()
print("final price of the first one is: ",e)