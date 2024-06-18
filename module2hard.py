

def search_pair_of_numbers(input_value):
    if input_value < 3 or input_value > 20:
        return 0
    list_summ = []
    for i in range(1, input_value):
        for j in range(1, input_value):
            if input_value == i or input_value == j:
                continue

            if input_value % (i + j) == 0 and i < j:
                list_summ.append(i)
                list_summ.append(j)

    return list_summ


while True:
    value_ = int(input("Введите любое число от 3 до 20: "))
    result = search_pair_of_numbers(value_)

    if result == 0:
        print(f"Число {value_} не входит в диапазон от 3 до 20")
        continue
        
    print(*result)
