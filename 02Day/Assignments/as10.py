import as4

grades = list(map(int, input("enter marks in three subjects: ").split()))

average = as4.avg(grades)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"average = {average}\ngrade = {grade}")