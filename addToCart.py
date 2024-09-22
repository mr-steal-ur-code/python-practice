

items = [
    {"name": "apple", "price": 0.5},
    {"name": "banana", "price": 0.3},
    {"name": "orange", "price": 0.7},
]

cart = []


def add_to_cart(item_name, quantity):
    for item in items:
        if item['name'].lower() == item_name.lower():
            cart.append(
                {"name": item['name'], "price": item['price'], "quantity": quantity})
            print(f"Added {quantity} {item['name']} to cart. Total {
                  item['price'] * quantity}")
            return


# Call the function
add_to_cart("banana", 1)
