class Circle:
    pi = 3.14

    def area(radius):
        return Circle.pi * radius ** 2
    
    def circumference(radius):
        return 2 * Circle.pi * radius
    

print(f"area: {Circle.area(5)}")
print(f"circumference: {Circle.circumference(5)}")

