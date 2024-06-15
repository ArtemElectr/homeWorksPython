my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

# 1 вариант
while my_list[i] >= 0 and i < len(my_list):
    if my_list[i] == 0:
        i += 1
        continue
    print(my_list[i])
    i += 1

# 2 вариант
print(' ')
i = 0
while i < len(my_list):
    if my_list[i] < 0:
        break
    elif my_list[i] > 0:
        print(my_list[i])
        i += 1
        continue
    elif my_list[i] == 0:
        i += 1
