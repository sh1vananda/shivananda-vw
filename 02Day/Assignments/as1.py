def area(l, w):
    return l * w

def perimeter(l, w):
    return 2 * (l + w)

length = int(input("length: "))
width = int(input("width: "))

print(f"area: {area(length, width)}")
print(f"area: {perimeter(length, width)}")