from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for word_number in range(word_count + 1):
            file.write(f'Какое-то слово № {word_number}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


non_thread_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

non_thread_end = datetime.now()

first_thread = Thread(target=write_words, args=(10, 'example5.txt'))
second_thread = Thread(target=write_words, args=(30, 'example6.txt'))
third_thread = Thread(target=write_words, args=(200, 'example7.txt'))
forth_thread = Thread(target=write_words, args=(100, 'example8.txt'))

thread_start = datetime.now()

first_thread.start()
second_thread.start()
third_thread.start()
forth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
forth_thread.join()

thread_end = datetime.now()

print(f'Без потоков затрачено времени: {non_thread_end - non_thread_start}\n'
      f'С потоками затрачено времени: {thread_end - thread_start}')

