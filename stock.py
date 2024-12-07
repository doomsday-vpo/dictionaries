# Complete this tak using dictionaries.
# You will be given key-value pairs of products and quantities (on a single line separated by space). On the following line,
# you will be given products to search for. Check for each product. You have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left".
# •	Otherwise, print "Sorry, we don't have {product}".


elements = input().split()
searched_products = input().split()
bakery = {}

# First, create the complete dictionary
for i in range(0, len(elements), 2):
    food = elements[i]
    quantity = int(elements[i + 1])
    bakery[food] = quantity

# Then search for products in a separate loop
for product in searched_products:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
