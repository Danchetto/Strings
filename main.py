#!/usr/bin/env python
# -*- coding: utf-8 -*


import sys
from Queue import *


class Graph():
    edges = []

    def add_edge(self, obj1, obj2):
        if not (obj1, obj2) in self.edges:
            self.edges.append((obj1, obj2))



    def neighbours(self, obj):
        neighs = []

        for pair in self.edges:
            if obj == pair[0]:
                neighs.append(pair[1])
            if obj == pair[1]:
                neighs.append(pair[0])

        return neighs



def heuristic(obj1, obj2):
    result = 0

    for i in range(len(obj1)):
        if obj1[i] != obj2[i]:
            result += 1

    return result



def build_graph(begin, end, dict):
    d = {}
    g = Graph()
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

    # построение графа
    for bucket in d.keys():
        for i in range(len(d[bucket])):
            for j in range(i + 1, len(d[bucket])):
                g.add_edge(d[bucket][i], d[bucket][j])
    return g



def find_path(graph, begin, end):
    # текущая граница рассматриваемых элементов
    frontier = PriorityQueue()
    frontier.put(begin)

    # сохранение предыдущих элементов (для построения пути)
    previous = {}
    previous[begin] = None

    # стоимость от начала до рассматриваемого элемента
    all_cost = {}
    all_cost[begin] = 0

    flag = False

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            flag = True
            break

        for next in graph.neighbours(current):
            new_cost = all_cost[current] + 1
            if next not in all_cost or new_cost < all_cost[next]:
                all_cost[next] = new_cost
                priority = heuristic(end, next) + new_cost
                frontier.put(next, priority)
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

    dictionary = "dict.txt"

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