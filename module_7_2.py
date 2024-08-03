def custom_write(file_name, strings):
    strings_positions = dict()
    count_string = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        count_string += 1
        start_byte = file.tell()
        file.write(f'{string}\n')
        strings_positions.update({tuple((count_string, start_byte)): string})
    file.close()

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)