# greater = lambda a, b : a if a > b else b

# print(greater(6, 7))

# ---

# def outer():
#     print("outer")
#     def inner():
#         num = 22
#         print("inner")
#     inner()

# outer()

# ---

# def square_num(num):
#     return num*num

# def square_text(text):
#     return text+" "+text

# def square(x, operation):
#     return operation(x)

# x = input("input: ")

# if x.isdigit():
#     print(square(int(x), square_num))
# else:
#     print(square(x, square_text))

# ---

# built_in_namespace = dir()

# print(built_in_namespace)

# ---

# x = 100 # global scope
# def outer():
#     a = 10 # local scope
#     b = 20
#     def inner():
#         c = 30 # enclosed scope
#         return x - (a + b + c)
#     return inner()

# print(outer())  

# ---

# x = 100

# def outer():
#     global x
#     x -= 10
#     def inner():
#         global x
#         x -= 10
#     inner()

# outer()
# print(x)

# ---

