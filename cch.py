from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Проверяет положительность значения и высчитывает корень."""
    required_number = CalculateSquareRoot(your_number)
    if your_number <= 0:
        return
    else:
        print(
            f'Мы вычислили квадратный корень из введённого вами числа.'
            f' Это будет: {required_number}')


print(message)
calc(25.5)
