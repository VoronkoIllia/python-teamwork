from os import path

#--- Воронко Ілля КН-35 (тімлід) ---

#функція що відкриває файл та обробляє винятки, що можуть виникнути в процесі відкриття файлу
def Open(file_name, mode):

    current_dir = path.dirname(__file__)
    file_path = path.join(current_dir, file_name)

    try:
        file = open(file_path, mode, encoding="utf-8")
    except:
        print(f"File {file_name} wasn't opened")
        return None
    else:
        print(f'File {file_name} was opened')
        return file

FILE_NAME = "output.txt"

file = Open(FILE_NAME, "w")

if file != None:
    file.write("Воронко Ілля КН-35\n")
    file.write("Які існують режими відкриття файлу та чим вони відрізняються?")
    file.write("\n")
    file.close()
    print(f"File {FILE_NAME} was closed!")