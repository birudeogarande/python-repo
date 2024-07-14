def takeOrder():
    menu={
    "Pasta":100,
    "Idali":200,
    "Pohe":10
    }

    for item in menu:
        print(f"{item} : {menu[item]}")

    orderMore='y'
    total = 0
    while(orderMore=='y' or orderMore=='Y'):
        item1 = input("Please enter your order\n")
        if item1 in menu:
            print(f"{item1} is available for {menu[item1]} ruppes and will serve you soon! Thank you!!")
            # print(f"{item1} will cost you {menu[item1]} and will be add in your bill.")
            total+=menu[item1]
        else:
            print(f"{item1} is not available")    

        orderMore = input("Do you want to order more? (y/n))")
    return total;    

# bill = takeOrder();
# print(f"Your bill is : {bill}")

x= lambda a:a+10;
print(x(10))

def myFn(n):
    return lambda a:a*n


doubleN = myFn(3);

print(doubleN(11))