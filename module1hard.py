grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Jonny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()

dict = dict()
# 1 variant
dict.update({students[0]: sum(grades[0])/len(grades[0])})
dict.update({students[1]: sum(grades[1])/len(grades[1])})
dict.update({students[2]: sum(grades[2])/len(grades[2])})
dict.update({students[3]: sum(grades[3])/len(grades[3])})
dict.update({students[4]: sum(grades[4])/len(grades[4])})
print(dict)

# 2 variant
dict_ = {}
for i in range(0, len(grades)):
    dict_.update({students[i]: sum(grades[i]) / len(grades[i])})

print(dict_)
