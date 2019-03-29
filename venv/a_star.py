class Vertex():
    def __init__(self, parent=None, positionOf=None):

        self.H = 0
        self.G = 0
        self.F = 0
        self.positionOf = positionOf
        self.parent = parent
    def __eq__(self, other):
        return self.positionOf == other.positionOf
def a_star(map, begin, goal):

    # Create begin and goal vertices
    begin_node = Vertex(None, begin)
    begin_node.G = begin_node.H = begin_node.F = 0
    goal_node = Vertex(None, goal)
    goal_node.G = goal_node.H = goal_node.F = 0

    # Initializing open and closed lists
    open = []
    closed = []
    open.append(begin_node)
    while len(open) > 0:
        current = open[0]
        indexOfCurrent = 0
        for i, elements in enumerate(open):
            if elements.F < current.F:
                current = elements
                indexOfCurrent = i

        open.pop(indexOfCurrent)
        closed.append(current)

        # Findind goal state
        if current == goal_node:
            route = []
            current = current
            while current is not None:
                route.append(current.positionOf)
                current = current.parent
            return route[::-1]
        # Generate child_array
        child_array = []
        for updated_positions in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # all neighbor square
            position_node = (current.positionOf[0] + updated_positions[0], current.positionOf[1] + updated_positions[1])
            if position_node[0] > (len(map) - 1) or position_node[0] < 0 or position_node[1] > (len(map[len(map)-1]) -1) or position_node[1] < 0:
                continue
            if map[position_node[0]][position_node[1]] != 0:
                continue
            newNode = Vertex(current, position_node)
            child_array.append(newNode)
        for child in child_array:
            for seen_child in closed:
                if child == seen_child:
                    continue
            # Create the F, G,H
            child.G = current.G + 1
            child.H = ((child.positionOf[0] - goal_node.positionOf[0]) ** 2) + ((child.positionOf[1] - goal_node.positionOf[1]) ** 2)
            child.F = child.G + child.H

            for open_vertex in open:
                if child == open_vertex and child.G > open_vertex.G:
                    continue
            open.append(child)
def main():

    map = [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    begin = (0, 0)
    goal = (5, 9)

    route = a_star(map, begin, goal)
    print(route)

if __name__ == '__main__':
    main()
