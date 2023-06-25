import json

order = {
    'item': '',
    'quantity': '',
    'price': '',
    'buyer': '',
    'date': ''
}

order_list = list()


def writer_order_to_json(*args):
    order['item'], order['quantity'], order['price'], order['buyer'], order['date'] = args
    with open('orders.json', encoding='utf-8') as f:
        orders_dict = json.load(f)
        order_list = orders_dict['orders']
        order_list.append(order)
        order_dict = {'orders': order_list}
        with open('orders.json', 'w', encoding='utf-8') as f:
            json.dump(order_dict, f, indent=4, ensure_ascii=False)


writer_order_to_json('принтер', '10', '6700', 'Ivanov I.I.', '24.09.2017')
writer_order_to_json('системный блок', '12', '11500', 'Kuznetsov I.A.', '01.10.2017')
writer_order_to_json('монитор', '8', '9300', 'Петров И.В.', '07.10.2017')
