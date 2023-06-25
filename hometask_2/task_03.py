import yaml
from yaml import SafeLoader

equipment = {
    'items': ['станок токарный', 'станок фрезерный', 'станок сверлильный', 'станок шлифовальный'],
    'item_quantity': 4,
    'item_price': {
        'станок токарный': '8000\u20AC - 10000\u20AC',
        'станок фрезерный': '10000\u0024 - 13000\u0024',
        'станок сверлильный': '1000\u20AC - 1500\u20AC',
        'станок шлифовальный': '800\u0024 - 1000\u0024'
    }
}
with open('file.yaml', 'w') as f:
    yaml.dump(equipment, f, sort_keys=False, default_flow_style=False, allow_unicode=True)
with open('file.yaml') as f:
    equip = yaml.load(f, Loader=SafeLoader)
print(equip)
