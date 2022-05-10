
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
        


