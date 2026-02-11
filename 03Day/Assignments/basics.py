# 1. Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”

d = {"table": ["a piece of furniture", "list of facts & figures"], "cat": "a small animal"}
print(list(d.items()))

# 2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# ”python”, “java”, “C++”, “python”, “javascript”,
# “java”, “python”, “java”, “C++”, “C”

l1 = ["python", "java", "C++", "python", "javascript"]
print(f"number of classes required: {len(set(l1))}")

l2 = ["java", "python", "java", "C++", "C"]
print(f"number of classes required: {len(set(l2))}")

# 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

for i in range(3):
    key, value = input(f"enter subject {i + 1} name followed by marks: ").split()
    marks[key] = value

print(marks)

# 4. Figure out a way to store 9 & 9.0 as separate values in the set. 
# (You can take help of built-in data types) 

s = set()

s.add('9')
s.add('9.0')

print(s)

# 5. WAP to find the occurrence of '$' in a string
#  str = "Hi, $I am the $ Symbol $99.99"

st = "Hi, $I am the $ Symbol $99.99"

print(f"total occurrences: {st.count('$')}")

st2 = [i for i, c in enumerate(st) if c == "$"]

print(f"indices: {st2}")

# c = 0
# for i in st:
#     if i == "$":
#         c += 1

# print(c)