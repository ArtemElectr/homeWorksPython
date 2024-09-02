from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding="utf-8") as file:

        for _ in range(1, word_count + 1):
            file.write(f"Какое-то слово № {_} \n")
            sleep(0.1)

    print(f'завершилась запись в файл {file_name}')

time_func_start = datetime.now()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_func_end = datetime.now()
time_run_func = time_func_end - time_func_start
print(f"Работа функций {time_run_func}")

thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

time_thr_start = datetime.now()

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_thr_end = datetime.now()
time_run_thr = time_thr_end - time_thr_start
print(f'Работа потоков {time_run_thr}')