def is_eligible(age):
    return age >= 18

age = int(input("enter age: "))

if is_eligible(age):
    print("is eligible to vote")
else:
    print("not eligible to vote")