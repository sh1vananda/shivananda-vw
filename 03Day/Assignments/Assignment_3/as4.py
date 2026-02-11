myList = ["41", "DROND", "BVSs", "13", "ZARA"]

res = [" ".join([ele]*3) if ele.isdigit() else ele+"#" for ele in myList]

print("\n".join(res))
