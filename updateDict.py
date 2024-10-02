def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key, values in fulfillment_cart.items():
        store_inventory[key][0] = store_inventory[key][0] - values[0]
        if store_inventory[key][0] == 0:
            store_inventory[key][0] = 'Out of Stock'
    return store_inventory


cart = {
    'Orange': [1, 'Aisle 4', False],
    'Milk': [2, 'Aisle 2', True],
    'Banana': [3, 'Aisle 5', False],
    'Apple': [2, 'Aisle 4', False]
}
inventory = {
    'Banana': [15, 'Aisle 5', False],
    'Apple': [12, 'Aisle 4', False],
    'Orange': [1, 'Aisle 4', False],
    'Milk': [4, 'Aisle 2', True]}
print(update_store_inventory(cart, inventory))
