# початковий масив зі словниками 

group = {
    "groupNumber": "СУ-13",
    "course": 3,
    "students":[
        {
            "fullName":"Петренко Антон Федорович",
            "marks": {
                "ММДО": 100,
                "Чисельні методи": 60,
                "Програмування мовою Python": 60,
            }
        },
        {
            "fullName":"Мельник Олена Іванівна",
            "marks": {
                "ММДО": 80,
                "Чисельні методи": 80,
                "Програмування мовою Python": 90,
            }
        },
        {
            "fullName":"Андрієнко Петро Миколайович",
            "marks": {
                "ММДО": 60,
                "Чисельні методи": 80,
                "Програмування мовою Python": 75,
            }
        },
    ]
}


# ----Виконано студентом групи КН-35 Воронко І. І.----

# функція для обчислення середнього балу студента
def get_average_mark(student):
    return sum(student["marks"].values()) / len(student["marks"].values())

# функція для пошуку студента з найбільшим середнім балом
def get_student_with_max_average_mark(group):

    student_with_max_average_mark = group["students"][0]

    for student in group["students"]:
        if get_average_mark(student) > get_average_mark(student_with_max_average_mark):
            student_with_max_average_mark = student

    return student_with_max_average_mark


student = get_student_with_max_average_mark(group)
print("Студент з найбільшим середнім балом: ", student["fullName"])