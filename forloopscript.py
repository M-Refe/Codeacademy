#A day in the Supermarket

prices = {
  "banana" : 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
  }
#created (dictionary) prices for my supermarket

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
#created (dictionary) stock count for my supermarket

#add for loop to print key with price and stock information
for key in prices:
  print (key)
  print ("price: %s" % prices[key])
  print ("stock: %s" % stock[key])

#record total value of inventory
  # Create a variable called total and set it to zero.
  # Loop through the prices dictionary.
  # For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
  # Finally, outside your loop, print total.
total = 0
for food in prices:
  print (prices[food] * stock[food])
  total = total + prices[food] * stock[food]
print (total)

#make consumer interface, created groceries list
groceries = ["banana", "orange", "apple"]

#making a purchase
  # Define a function compute_bill that takes one argument food as input.
  # In the function, create a variable total with an initial value of zero
  # For each item in the food list, add the price of that item to total.
  # Finally, return the total.
  # Ignore whether or not the item you're billing for is in stock.  Note that your function should work for ANY food list.

def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total

#changing function
#only adding to total as long as stock is > 0.
# and then when adding price to total, stock item is subtracted by 1
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total
