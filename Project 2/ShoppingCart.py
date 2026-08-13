#Troy Justesen
print('Welcome to the Shopping Cart Program!')
action = ''
cart = []
money = []

while action != '6':
    print('\nPlease select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Replace item')
    print('5. Compute total')
    print('6. Buy cart')
    action = input('Please enter an action from 1-6: ')
    if action == '1':
        item = input('\nWhat item would you like to add? ').capitalize()
        price = float(input(f'What is the price of {item}? '))
        print(f'{item} has been added to the cart.')
        cart.append(item)
        money.append(price)
    elif action == '2':
        print('\nThe contents of the shopping cart are: ')
        for i, words in enumerate(range(len(cart))):
            prices = money[words]
            shopping = cart[words]
            print(f'{i + 1}. {shopping} - ${prices:.2f}')
    elif action == '3':
        print('Here is your cart: ')
        for i, words in enumerate(range(len(cart))):
            prices = money[words]
            shopping = cart[words]
            print(f'{i + 1}. {shopping} - ${prices:.2f}')
        remove = int(input('\nWhich item would you like to remove?(Choose a number next to the item) '))
        remove = remove - 1
        if remove in range(len(cart)):
            cart.pop(remove)
            money.pop(remove)
            print('Item removed')
        else:
            print('\nSorry, that is not a valid number.')
    elif action == '4':
        print('\nHere is your cart: ')
        for i, words in enumerate(range(len(cart))):
            shopping = cart[words]
            prices = money[words]
            print(f'{i + 1}. {shopping} - ${prices:.2f}')
        replace = int(input('\nWhich item would you like to replace?(Choose a number next to the item) '))
        replace = replace - 1
        if replace in range(len(cart)):
            item = input('What would you like to replace that with? ').capitalize()
            price = float(input(f'What is the price of {item}? '))
            print(f'{item} has been added to the cart.')
            cart[replace] = item
            money[replace] = price
        else:
            print('\nSorry, that is not a valid number.')
    elif action == '5':
        total = sum(money)
        print(f'\nThe total price of the items in the shopping cart is ${total:.2f}')
    elif action == '6':
        total = sum(money)
        print('\nYou bought:')
        for i in range(len(cart)):
            shopping = cart[i]
            print(shopping)
        print(f'\nAnd your total is: {total:.2f}')
        print('\nThank you for shopping. Goodbye.')
    else:
        print('\nEnter a number from 1-5.')