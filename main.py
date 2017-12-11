#!/usr/bin/env python
# -*- coding: utf-8 -*


import sys
from Queue import *


def neighbours(d, word):
    neighs = []

    for i in range(len(word)):
        bucket = word[:i] + '_' + word[i + 1:]
        for j in d[bucket]:
            if j != word:
                neighs.append(j)

    return neighs


def heuristic(obj1, obj2):
    result = 0

    for i in range(len(obj1)):
        if obj1[i] != obj2[i]:
            result += 1

    return result


def build_graph(begin, end, dict):
    d = {}
    flag = 0
    input_file = open(dict, 'r')

    # "корзины", состоящие из слов, отличающихся на 1 символ
    for line in input_file:
        if len(line) - 1 == len(begin):
            word = line[:-1]
            if word == begin or word == end:
                flag += 1
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

    # проверка, что оба входных слова есть в словаре
    if flag != 2:
        return -1

    return d


def find_path(graph, begin, end):
    # текущая граница рассматриваемых элементов
    frontier = PriorityQueue()
    frontier.put((0, begin))

    # сохранение предыдущих элементов (для построения пути)
    previous = {}
    previous[begin] = None

    # стоимость от начала до рассматриваемого элемента
    all_cost = {}
    all_cost[begin] = 0

    flag = False

    while not frontier.empty():

        current_tuple = frontier.get()
        current = current_tuple[1]

        if current == end:
            flag = True
            break

        for next in neighbours(graph, current):

            new_cost = all_cost[current] + 1
            if next not in all_cost:
                all_cost[next] = new_cost

            if all_cost[current] + 1 > all_cost[next]:
                continue

            priority = new_cost + heuristic(next, end)
            frontier.put((priority, next))
            previous[next] = current

    # не дошли до искомого элемента (пути нет)
    if not flag:
        return -1

    current = end
    path = [current]

    while current != begin:
        current = previous[current]
        path.append(current)

    path.reverse()

    return path


def main_script(input, output):
    input_file = open(input)
    output_file = open(output, 'w')

    dictionary = "./dict_preparation/dict.txt"

    for line in input_file:
        begin = line.split()[0]
        end = line.split()[1]

        graph = build_graph(begin, end, dictionary)

        if graph != -1:
            steps = find_path(graph, begin, end)

            if steps != -1:
                result = ' '.join(str(word) for word in steps)

            else:
                result = str(-1)

        else:
            result = str(-1)

        output_file.write(result)


if __name__ == '__main__':
    main_script(sys.argv[1], sys.argv[2])

# main_script('input.txt', 'output.txt')