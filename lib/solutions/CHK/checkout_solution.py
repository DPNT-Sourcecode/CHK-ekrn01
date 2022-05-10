# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+

price_table = {
    "A": {
        "price": 50,
        "specials": {
            "reductions": [{"required_quantity": 3, "price": 130}, {"required_quantity": 5, "price": 200}]
        },
    },
    "B": {
        "price": 30,
        "specials": {
            "reductions": [{"required_quantity": 2, "price": 45}]
        },
    },
    "C": {
        "price": 20
    },
    "D": {
        "price": 15
    },
    "E": {
        "price": 40,
        "specials": {
            "offers": [{"required_quantity": 2, "item": "B"}]
        }
    },
    "F": {
        "price": 10,
        "specials": {
            "offers": [{"required_quantity": 2, "item": "F"}]
        }
    },
    "G": {
        "price": 20,
    },
    "H": {
}

def get_reductions_total_price(count, sku):
    reductions = price_table[sku]["specials"]["reductions"]
    reductions_total_price = 0
    reduction_items_count = 0
    # reductions have to be applied in order from the most items to the least
    sorted_reductions = sorted(reductions, key=lambda x: x["required_quantity"], reverse=True)
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
    

# CHK_2 more complex special offers
def checkout(skus):
    if skus == "":
        return 0
    sorted_skus = sorted(skus)
    counted_skus = {i:sorted_skus.count(i) for i in set(sorted_skus)}
    total = 0
    counted_skus = remove_offered_items(counted_skus)
    for sku, count in counted_skus.items():
        if sku not in price_table:
            return -1
        count_after_reductions = count
        if "specials" in price_table[sku]:
            specials = price_table[sku]["specials"]
            if "reductions" in specials:
                reductions_total_price, reduction_item_count = get_reductions_total_price(count, sku)
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





