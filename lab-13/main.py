import csv
import json
import os

CURRENT_DIR = os.path.dirname(__file__)

# функція для відкриття файлів з обробкою виключень
def Open(file_name, mode):
    
    file_path = os.path.join(CURRENT_DIR,file_name)
    
    try:
        file = open(file_path, mode, encoding="utf-8")
    except:
        print(f"Файл {file_name} не знайдено!")
        return None
    else:
        return file


# заголовки стовпців файла data.csv
CSV_FILE_FIELDNAMES = ["Прізвище", "Ім'я", "Середній бал"]

# Початкове заповнення файлу data.csv
csv_file = Open("data.csv", "w")

if csv_file != None:
    csv_writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=CSV_FILE_FIELDNAMES, lineterminator="\n")
    csv_writer.writeheader()
    csv_writer.writerow({CSV_FILE_FIELDNAMES[0]: "Петренко", CSV_FILE_FIELDNAMES[1]: "Іван", CSV_FILE_FIELDNAMES[2]: 72,})
    csv_writer.writerow({CSV_FILE_FIELDNAMES[0]: "Іванов", CSV_FILE_FIELDNAMES[1]: "Сергій", CSV_FILE_FIELDNAMES[2]: 80,})
    csv_writer.writerow({CSV_FILE_FIELDNAMES[0]: "Охрипенко", CSV_FILE_FIELDNAMES[1]: "Марія", CSV_FILE_FIELDNAMES[2]: 95,})
    csv_file.close()


#--- Воронко Ілля КН-35 ---

# відкриваємо файл data.csv на читання
csv_file = Open("data.csv", "r")

# відкриваємо файл data.json на запис
json_file = Open("data.json", "w")

if csv_file != None and json_file != None:
    
    csv_reader = csv.DictReader(csv_file, delimiter=";",)

    # формуємо список, кожен елемент якого є рядком файла data.csv, записаним у форматі словника
    items = [row for row in csv_reader]

    # записуємо отриманий список у файл data.json
    json.dump(items, json_file, ensure_ascii=False, indent=4, separators=(',',':'))

    # закриваємо обидва файла
    csv_file.close()
    json_file.close()
