import copy

class Node:
    def __init__(self, state, cost, blank, depth, parent):
        self.s = state
        self.c = cost
        self.d = depth

    def get_state(self):
        return self.s

    def get_coordinate(self,num):
        for i in range(3):
            for j in range(3):
                if self.s[i][j] == num:
                    return i, j

    def __eq__(self, other):
        return True if self.s == other.s else False

    def man_distance(self,other):
        man = 0
        for i in range(3):
            for j in range(3):
                value = self.get_state()[i][j]
                if value != 0:
                    x,y = other.get_coordinate(value)
                    man += abs(i-x) + abs(j-y)
        return man

def inversions(s):  # Calculate total inversions of state
    t = 0
    for i in range(3):
        for j in range(3):
            k = s[i][j]
            for w in range(j+1,3):
                if k > s[i][w] and s[i][w]:
                    t+=1
            for q in range(i+1,3):
                for w in range(3):
                    if k > s[q][w] and s[q][w]:
                        t+=1
    return t

def solvable(gstate, s):  # Check if problem is solvable
    return not (inversions(gstate) - inversions(s)) % 2

def nod(s, x, y, X, Y):
    ss = copy.deepcopy(s.st)
    ss[x][y] = ss[X][Y]
    ss[X][Y] = 0
    node = Node(ss, man(gstate, ss) + s.de + 1, (X, Y), s.de + 1, s.st)
    return node

def add(lis, nod):  # Add generated node to list and delete repeated state
    t = 1
    for i in range(len(lis)):
        if nod.st == lis[i].st:
            if lis[i].co > nod.co:
                lis.pop(i)
            else:
                t = 0
            break
    if t:
        lis.append(nod)
    return t == 1

def gen(s, listnode):  # Generate next nodes
    global ex
    x = s.bl[0]
    y = s.bl[1]
    if x != 0:
        ex += 1
        add(listnode, nod(s, x, y, x-1, y))
    if x != 2:
        ex += 1
        add(listnode, nod(s, x, y, x+1, y))
    if y != 0:
        ex += 1
        add(listnode, nod(s, x, y, x, y-1))
    if y != 2:
        ex += 1
        add(listnode, nod(s, x, y, x, y+1))
    listnode.sort(key=lambda x: x.co)  # sort nodes by the ascending of cost

def expand(listnode, successor):  # Expand next node which has lowest cost
    gen(successor[-1], listnode)
    nod = listnode[0]
    while not add(successor, nod):
        listnode.pop(0)
        nod = listnode[0]
    else:
        listnode.pop(0)

def sol(successor):  # Print sequence of moves
    l = len(successor)
    t = successor[l - 1]
    sol = [t]
    for i in range(l - 1):
        if t.pa == successor[l - i - 2].st:
            t = successor[l - i - 2]
            sol.append(t)
    sol.reverse()
    for i in range(len(sol)):
        print(sol[i].st)

# Main

# Test here: https://deniz.co/8-puzzle-solver/
gstate = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state
ss = [[0, 1, 6], [4, 8, 5], [3, 7, 2]]  # 016485372 Depth: 18 Iteration: 162 Expanded: 163 / 163 Frontier: 103 / 103
# ss = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]  # 123456708
# ss = [[1, 2, 3], [0, 8, 7], [6, 5, 4]]  # 123087654 Depth: 15 Iteration: 106 Expanded: 106 / 106 Frontier: 68 / 69
# ss = [[5, 2, 0], [8, 7, 6], [4, 3, 1]]  # 520876431 Depth: 22 Iteration: 823 Expanded: 823 / 823 Frontier: 473 / 474
# ss = [[0, 3, 2], [1, 7, 6], [8, 4, 5]]  # 032176845 Depth: 22 Iteration: 1972 Expanded: 1972 / 1972 Front: 1138 / 1139

if solvable(gstate, ss):
    s = Node(ss, man(gstate, ss), blank(ss), 0, [])  # Initial node
    ex = 0  # number of nodes expanded
    listnode = []  # List of next nodes
    successor = [s]  # Nodes went through

    while not check(successor[-1].st,gstate):
        expand(listnode, successor)

    sol(successor)
    print('Depth = ', successor[-1].de)
    print('Memory = ', len(listnode)+len(successor))
    print('Node expanded = ', ex)
else:
    print('Unsolvable')
