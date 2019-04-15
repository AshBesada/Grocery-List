# Create a dictionary
grocery_item = {}

# Create a list
grocery_history = []

# Variable used to check if the while loop condition is met
stop = False

# A while loop
# Initializes the list and asks the user for commands until he/she types 'q'.
while not stop:

    # Accept input of the name of the grocery item purchased.
    name = input('Item name:\n')

    # Accept input of the quantity of the grocery item purchased.
    quantity = input('Quantity purchased:\n')  # Modifying values

    # Accept input of the cost of the grocery item input (this is a per-item cost).
    cost = input('Price per item:\n')

    # Using the update function to create a dictionary entry which contains the name, number and price entered by the user.
    # Adding key-value pairs
    grocery_item = {'item_name': name, 'quantity': int(
        quantity), 'cost': float(cost)}

    # Add the grocery_item to the grocery_history list using the append function
    # Adding data to a list
    grocery_history.append(grocery_item)

    # Accept input from the user asking if they have finished entering grocery items.
    response = input(
        'Would you like to enter another item?\nType \'c\' for continue or \'q\' to quit:\n')

    if response == 'q':
        stop = True

# Define variable to hold grand total called 'grand_total'
grand_total = float(0.00)

# Define a 'for' loop.
# index-based range loop
for item in grocery_history:  # Accessing values in a list

    # Calculate the total cost for the grocery_item.

    item_total = item['quantity'] * item['cost']

    # Add the item_total to the grand_total
    grand_total += float(item_total)

    print("%d %s @ $%.2f ea $%.2f" %
          (item['quantity'], item['item_name'], item['cost'], item_total))

    # Reset item_total
    item_total = 0

# Print the grand total
print("Grand total: $%.2f" % grand_total)

# Pause program on screen until user hit the enter key.
input("Press \"Enter\" to close")