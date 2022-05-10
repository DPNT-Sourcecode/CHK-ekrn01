
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
            quantity = price_table[sku]['special']['quantity']
            # the special price is applied if the quantity is greater than or equal to the quantity
            if quantity <= count:
                # computes how many times the special price should be applied
                special_count = count // quantity
                count -= special_count * quantity
                total += special_count * price_table[sku]['special']['price']
        total += count * price_table[sku]['price']
    return total

checkout('ABACAD')


        




