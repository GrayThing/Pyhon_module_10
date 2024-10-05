from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    with open(name, 'r') as file:
        all_data = [line for line in file.readlines()]


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    mono_start = datetime.now()

    for file in filenames:
        read_info(file)

    mono_end = datetime.now()

    multi_start = datetime.now()

    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    multi_end = datetime.now()

    print(f'Линейный: {mono_end - mono_start}')
    print(f'Многопроцессный: {multi_end - multi_start}')