nums_list = [1, 2, 3, 4, 5]

nums_tuple = (6, 7, 8, 9, 10)

text_list = list(map(lambda num: str(num), nums_list))

text_list.extend(list(map(lambda num: str(num), nums_tuple))) # or initialize new list and perfect list concat

print(text_list)