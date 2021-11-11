# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
#
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):

    print(type(func))

    def type_logger(*args, **kwargs):
        args_and_kwargs = list(args) + list(kwargs.values())
        # Создаем кортеж из переменных и их описания
        types = tuple(map(lambda i: f'{i}: {type(i)}', args_and_kwargs))
        # Выводим на экран название функции и аргументов
        print(f'{func.__name__}{types}')
        orig_func = func(*args, **kwargs)
        return orig_func

    return type_logger


@type_logger
def calc_cubes(*args, **kwargs):
    # согдаем функцию расчета кубов аргументов
    # обьявьявляем пременную для результата
    result = []
    try:
        # Создаем блок try except и в нутри него проходимся по циклом по именованым и не именнованным аргументам
        for i in kwargs.values():
            result.append(i ** 3)
        for i in args:
            result.append(i ** 3)

        print(f'cubes is {result}')
    except Exception as e:
        print(e)

# Проверяем
calc_cubes(2, 3, a=4, b=5)