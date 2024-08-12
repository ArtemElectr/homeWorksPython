def all_variants(text):
    count = 1
    current_len = len(text)

    while not count > len(text):
        for _ in range(current_len):
            yield text[_:_+count]
        count += 1
        current_len -= 1


a = all_variants("abc")
for i in a:
    print(i)
