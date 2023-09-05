def addItem():
    grocery_list = []
    more_items = True

    while more_items:
        grocery_item = input("Add an item to the list: ")
        grocery_list.append(grocery_item)

        item = (input("Would you like to add another item to the list? (y or n): ")).lower()
        if (item != 'y'):
            more_items = False
    print(grocery_list)
    return grocery_list



        
addItem();