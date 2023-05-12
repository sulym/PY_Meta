import os # Импортирует модуль os для работы с операционной системой.
import re # Импортирует модуль re для работы с регулярными выражениями.


# Функция get_last_number(), которая принимает строку line,
# находит последнее число в этой строке с помощью регулярного выражения,
# и возвращает его в виде целого числа.
def get_last_number(line: str) -> int:
    return int(re.findall(r'\d+', line)[-1])


with open('File_name', 'r') as file: # Открывает файл ttt для чтения, используя контекстный менеджер with.
    lines = file.readlines() # Читает все строки из файла ttt и сохраняет их в список lines.
    
# Cортирует список lines с помощью функции sorted() и ключа сортировки get_last_number(),
# Cохраняет отсортированный список строк в sorted_lines.
sorted_lines = sorted(lines, key=get_last_number)

with open('File_name', 'w') as file: #  Oткрывает файл ttt для записи.
    file.writelines(sorted_lines) # Записывает все строки из списка sorted_lines в файл ttt.
