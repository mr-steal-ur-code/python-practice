def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    cart_list = sorted(cart.items(), reverse=True)
    for item, quantity in cart_list:
        if item in aisle_mapping:
            aisle_info = aisle_mapping[item]
            aisle_info.insert(0, quantity)
            fulfillment_cart[item] = aisle_info
    return fulfillment_cart


cart = {'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2}
details = {
    'Banana': ['Aisle 5', False],
    'Apple': ['Aisle 4', False],
    'Orange': ['Aisle 4', False],
    'Milk': ['Aisle 2', True]
}
print(send_to_store(cart, details))
