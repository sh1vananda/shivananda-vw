def c_to_f(t):
    return (t * 9/5) + 32

def f_to_c(t):
    return (t - 32) * 5/9

temp = int(input("temperature: "))

print("1. celsius to farenheit  2. farenheit to celsius")
choice = int(input("choice: "))

match choice:
    case 1: print(f"converted to farenheit: {c_to_f(temp)}")
    case 2: print(f"converted to celsius: {f_to_c(temp)}")

