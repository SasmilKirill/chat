import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_n:
        f_n_content = f_n.read()
        obj = json.loads(f_n_content)
    if obj and 'orders' in obj.keys():
        old_orders = obj['orders']
    else:
        old_orders = []
    new_order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    old_orders.append(new_order)
    dict_to_json = {'orders': old_orders}
    with open('orders.json', 'w') as f_n:
        f_n.write(json.dumps(dict_to_json, indent=4))


if __name__ == '__main__':
    write_order_to_json('12345', 1, 50.09, 'Thrall', '2023-03-12')
    write_order_to_json('12346', 2, 10.76, 'Garosh', '2023-03-15')
    write_order_to_json('12381', 2, 20.00, 'Varian', '2023-03-19')
    write_order_to_json('12762', 1, 10.06, 'Anduin', '2023-03-24')