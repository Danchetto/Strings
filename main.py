from Queue import *



class Graph():

    edges = []
    nodes = []

    def add_edge(self, obj1, obj2):

        if not obj1 in self.nodes:
            self.nodes.append(obj1)
        if not obj2 in self.nodes:
            self.nodes.append(obj2)

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
    input_file = open(dict,'r')
    # create buckets of words that differ by one letter
    for line in input_file:
        if len(line) - 1 == len(begin):
            word = line[:-1]
            if word == begin or word == end:
                flag += 1
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]


    if flag != 2:
        print "No such word in dictionary! Please, try again."
        return -1


    for bucket in d.keys():
        for i in range(len(d[bucket])):
            for j in range(i + 1, len(d[bucket])):
                g.add_edge(d[bucket][i], d[bucket][j])
    return g



def find_path(graph, begin, end):

    frontier = PriorityQueue()
    frontier.put(begin)
    previous = {}
    previous[begin] = None
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

    if not flag:
        print "Can't transform " + begin + " -> " + end
        return -1


    current = end
    path = [current]
    while current != begin:
        current = previous[current]
        path.append(current)
    # path.append(begin)
    path.reverse()

    return path



print("Enter first word: ")
begin = str(raw_input())
print("Enter second word: ")
end = str(raw_input())

dictionary = "dict.txt"

steps = -1

g = build_graph(begin, end, dictionary)

if g != -1:
    steps = find_path(g, begin, end)

if steps != -1:
    for word in steps:
        print word
