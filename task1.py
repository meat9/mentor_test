class StackBracket:

    """
    Класс проверки корректности скобочных последовательностей
    реализован в виде стека.
    Методы:
        _push         - добавление элемента в стек
        _pop          - извлечение элемента из стека
        _clear        - очистка стека
        check_string  - проверка скобочной последовательности на корректность
    Свойство:
        _is_empty     - проверка стека на пустоту
    Методы реализованы защищенными (кроме check_string), т.к. использование подразумевается внутреннее (системное)

    Логика работы метода check_string:
        Перебор строки посимвольно. 
        При получении открывающейся скобки - кладём её в стек. 
        При получении закрывающейся - убираем из стека ранее положенную скобку.
        Если нужно убрать скобку из стека, а их там больше не осталось - последовательность неправильная. 
        Если после разбора строки в стеке остались лишние скобки - последовательность неправильная. 
        Если попался символ не похожий на скобку - последовательность не правильная
        Во всех остальных случаях - правильная.
    """

    def __init__(self) -> None:
        self._stack: list[str] = []

    def _pop(self) -> str:
        """
        Метод для извлечение элемента из стека.

        :return: последний элемент стека
        """
        return self._stack.pop()

    def _push(self, value: str) -> None:
        """
        Метод для добавления элемента в стек.
        """
        self._stack.append(value)

    def _clear(self) -> None:
        """
        Метод для полной очистки стека.
        """
        self._stack = []

    @property
    def _is_empty(self) -> bool:
        """
        Метод проверки стека на пустоту.

        :return: True если стек пустой, False, если нет
        """
        return not self._stack

    def check_string(self, code: str) -> bool:
        """
        Метод для проверки корректности скобочных последовательностей

        :param str code: Строка для проверки
        :return: True если последовательность корректная, False, в иных случаях
        """

        # Проверка основывается на двух кротежах открытых и закрытых скобок
        # кортежи "смежные", т.е. индексы пар скобок соответствуют друг другу
        el_open = ("(", "{", "[")
        el_close = (")", "}", "]")

        # Обходим полученную строку
        for el in code:

            # если элемент является открытой скобкой - кладем его в стек
            if el in el_open:
                self._push(el)

            # если элемент является закрытой скобкой:
            elif el in el_close:

                try:
                    # извлекаем последний добавленный элемент
                    poped_elem = self._pop()

                    # сравним значения по индексам элементов
                    # если они не равны - ошибка.
                    found_index = el_open.index(poped_elem)
                    if el != el_close[found_index]:
                        return False

                # отловим ошибку, если стек еще/уже пуст
                except IndexError:
                    return False

            # если в строке есть значение отличное от
            # скобок из кортежей - очистим стек и выйдем.
            else:
                self._clear()
                return False

        # если последовательнсть корректная - в стеке должно быть пусто.
        # вернем результат работы проверки стека на "пустоту"
        return self._is_empty


if __name__ == '__main__':
    bracket = StackBracket()                    # инициализируем пустой стек
    print(bracket.check_string("((((ы))))"))    # проверим не корректную последовательность
    print(bracket.check_string("(((())))"))     # проверим корректную последовательность
    print(bracket.__dict__)                     # выведем содержимое стека
    print(bracket.check_string("(((()"))        #
    print(bracket.__dict__)                     # выведем содержимое стекаv
