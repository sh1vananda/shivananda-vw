people={'Arham':'Blue', 'Lisa':'Yellow', 'Vinod':'Purple', 'Jenny':'Pink'}

print(f"A. Total students: {len(people)}")

people["Lisa"] = "Black"

print(f"B. Lisa's new favourite color: {people["Lisa"]}")

people.pop("Jenny")

print(f"C. {list(people.items())}")

sorted_p = sorted(people.items())

print(f"D. {list(sorted_p)}")
