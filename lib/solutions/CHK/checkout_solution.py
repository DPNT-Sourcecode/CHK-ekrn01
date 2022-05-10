price_table = {
    "A": {
        "price": 50,
        "specials": {
            "reductions": [{"quantity": 3, "price": 130}, {"quantity": 5, "price": 200}]
        },
    },
    "B": {
        "price": 30,
        "specials": {
            "reductions": [{"quantity": 2, "price": 45}]
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
            "offer": {"quantity": 3, "item": "B"}
        }
    }
}


# CHK_2 more complex special offers
def checkout(skus):
    sorted_skus = sorted(skus)
    counted_skus = [[sorted_skus.count(i), i] for i in set(sorted_skus)]
    total = 0
    for count, sku in counted_skus:
        if sku not in price_table:
            return -1
        if "specials" in price_table[sku]:
            specials = price_table[sku]["specials"]
            if "reductions" in specials:
                reductions = specials["reductions"]
                # reductions have to be applied in order from the most items to the least
                sorted_reductions = sorted(reductions, key=lambda x: x["quantity"])
                for reduction in sorted_reductions:
                    quantity = reduction["quantity"]
                    price = reduction["price"]
                    # the special price is applied if the quantity is greater than or equal to the quantity
                    if quantity <= count:
                        # computes how many times the special price should be applied
                        special_count = count // quantity
                        count -= special_count * quantity
                        total += special_count * price
        total += count * price_table[sku]["price"]





# print(checkout('ABACADA'))





