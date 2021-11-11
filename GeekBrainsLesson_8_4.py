# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
# выбрасывать исключение ValueError, если что-то не так, например: def val_checker... ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
#
# Примечание: сможете ли вы замаскировать работу декоратора?

# ----------Решение-------------


def val_checker(function):
    def _val_checker(func):
        def wrapper(*args):
            markup = func(*args)
            if not function(int(args[0])):
                raise ValueError(f" Wrong val! For func '{func.__name__}' with argument: {int(args[0])}")
            return markup

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


# Проверяем
print(calc_cube(5))

try:
    print(calc_cube(-5))
except Exception as e:
    print(e)
