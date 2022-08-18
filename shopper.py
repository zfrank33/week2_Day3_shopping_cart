import copy
shelf = {
    "item1":[90,500,10],
    "item2":[1,300,15],
    "item3":[1,200,20],
    "item4":[10,300,25],
    "item5":[12,200,12],
    "item6":[100,300,14],
}
def pick_item(action,item,quantity ):
    if action == "pick":
        print("quantity")
        print(quantity)
        print(type(quantity))
        print(shelf[item][2])
        print(type(shelf[item][2]))
        if quantity <= shelf[item][2]:
            shelf[item][2] = shelf[item][2]-quantity
            # return_item = shelf[item]
            return_item =copy.deepcopy(shelf)
            return_item[item][2] = quantity
            return return_item[item]
        else:
            return "Quantity is less"
    elif action == "return":
        shelf[item][2] = shelf[item][2]+quantity
            # return_item = shelf[item]
        return "Succesful Returned"
    else:
        return "choose a smaller amount invalid action"

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
cart = list()
check = True
print("++++++++++++++++++++SHELF+++++++++")
print(shelf)
print("+++++++++++++++++++++++++++++++")
while check:
    print("++++++++++++++++++++SHELF+++++++++")
    print(shelf)
    print("+++++++++++++++++++++++++++++++")
    choice = input("Type s to Show,a to Add,d to Delete and q to Quit")
    print("You chose :" +str(choice))
    choice = str(choice).lower()

    if choice == "a":
        item = input("pick item from shelf: ")
        quantiy = input("How many would you like")
        return_item = pick_item("pick",item, int(quantiy) )
        cart.append({item:return_item})
    elif choice == "s":
        print("You Cart contains the following")
        print(cart)
    elif choice == "d":
        item = input("pick item to return to shelf: ")
        q = input("How many would you like to return: ")
        quantity = int(q)
        pick_item("return", item, int(quantity))
        counter = 0
        for c in cart:
            print(c)
            print(counter)
            if item in c:
                print("c2")
                print(c[item][2])
                print(type(c[item][2]))
                print("quantity")
                print(quantity)
                print(type(quantity))
                if quantity >= int(c[item][2]):
                    cart.remove(c)
                else:
                    c[item][2]=c[item][2]-quantity
            else:
                print("counter in else")
                counter=counter+1
        print("Counter = :"+str(counter))
        print("carter len = :"+str(len(cart)))

        if counter == len(cart):
            print("item is not in ur cart")


    elif choice == "q":
        print("Behold Your Cart")
        print(cart)
        print("Good Bye!")
        check = False
    else:
        print("choose a smaller amount invalid action")
        # pass
