import json
from unique import Unique
from print_result import print_result
from cm_timer import cm_time_1
from field import field
from gen_random import gen_random
import sys
# Сделаем другие необходимые импорт

path = "C:/Users/Ия/OneDrive/Рабочий стол/lab3/data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, 'job-name'), ignore_case=True)), key=lambda x: str.casefold(x))


@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x.lower(), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return dict((zip(arg, gen_random(len(arg), 100000, 200000))))


if __name__ == '__main__':
    with cm_time_1():
       f4(f3(f2(f1(data))))