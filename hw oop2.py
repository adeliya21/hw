class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_hw_grade(self):
        sum_hw = 0
        list_of_all_grades = []
        for x in self.grades.values():
            for y in x:
                sum_hw += y
                list_of_all_grades.append(y)
        avg_hw_grade = sum_hw / len(list_of_all_grades)
        return avg_hw_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за дз: {self.avg_hw_grade()}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.avg_hw_grade() < other.avg_hw_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_lecture_grade(self):
        sum_lecture = 0
        list_of_all_grades = []
        for x in self.grades.values():
            for y in x:
                sum_lecture += y
                list_of_all_grades.append(y)
        avg_lecture_grade = sum_lecture / len(list_of_all_grades)
        return avg_lecture_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_lecture_grade()}'
        return res

class Reviewier(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def avg_grade_of_students_in_this_course(student_list, course_name):
    sum_grade = 0
    list_of_all_grades = []
    for q in student_list:
        if course_name in q.courses_in_progress:
            for w in q.grades[course_name]:
                sum_grade += w
                list_of_all_grades.append(w)
    avg_grade_of_students_in_this_course = sum_grade / len(list_of_all_grades)
    return avg_grade_of_students_in_this_course

def avg_grade_of_lecturers_in_this_course(lecturers_list, course_name):
    sum_grade = 0
    list_of_all_grades = []
    for k in lecturers_list:
        if course_name in k.courses_attached:
            for t in k.grades[course_name]:
                sum_grade += t
                list_of_all_grades.append(t)
    avg_grade_of_lecturers_in_this_course = sum_grade / len(list_of_all_grades)
    return avg_grade_of_lecturers_in_this_course

student_1 = Student('Ruoy', 'Eman', 'your_gender_1')
student_1.courses_in_progress += ['Python']

student_2 = Student('Kelly', 'Rolla', 'your_gender_2')
student_2.courses_in_progress += ['Python', 'git']
student_2.finished_courses += ['введение в программирование']

lecturer_1 = Lecturer('lec_1', 'turer_1')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('lec_2', 'turer_2')
lecturer_2.courses_attached += ['Python', 'git']

reviewer_1 = Reviewier('rev_1', 'iewer_1')
reviewer_1.courses_attached += ['Python', 'git']

reviewer_2 = Reviewier('rev_2', 'iewer_2')
reviewer_2.courses_attached += ['Python', 'git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)

reviewer_1.rate_hw(student_2, 'git', 8)
reviewer_1.rate_hw(student_2, 'git', 8)
reviewer_1.rate_hw(student_2, 'git', 8)

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'Python', 10)

student_1.rate_lecture(lecturer_2, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Python', 10)
student_1.rate_lecture(lecturer_2, 'git', 9) #этой оценки нет, тк student_1 не проходит курс git
student_2.rate_lecture(lecturer_2, 'git', 8)
student_2.rate_lecture(lecturer_2, 'git', 7)

print(f'{student_1.name} {student_1.surname} {student_1.grades}')
print(f'{student_2.name} {student_2.surname} {student_2.grades}')
print('')

print(f'{lecturer_1.name} {lecturer_1.surname} {lecturer_1.grades}')
print(f'{lecturer_2.name} {lecturer_2.surname} {lecturer_2.grades}')
print('')

print(student_1)
print('')
print(student_2)
print('')
print(f'Is avg grade of {student_1.name} {student_1.surname} > avg grade of {student_2.name} {student_2.surname}?')
print(f'Answer: {student_1.avg_hw_grade() > student_2.avg_hw_grade()}')
print('')

print(lecturer_1)
print('')
print(lecturer_2)
print('')
print(f'Is avg grade of {lecturer_1.name} {lecturer_1.surname} > avg grade of {lecturer_2.name} {lecturer_2.surname}?')
print(f'Answer: {lecturer_1.avg_lecture_grade() > lecturer_2.avg_lecture_grade()}')
print('')

print(reviewer_2)
print('')
print(reviewer_1)
print('')

list_of_students = [student_1, student_2] #как создать список из всех экземпляров класса Student? то что я сделала не будет удобно при большом количестве students
list_of_lecturers = [lecturer_1, lecturer_2] #как создать список из всех экземпляров класса Lecturer?

#print(f'Cр.оц за дз по всем студентам в рамках курса Python: {av_grade_of_students_in_this_course(list_of_students, 'Python')}') #почему так не работает?
print('avg grade of students in python')
print(avg_grade_of_students_in_this_course(list_of_students, 'Python'))
print('')
print('avg grade of students in git')
print(avg_grade_of_students_in_this_course(list_of_students, 'git'))
print('')
print('avg grade of lecturers in python')
print(avg_grade_of_lecturers_in_this_course(list_of_lecturers, 'Python'))
print('')
print('avg grade of lecturers in git')
print(avg_grade_of_lecturers_in_this_course(list_of_lecturers, 'git'))