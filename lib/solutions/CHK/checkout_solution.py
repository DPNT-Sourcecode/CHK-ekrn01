"""
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+
"""
price_table = {
    "A": {
        "price": 50,
        "specials": {
            "reductions": [
                {"required_quantity": 3, "price": 130},
                {"required_quantity": 5, "price": 200},
            ]
        },
    },
    "B": {
        "price": 30,
        "specials": {"reductions": [{"required_quantity": 2, "price": 45}]},
    },
    "C": {"price": 20},
    "D": {"price": 15},
    "E": {"price": 40, "specials": {"offers": [{"required_quantity": 2, "item": "B"}]}},
    "F": {"price": 10, "specials": {"offers": [{"required_quantity": 2, "item": "F"}]}},
    "G": {
        "price": 20,
    },
    "H": {
        "price": 10,
        "specials": {
            "reductions": [
                {"required_quantity": 5, "price": 45},
                {"required_quantity": 10, "price": 80},
            ]
        },
    },
    "I": {
        "price": 35,
    },
    "J": {
        "price": 60,
    },
    "K": {
        "price": 70,
        "specials": {"reductions": [{"required_quantity": 2, "price": 120}]},
    },
    "L": {
        "price": 90,
    },
    "M": {
        "price": 15,
    },
    "N": {"price": 40, "specials": {"offers": [{"required_quantity": 3, "item": "M"}]}},
    "O": {
        "price": 10,
    },
    "P": {
        "price": 50,
        "specials": {"reductions": [{"required_quantity": 5, "price": 200}]},
    },
    "Q": {
        "price": 30,
        "specials": {"reductions": [{"required_quantity": 3, "price": 80}]},
    },
    "R": {"price": 50, "specials": {"offers": [{"required_quantity": 3, "item": "Q"}]}},
    "S": {
        "price": 20,
        "specials": {
            "group_reduction": {
                "group": ["S", "T", "X", "Y", "Z"],
                "required_quantity": 3,
                "price": 45,
            }
        },
    },
    "T": {
        "price": 20,
        "specials": {
            "group_reduction": {
                "group": ["S", "T", "X", "Y", "Z"],
                "required_quantity": 3,
                "price": 45,
            }
        },
    },
    "U": {"price": 40, "specials": {"offers": [{"required_quantity": 3, "item": "U"}]}},
    "V": {
        "price": 50,
        "specials": {
            "reductions": [
                {"required_quantity": 2, "price": 90},
                {"required_quantity": 3, "price": 130},
            ]
        },
    },
    "W": {
        "price": 20,
    },
    "X": {
        "price": 17,
        "specials": {
            "group_reduction": {
                "group": ["S", "T", "X", "Y", "Z"],
                "required_quantity": 3,
                "price": 45,
            }
        },
    },
    "Y": {
        "price": 20,
        "specials": {
            "group_reduction": {
                "group": ["S", "T", "X", "Y", "Z"],
                "required_quantity": 3,
                "price": 45,
            }
        },
    },
    "Z": {
        "price": 21,
        "specials": {
            "group_reduction": {
                "group": ["S", "T", "X", "Y", "Z"],
                "required_quantity": 3,
                "price": 45,
            }
        },
    },
}


def get_reductions_total_price(count, sku):
    reductions = price_table[sku]["specials"]["reductions"]
    reductions_total_price = 0
    reduction_items_count = 0
    # reductions have to be applied in order from the most items to the least
    sorted_reductions = sorted(
        reductions, key=lambda x: x["required_quantity"], reverse=True
    )
    for reduction in sorted_reductions:
        quantity = reduction["required_quantity"]
        price = reduction["price"]
        # the special price is applied if the quantity is greater than or equal to the quantity
        if quantity <= count:
            special_count = count // quantity
            reduction_items_count += special_count * quantity
            count -= special_count * quantity
            reductions_total_price += special_count * price
    return reductions_total_price, reduction_items_count


def remove_offered_items(counted_skus):
    for sku, count in counted_skus.items():
        if sku not in price_table:
            continue
        if "specials" not in price_table[sku]:
            continue
        if "offers" not in price_table[sku]["specials"]:
            continue
        for offer in price_table[sku]["specials"]["offers"]:
            offer_item = offer["item"]
            if offer_item not in counted_skus:
                continue
            offer_quantity = offer["required_quantity"]
            if offer_quantity > count:
                continue
            if offer_item == sku:
                counted_skus[sku] -= count // (offer_quantity + 1)
                continue
            offer_count = min(count // offer_quantity, counted_skus[offer_item])
            counted_skus[offer_item] -= offer_count
            counted_skus[offer_item] = max(counted_skus[offer_item], 0)
    return counted_skus


def index_group_reductions(counted_skus):
    group_reductions = {}
    for sku, count in counted_skus.items():
        if sku not in price_table:
            continue
        if "specials" not in price_table[sku]:
            continue
        if "group_reduction" not in price_table[sku]["specials"]:
            continue
        counted_skus[sku] = 0
        group_reduction = price_table[sku]["specials"]["group_reduction"]
        group = group_reduction["group"]
        # a group is not hashable, so we need to store it as a string
        group_name = ",".join(group)
        if group_name not in group_reductions:
            required_quantity = group_reduction["required_quantity"]
            price = group_reduction["price"]
            group_reductions[group_name] = {
                "required_quantity": required_quantity,
                "price": price,
                "skus": {},
            }
        group_reductions[group_name]["skus"][sku] = count
    return group_reductions


def sort_skus_by_price(counted_skus):
    skus_by_price = []
    for sku, count in counted_skus.items():
        if sku not in price_table:
            continue
        skus_by_price.append((sku, count, price_table[sku]["price"]))
    skus_by_price.sort(key=lambda x: x[2], reverse=True)
    return {sku: count for sku, count, _ in skus_by_price}


def remove_group_reductions_get_price(counted_skus):
    total_price = 0
    # first finding the different group reductions that can be applied
    group_reductions = index_group_reductions(counted_skus)
    for group_reduction in group_reductions.values():
        required_quantity = group_reduction["required_quantity"]
        price = group_reduction["price"]
        skus = group_reduction["skus"]
        total_skus_count = 0
        for sku, count in skus.items():
            total_skus_count += count
        items_to_remove = (total_skus_count // required_quantity) * required_quantity
        # sku's should be sorted from most expensive to least since the policy of the shop is to make the client pay the least amount
        skus = sort_skus_by_price(skus)
        for sku, count in skus.items():
            if items_to_remove <= 0 or count <= 0:
                counted_skus[sku] += skus[sku]
                continue
            if items_to_remove >= count:
                items_to_remove -= count
                skus[sku] = 0
            else:
                skus[sku] -= items_to_remove
                items_to_remove = 0
            counted_skus[sku] += skus[sku]
        total_price += (total_skus_count // required_quantity) * price
    return total_price, counted_skus


# CHK_2 more complex special offers
def checkout(skus):
    if skus == "":
        return 0
    sorted_skus = sorted(skus)
    counted_skus = {i: sorted_skus.count(i) for i in set(sorted_skus)}
    counted_skus = remove_offered_items(counted_skus)
    total, counted_skus = remove_group_reductions_get_price(counted_skus)

    for sku, count in counted_skus.items():
        if sku not in price_table:
            return -1
        count_after_reductions = count
        if "specials" in price_table[sku]:
            specials = price_table[sku]["specials"]
            if "reductions" in specials:
                (
                    reductions_total_price,
                    reduction_item_count,
                ) = get_reductions_total_price(count, sku)
                total += reductions_total_price
                count_after_reductions = count - reduction_item_count
        total += count_after_reductions * price_table[sku]["price"]
    return total


def test_checkout(sku, expected):
    value = checkout(sku)
    print("{} -> {}".format(sku, value))
    assert value == expected


# test_checkout("", 0)
# test_checkout("A", 50)
# test_checkout("AA", 100)
# test_checkout("AAA", 130)
# test_checkout("AAAAA", 200)
# test_checkout("EEEEEEAAAD", 385)
# test_checkout("EEB", 80)
# test_checkout("EEEEBB", 160)
# test_checkout("BEBEEE", 160)
# test_checkout("FFF", 20)
# test_checkout("FFFF", 30)
# test_checkout("FFFFFF", 40)
# test_checkout("FFFFFFFF", 60)
# test_checkout("XYZX", 62)
# test_checkout("XYZYSTU", 130)
# test_checkout("XYZYSTUAAAFFF", 280)
# test_checkout("ABCDEFGHIJKLMNOPQRSTUVW", 795)



