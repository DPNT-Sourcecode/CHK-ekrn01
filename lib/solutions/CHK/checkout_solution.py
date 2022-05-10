
price_table = {
    'A': { 'price': 50, 'special' : { 'quantity': 3, 'price': 130 } },
    'B': { 'price': 30, 'special' : { 'quantity': 2, 'price': 45 } },
    'C': { 'price': 20 },
    'D': { 'price': 15 },
}




# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sorted_skus = sorted(skus)
    counted_skus = [[sorted_skus.count(i), i] for i in set(sorted_skus)]
    total = 0
    for count, sku in counted_skus:
        if sku not in price_table:
            return -1
        if 'special' in price_table[sku]:
            if price_table[sku]['special']['quantity'] <= count:
                special_count = count // price_table[sku]['special']['quantity']
                total += price_table[sku]['special']['price'] * special_count

        



