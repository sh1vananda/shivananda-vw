# 1)  Concatenate two lists in the following order by using list comprehension
# Input:- list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Output:- [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’]

def concat(l1, l2):
    # res = []
    # for w1 in l1:
    #     for w2 in l2:
    #         w3 = w1 + " " + w2
    #         res.append(w3)
    res = [w1 + " " + w2 for w1 in l1 for w2 in l2]
    return res

l1 = ["Hello ", "take"]
l2 = ["Dear", "Sir"]

print(concat(l1, l2))