
from operator import itemgetter


class StudentGroup:
    """Студенческая группа"""

    def __init__(self, id, name, students_count, department_id):
        self.id = id
        self.name = name
        self.students_count = students_count
        self.department_id = department_id


class Department:
    """Кафедра"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class GroupDepartment:
    """Связь группы с кафедрой (многие ко многим)"""

    def __init__(self, group_id, department_id):
        self.group_id = group_id
        self.department_id = department_id


# Список кафедр
departments = [
    Department(1, 'Автоматизированные системы'),
    Department(2, 'Информационные технологии'),
    Department(3, 'Прикладная математика'),
    Department(4, 'Программная инженерия'),
]


# Список студенческих групп
groups = [
    StudentGroup(1, 'АИ-21', 25, 1),
    StudentGroup(2, 'ИУ5-24', 28, 2),
    StudentGroup(3, 'АИ-22', 22, 1),
    StudentGroup(4, 'ПМ-23', 19, 3),
    StudentGroup(5, 'ИУ5-25', 24, 2),
]


# Связь многие ко многим
groups_departments = [
    GroupDepartment(1, 1),
    GroupDepartment(1, 4),
    GroupDepartment(2, 2),
    GroupDepartment(2, 4),
    GroupDepartment(3, 1),
    GroupDepartment(4, 3),
    GroupDepartment(5, 2),
    GroupDepartment(5, 4),
]


def main():
    # Связь один ко многим
    one_to_many = [
        (g.name, g.students_count, d.name)
        for g in groups
        for d in departments
        if g.department_id == d.id
    ]

    # Связь многие ко многим
    many_to_many = [
        (g.name, d.name)
        for gd in groups_departments
        for g in groups
        for d in departments
        if gd.group_id == g.id and gd.department_id == d.id
    ]

    # Задание В1
    # Группы, название которых начинается на А
    print('Задание В1')

    result1 = [
        (name, dep)
        for name, count, dep in one_to_many
        if name.startswith('А')
    ]

    print(result1)

    # Задание В2
    # Минимальное количество студентов на каждой кафедре
    print('\nЗадание В2')

    result2 = []

    for d in departments:
        counts = [
            count
            for name, count, dep in one_to_many
            if dep == d.name
        ]

        if counts:
            result2.append((d.name, min(counts)))

    result2 = sorted(result2, key=itemgetter(1))

    print(result2)

    # Задание В3
    # Все связанные группы и кафедры
    # Сортировка по названию группы
    print('\nЗадание В3')

    result3 = sorted(many_to_many, key=itemgetter(0))

    print(result3)


if __name__ == '__main__':
    main()
