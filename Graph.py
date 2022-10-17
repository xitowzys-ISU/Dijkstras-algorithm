import math


class GraphException(Exception):
    def __init__(self, text):
        self.txt = text


class Graph:
    def __init__(self):
        self.__graph: dict = {}

    def read_file(self, file: str):
        with open(file, "r") as file:
            readline = file.read().splitlines()

            matrix = []

            if(readline[0] == "AM"):
                edge_len = len(list(
                    map(int, filter(None, readline[1].replace(" ", "").split(",")))))

                for line in readline[1:]:
                    format_line = list(
                        map(int, filter(None, line.replace(" ", "").split(","))))

                    if edge_len != len(format_line):
                        raise GraphException(f"Неправильный размер матрицы")

                    matrix.append(format_line)
            else:
                raise GraphException(
                    f"Неправильный параметр матрицы -> {readline[0]}")

            for i_item, i in enumerate(matrix):

                node_dict = {}

                for j_item, j in enumerate(i):
                    if not j:
                        continue
                    else:
                        node_dict[str(1 + j_item)] = j

                self.__graph[str(i_item + 1)] = node_dict

    def get_graph(self):
        return self.__graph

    def dijkstra(self, start, goal):
        distance = {}
        predecessor = {}
        unseenNodes = self.__graph
        path = []

        for node in unseenNodes:
            distance[node] = math.inf
        distance[start] = 0

        while unseenNodes:
            minNode = None
            for node in unseenNodes:
                if minNode is None:
                    minNode = node
                elif distance[node] < distance[minNode]:
                    minNode = node

            for childNode, weight in self.__graph[minNode].items():
                if weight + distance[minNode] < distance[childNode]:
                    distance[childNode] = weight + \
                        distance[minNode]
                    predecessor[childNode] = minNode
            unseenNodes.pop(minNode)

        currentNode = goal

        while currentNode != start:
            try:
                path.insert(0, currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                raise GraphException("Путь недостижим")

        path.insert(0, start)

        if distance[goal] != math.inf:
            return path, distance
