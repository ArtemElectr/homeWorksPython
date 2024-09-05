import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            row = file.readline()
            if not row:
                break
            all_data.append(row)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

time_start = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
time_end = datetime.datetime.now()
print(time_end - time_start)


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        time_start = datetime.datetime.now()
        pool.map(read_info, filenames)

    time_end = datetime.datetime.now()
    print(time_end - time_start)