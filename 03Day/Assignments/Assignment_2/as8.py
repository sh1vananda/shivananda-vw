def total_price(q):
    total = q * 5
    if q > 50:
        return total - (total * 0.15)
    if q > 30:
        return total - (total * 0.1)
    else:
        return total

print(total_price(51))


