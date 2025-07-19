# Create a shopping cart programme that will continuously ask the user for a food product and the price of the product
# have an exit clause if the user wishes to stop adding more items to the cart
# At the end, show the food items and the total cost to the user

foods = []
prices = []
total = 0
tax_rate = 0.14 #VAT

while True:
    food = input("Enter a food to buy or press q to quit ")
    if food.lower() == 'q': #.lower ensures that q is recognised whether it is entered in lower case or upper case
        break
    else:
        try:
            price = float(input(f"Enter the price of the {food}: P"))
            foods.append(food)
            prices.append(price)
        except ValueError:
            print("Invalid Price! Please enter a number.")
            
#Calculate Totals
subtotal = sum(prices)
tax = subtotal * tax_rate
grand_total = subtotal + tax

#print receipt
                    
print("\n----- YOUR RECEIPT -----")
print(f"{'Item':<20}{'Price (P)':>10}")
print("-" * 30)

for food, price in zip(foods, prices):    #code shows each food item and its relevant price
    print(f"{food:<20} P{price:>9.2f}")
    
print("-" * 30)
print(f"{'Subtotal:':<20}P{subtotal:>9.2f}")
print(f"{'Tax (@14%):':<20}P{tax:>9.2f}")
print(f"{'Total:':<20}P{grand_total:>9.2f}")
print("-" * 30)

print("Thank you for shopping with us!")    
    
# for price in prices:
#     total += price #adds the prices of each food item to get to the total
    
# print("\n")    #inserts a blank line
# print(f"Your Total is: P{total:.2f}") #{total:.2f} ensures the total is set to 2 decimal places            