ton_to_kg = lambda w : w * 1000
kg_to_gm = lambda w : w * 1000
gm_to_mg = lambda w : w * 1000 # or a single lambda function for all three since the same logic is used
mg_to_lb = lambda w : w / 453592

funcs = [ton_to_kg, kg_to_gm, gm_to_mg, mg_to_lb]
units = ["kg", "gm", "mg", "lbs"]

weight = float(input("enter weight in tons: "))

res = weight
for i in range(4):
    res = funcs[i](res)
    print(res, f"{units[i]}")