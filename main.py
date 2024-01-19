# Item list----------------
snack_price = {
  'Loaded': 10,
  'Tomy': 9,
  'Nova': 18
}
drink_price = {
  'Coke': 12,
  'Sprite': 12,
  'Royal': 12,
}
biscuit_price = {
  'Fudge bar': 9,
  'Dowee donut': 12,
  'Overload': 10,
}
# Item list----------------


# Display------------------
snack_list = ["Loaded (10)", "Tomy (9)", "Nova(18)"]
print('(Snacks):',', '.join(snack_list))
drink_list = ["Coke (12)", "Sprite (12)", "Royal (12)"]
print('(Drinks):',', '.join(drink_list))
my_list = ["Fudge bar (9)", "Dowee donut (12)", "Overload (10)"]
print('(Biscuits):',', '.join(my_list))
# Display------------------


# Input command------------
user_inputs = []
user_input = input("Enter category (snacks,drinks,biscuts): ")
# Input command------------
  
  
# Category-----------------
if user_input.lower() == 'snacks':
  snack = str(input("(Choose snack): "))
  # Types of snack
  if snack in snack_price:
    # Quantity
    quantity = int(input("(Quantity): "))
    # Amount
    amount = int(input("(Amount): "))
    # If insufficient balance
    compute = quantity * snack_price[snack]
    if amount < compute:
      print("Insufficient balance, try again")
    # Reciept
    else:
      total_sales = 10
      remaining_stocks = total_sales - quantity
      print("Receipt")
      print(f"Snack: {snack}")
      print(f"Quantity: {quantity}")
      print(f"Amount: {amount}")
      amount -= compute
      print(f"Change: {amount}")
      print(f"Stocks: {total_sales}, {remaining_stocks} left remaining ")
  else:
    print(f"{snack}, not found")
    
elif user_input.lower() == 'drinks':
  drink = str(input("(Choose drinks): "))
  # Types of drinks
  if drink in drink_price:
    # Quantity
    quantity = int(input("Quantity: "))
    # Amount
    amount = int(input("Amount: "))
    # If insufficient balance
    compute = quantity * drink_price[drink]
    if amount < compute:
      print("Insufficient balance, try again")
    # Reciept
    else:
      total_sales = 10
      remaining_stocks = total_sales - quantity
      print("Reciept")
      print(f"Drink: {drink}")
      print(f"Quantity: {quantity}")
      print(f"Amount: {amount}")
      amount -= compute
      print(f"Change: {amount}")
      print(f"Stocks: {total_sales}, {remaining_stocks} left remaining")
  else:
    print(f"{drink}, not found")
elif user_input.lower() == 'biscuits':
  biscuit = str(input("(Choose biscuit): "))
  # Types of biscuit
  if biscuit in biscuit_price:
    # Quantity
    quantity = int(input("Quantity: "))
    # Amount
    amount = int(input("Amount: "))
    # If insufficient balance
    compute = quantity * biscuit_price[biscuit]
    if amount < compute:
      print("Insufficient balance, try again")
    #Reciept
    else:
      total_sales = 10
      remaining_quantity = total_sales - quantity
      print("Reciept")
      print(f"Biscuit: {biscuit}")
      print(f"Quantity: {quantity}")
      print(f"Amount: {amount}")
      amount -= compute
      print(f"Change: {amount}")
      print(f"Stocks: {total_sales}, {remaining_quantity} left remaining")
  else:
    print(f"{biscuit}, not found")
    
else:
  print("Error: Unknown item code, try again")
# Category-----------------