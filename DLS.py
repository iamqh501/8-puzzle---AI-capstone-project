class Node:
    def __init__(self, state, parent, action, cost, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

class Puzzles:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
    def actions(self, state):
        actions = []
        i, j = self.blank(state)
        def swap(row, col):
            state[i][j], state[row][col] = state[row][col], state[i][j]
            return state

        if i in range(1, 3):
            actions.append(('up', swap(i - 1, j)))
        elif i in range(2):
            actions.append(('down', swap(i + 1, j)))
        elif j in range(1, 3):
            actions.append(('left',swap(i, j - 1)))
        elif j in range(2):
            actions.append(('right',swap(i, j + 1)))
        return actions

    def expand(self, node):
        successors = []
        for action, result in self.actions(node.state):
            s = Node(state = result, parent = node, action = action, cost = node.cost + 1, depth = node.depth + 1)
        return successors

    def solution(self, node):

        actions = []
        cells = []
        cost = node.cost
        while node.parent is not None:
            actions.append(node.action)
            cells.append(node.state)
            node = node.parent
        actions.reverse()
        cells.reverse()

        print(actions)
        print(cells)
        print(cost)

    def IDDFS(self):
        import itertools
        def DLS(node, limit):
            #cutoff_occured = False
            if node.state == self.goal:
                return self.solution(node)
            elif node.depth == limit:
                return None
            else:

                for successor in self.expand(node):
                    if successor.state not in expored:
                        explored.append(successor.state)
                    result = DLS(successor, limit)
                    if result != None:
                        if result != False:
                            return result
                        else:
                            return False

        start = Node(state=self.start, parent=None, action=None,cost = 0, depth=0)
        for depth in itertools.count():
            explored = []
            result = DLS(start, depth)
            print(explored)
            if result != None:
                return result
    





initial_state = [[1, 7, 8], [6, 3, 2], [5, 4, 0]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# Puzzles(initial_state, goal).IDDFS()
print('\n'.join(' '.join(str(i) for i in row) for row in goal))




