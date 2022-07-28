from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, mentor, course, grade):
        if isinstance(mentor, Mentor) and grade in range(11):
            if course in mentor.grade_lec:
                mentor.grade_lec[course] += [grade]
            else:
                mentor.grade_lec[course] = [grade]
        else:
            return 'Ошибка'        

    def avg_grade(self, grades):
        avg_grade_in_cours = 0
        if len(self.grades) > 0:
            for grade in self.grades.values():
                avg_grade_in_cours += mean(grade)
            avg_grade_all = round(avg_grade_in_cours/len(self.grades), 2)
        else:
            avg_grade_all = 'Оценки отсутствуют'
        return avg_grade_all
        
# Магия сравнения (студенты)
    def __lt__(stud_1, stud_2):
        if not isinstance(stud_1, Student) and isinstance(stud_2, Student):
            print('Студент не найден')
            return
        return stud_1.avg_grade(stud_1) > stud_2.avg_grade(stud_2)

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.avg_grade(self)}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
         
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_lec = {}

    def avg_grade(self, grade_lec):
        avg_grade_in_cours = 0
        if len(self.grade_lec) > 0:
            for grade in self.grade_lec.values():
                avg_grade_in_cours += mean(grade)
            avg_grade_all = avg_grade_in_cours/len(self.grade_lec)
        else:
            avg_grade_all = 'Оценки отсутствуют'
        return avg_grade_all

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.avg_grade(self)}'''
        return res

# Магия сравнения (лекторы)
    def __lt__(lector_1, lector_2):
        if not isinstance(lector_1, Lecturer) and isinstance(lector_2, Lecturer):
            print('Лектор не найден')
            return
        return lector_1.avg_grade(lector_1) > lector_2.avg_grade(lector_2)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}'''
        return res

best_student = Student('Konnov', 'Dmitriy', 'Man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
student_2 = Student('Ruoy', 'Eman', 'Man')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['GIT']

lecturer_1 = Lecturer('Ivan', 'Lecturer')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['GIT']
lecturer_2 = Lecturer('Boris', 'Lecturer')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['GIT']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['GIT']
reviewer_2 = Reviewer('Best', 'Reviewer')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['GIT']

best_student.rate_lecturer(lecturer_1, 'Python', 10)
best_student.rate_lecturer(lecturer_1, 'GIT', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'GIT', 6)

reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'GIT', 9)
reviewer_1.rate_hw(best_student, 'GIT', 9)
reviewer_1.rate_hw(best_student, 'GIT', 10)

reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'Python', 4)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'GIT', 5)
reviewer_2.rate_hw(student_2, 'GIT', 6)
reviewer_2.rate_hw(student_2, 'GIT', 7)


# Информация по студентам, проверяющим и лекторам
# print(best_student)
# print(student_2)
# print(reviewer_1)
# print(reviewer_2)
# print(lecturer_1)
# print(lecturer_2)

# Информация по студентам, проверяющим и лекторам
print(f'''Информация о студентах:
{best_student}
{student_2}

Информация о проверяющих:
{reviewer_1}
{reviewer_2}

Информация о лекторах:
{lecturer_1}
{lecturer_2}''')

list_courses = ['Python', 'GIT']
# Средняя оценка за курс по ученикам
def all_avg_grade_student(list_, cours_):
    grades = []
    for student in list_:
        for grade in student.grades.get(cours_):
            grades.append(grade)
            avg = mean(grades)
    print(f'Средня оценка за курс {cours_} по всем студентам: {avg}')
    return
list_student = [best_student, student_2]
all_avg_grade_student(list_student, 'Python')

# Средняя оценка за курс по лекторам
def all_avg_grade_lecturer(list_, cours_):
    grades = []
    for lecturer in list_:
        for grade in lecturer.grade_lec.get(cours_):
            grades.append(grade)
            avg = mean(grades)
    print(f'Средня оценка за курс {cours_} по всем лекторам: {avg}')
    return
list_lecturer = [lecturer_1, lecturer_2]
all_avg_grade_lecturer(list_lecturer, 'Python')

# Магия сравнения (лекторы)
print()
print (lecturer_2.__lt__(lecturer_1))
print(lecturer_1 < lecturer_2)


# Магия сравнения (студенты)
print()
print (best_student.__lt__(student_2))
print(student_2 < best_student)