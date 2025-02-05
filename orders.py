# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, that already exists, increase its quantity by the input
# quantity and if its price is different, replace the price as well.
# You will receive products(' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. Finally, print all items with their names and the total price of each product.)
# Input
# •	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# •	The product data is always delimited by a single space.
# Output
# •	Print information about each product in the following format:
# "{product_name} -> {total_price}"
# •	Format the total price to the 2nd digit after the decimal separator.


products = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {'price': price, 'quantity': quantity}
    else:
        products[name]['quantity'] += quantity
        products[name]['price'] = price

for product_name, product_info in products.items():
    total_price = product_info['price'] * product_info['quantity']
    print(f"{product_name} -> {total_price:.2f}")
