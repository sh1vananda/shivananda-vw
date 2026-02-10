calls = int(input("enter total calls: "))

total = 200

if calls > 100:
    temp = calls - 100

    if temp <= 50:
        total += temp * 0.60
    
    if temp <= 100:
        total += 50 * 0.60 + (temp - 50) * 0.50

    else:
        total += 50 * 0.60 + 50 * 0.50 + (temp - 100) * 0.40
    
print(f"total bill = {total}")