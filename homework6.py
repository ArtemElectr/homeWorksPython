# 2

my_dict = {"Artemy": 1989, "Alex": 2000, "Mary": 2005}

print("Dict:", my_dict)
print("Existing value:",my_dict["Artemy"])
print("Not existing value:", my_dict.get("Antony"))
my_dict.update({"Tony": 1985, "Sten": 1997})
del_couple = my_dict.pop("Alex")
print("Deleted value:", del_couple)
print("Modified dictionary:", my_dict)

# 3

my_set = {1, 2, 1, 2, 'str', (1, "val"), 'str', 65.45}
print("Set:", my_set)
my_set.add(95.16)
my_set.add('June')
my_set.remove(2)
print("Modified set:", my_set)