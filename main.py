from Graph import Graph

# graph = {'1': {'2': 10, '3': 6, '4': 8},
#          '2': {'4': 5, '5': 13, '7': 11},
#          '3': {'5': 3},
#          '4': {'3': 2, '5': 5, '6': 7, '7': 12},
#          '5': {'6': 9, '9': 12},
#          '6': {'8': 8, '9': 10},
#          '7': {'6': 4, '8': 6, '9': 16},
#          '8': {'9': 15},
#          '9': {}}

if __name__ == "__main__":
    g = Graph()
    g.read_file("./graph.matrix")

    vtx1 = input("start : ")
    vtx2 = input("end : ")

    path, _ = g.dijkstra(vtx1, vtx2)

    for i, node in enumerate(path):
        if (len(path) - 1 == i):
            print(f"{node}")
        else:
            print(f"{node} -> ", end="")
