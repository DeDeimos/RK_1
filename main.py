# используется для сортировки
from operator import itemgetter


class Emp:
    """Студенческая группа"""

    def __init__(self, id, name, quan, dep_id):
        self.id = id
        self.name = name
        self.quan = quan
        self.dep_id = dep_id


class Dep:
    """Кафедра"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class EmpDep:
    """
    'Сотрудники отдела' для реализации
    связи многие-ко-многим
    """

    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id
        self.emp_id = emp_id


# Отделы
deps = [
    Dep(1, 'Системы обработки информации и управления'),
    Dep(2, 'Системы автоматического управления'),
    Dep(3, 'Проектирование и технология производства электронной аппаратуры'),
    Dep(4, 'Радиоэлектронные системы и устройства'),

]

# Сотрудники
emps = [
    Emp(1, 'РТ5-31Б', 27, 1),
    Emp(2, 'РТ4-31', 22, 2),
    Emp(3, 'РТ2-31', 21, 3),
    Emp(4, 'РТ1-31', 18, 4),
    Emp(5, 'ИУ5-32', 15, 1),
    Emp(6, 'ИУ5-31', 14, 1),
]

emps_deps = [
    EmpDep(1, 1),
    EmpDep(2, 2),
    EmpDep(3, 3),
    EmpDep(4, 4),
    EmpDep(1, 5),
    EmpDep(1, 6),

]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.name, e.quan, d.name)
                   for d in deps
                   for e in emps
                   if e.dep_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id)
                         for d in deps
                         for ed in emps_deps
                         if d.id == ed.dep_id]

    many_to_many = [(e.name, e.quan, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in emps if e.id == emp_id]

    print('Задание E1')
    # res_11 = sorted(one_to_many, key=itemgetter(2))
    res_11 = list(filter(lambda x: 'Системы' in x[2], one_to_many))
    print(res_11)

    print('\nЗадание E2')
    res = []
    for emp in emps:
        mid_res = []
        sum = 0
        count = 0
        for emp_dep in emps_deps:
            if emp_dep.ide_id == emp.id:
                for dep in deps:
                    if dep.id == emp_dep.language_id:
                        sum += dep.diificulity
                        count += 1
        try:
            mid_res.append(emp.name)
            mid_res.append(round(sum / count, 2))
            res.append(mid_res)
        except ZeroDivisionError:
            pass
    return sorted(res, key=itemgetter(1), reverse=False)

    print('\nЗадание E3')
    res_13 = {}
    # Перебираем все отделы
    for d in deps:
        if 'П' in d.name[1]:
            # Список сотрудников отдела
            d_emps = list(filter(lambda i: i[2] == d.name, many_to_many))
            # Только ФИО сотрудников
            d_emps_names = [x for x, _, _ in d_emps]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.name] = d_emps_names

    print(res_13)


if __name__ == '__main__':
    main()
