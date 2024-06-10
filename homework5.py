# 2)
immutable_var = 10, "June", True
print("Immutable tuple:", immutable_var)

# 3)
# immutable_var[0] = 2  # ERROR
# В кортежах нельзя изменять значения элементов, т.к кортеж относится к неизменяемым типам данных (как цифры со строками)

# 4)
mutable_list = [30, "Arseny", "student", False]
mutable_list[0] = 34
mutable_list[1] = "Artemy"
mutable_list[3] = True

print("Mutable list:", mutable_list)