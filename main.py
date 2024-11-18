def sequence_number(number: int) -> str:
    '''
    Возвращает строку из первых элементов последовательности,
    где каждая цифра i повторяется i раз.
    '''
    sequence = ''

    if number == 0:

        return 'Число должно быть > 0'

    for i in range(1, number + 1):
        sequence += str(i) * i

    return sequence


if __name__ == '__main__':
    n = int(input('Введите число n: '))
    print(sequence_number(n))
