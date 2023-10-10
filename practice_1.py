"""
Having a price list of all the products as given above, combining the information from the both data dictionary, write algorithm to calcualte:

Total price of Apple across all storage hubs: Ex: expected = {"apple": ..., "unit": "usd"}
Total price of Orange across all hubs Ex: expected = {"orange": ..., "unit": "usd"}
Total product cost per hub Ex. expected = {"india": ..., "bangladesh": ..., "czech-republic": ..., "unit": "usd"}
Which hub is more costly in terms of price of total apple and orange combined?

"""

fruit_bank = {
    "india": {
        "apple": {"amount": 100, "unit": "pcs"},
        "orange": {"amount": 300, "unit": "kg"},
        "grape": {"amount": 200, "unit": "kg"},
    },
    "bangladesh": {
        "apple": {"amount": 500, "unit": "pcs"},
        "orange": {"amount": 800, "unit": "kg"},
        "grape": {"amount": 60000, "unit": "kg"},
    },
    "czech-republic": {
        "apple": {"amount": 1000, "unit": "pcs"},
        "orange": {"amount": 200, "unit": "kg"},
        "grape": {"amount": 500, "unit": "kg"},
    },
}

product_prices = {
    "india": {
        "apple": {"price": 3, "unit": "usd"},
        "orange": {"price": 7, "unit": "usd"},
        "grape": {"price": 6, "unit": "usd"},
    },
    "bangladesh": {
        "apple": {"price": 5, "unit": "usd"},
        "orange": {"price": 9, "unit": "usd"},
        "grape": {"price": 4, "unit": "usd"},
    },
    "czech-republic": {
        "apple": {"price": 15, "unit": "usd"},
        "orange": {"price": 20, "unit": "usd"},
        "grape": {"price": 12, "unit": "usd"},
    },
}


def each_coutry_and_amount(desh, fall):
    for countries, products in fruit_bank.items():
        if countries == desh and fall in products:
            price_each = products[fall]["amount"]
    for countries, products in product_prices.items():
        if countries == desh and fall in products:
            qnty_each = products[fall]["price"]
    return price_each * qnty_each


all_desh = []
all_fall = []

for countries, products in fruit_bank.items():
    all_desh.append(countries)

for countries, products in fruit_bank.items():
    for product, price in products.items():
        all_fall.append(product)

unique_fall = list(set(all_fall))

all_fall_1 = []
sep_amount_1 = []

for fall_1 in unique_fall:
    ttl_amount = 0
    for country_1 in all_desh:
        ttl_amount += each_coutry_and_amount(country_1, fall_1)
    all_fall_1.append(fall_1)
    sep_amount_1.append(ttl_amount)

for fruit_2, amount_1 in zip(all_fall_1[::-1], sep_amount_1[::-1]):
    my_dict = {}
    key_1 = fruit_2.title()
    val_1 = amount_1
    my_dict[key_1] = val_1

    unit_dict = {"unit": "usd"}  # create unit as hard coded
    result_dict = {**my_dict, **unit_dict}  # merge two dictionaries
    print(f"Total price of Apple across all storage hubs:{result_dict}")

print()

all_country_dict = []
for i in all_desh:
    ttl_amount = 0
    for j in unique_fall:
        my_dic = {}
        ttl_amount += each_coutry_and_amount(i, j)
        key = i.title()
        val = ttl_amount
        my_dic[key] = val
    all_country_dict.append(my_dic)

answer_dict = {}
for dic in all_country_dict:
    answer_dict.update(dic)

unit_dict = {"unit": "usd"}
result_dic = {**answer_dict, **unit_dict}
print(f"Total product cost per hub", result_dic)

max_key = 0
max_value = 0

for key, value in answer_dict.items():
    if max_value is None or value > max_value:
        max_key = key
        max_value = value

print(
    f"{max_key} hub is more costly in terms of price of total apple and orange combined"
)
