import math

def apply_rating(product):
    raw_rating = float(product.productrating or 4.0)
    product.rating = raw_rating
    full_stars = math.floor(raw_rating)
    decimal = raw_rating - full_stars
    if raw_rating == 5.0:
        full_stars = 5
        half_stars = 0
    elif decimal > 0:
        half_stars = 1
    else:
        half_stars = 0
    empty_stars = max(0, 5 - full_stars - half_stars)
    product.full_stars_range = range(full_stars)
    product.half_stars_range = range(half_stars)
    product.empty_stars_range = range(empty_stars)
    if (
        product.productmrpprice
        and product.productprice
        and product.productmrpprice > product.productprice
    ):
        discount = (
            (product.productmrpprice - product.productprice)
            / product.productmrpprice
        ) * 100
        product.productdiscountrate = str(int(discount))
    else:
        product.productdiscountrate = "0"
    return product