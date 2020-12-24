import copy
class Node:
    def __init__(self,st,co,bl,de,pa):
        self.st = st #state
        self.co = co #cost
        self.bl = bl #blank
        self.de = de #depth
        self.pa = pa #parent
def blank(s): #Find blank(0) position
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i,j
def check(s): #Check if the state is solution
    return s == [[1,2,3],[4,5,6],[7,8,0]]
def Man(s): #Calculate Mahattan distance
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != 0:
                d += abs(i-(s[i][j]-1)//3) + abs(j-(s[i][j]-1)%3)
    return d
def nod(s,x,y,X,Y):
    ss = copy.deepcopy(s.st)
    ss[x][y] = ss[X][Y]
    ss[X][Y] = 0
    node = Node(ss, Man(ss) + s.de + 1, (X, Y), s.de + 1, s.st)
    return node
def add(list,nod): #add generated node to list and delete repeated state
    t = 1
    for i in range(len(list)):
        if nod.st == list[i].st:
            if list[i].co > nod.co:
                list.pop(i)
            else:
                t = 0
            break
    if t: list.append(nod)
    return t == 1
def gen(s,listnode): # Generate next nodes
    global ex
    x = s.bl[0]
    y = s.bl[1]
    if x != 0:
        ex+=1
        add(listnode,nod(s,x,y,x-1,y))
    if x != 2:
        ex += 1
        add(listnode, nod(s,x,y,x+1,y))
    if y != 0:
        ex += 1
        add(listnode, nod(s,x,y,x,y-1))
    if y != 2:
        ex += 1
        add(listnode, nod(s,x,y,x,y+1))
    listnode.sort(key=lambda x: x.co) #sort nodes by the ascending of cost
def loop(s,listnode,successor): #Open next node which has lowest cost
    if not check(s.st):
        gen(s,listnode)
        nod = listnode[0]
        while not add(successor,nod):
            listnode.pop(0)
            nod = listnode[0]
        else: listnode.pop(0)
        return 0
    else:
        return 1
def sol(successor): #Print sequence of moves
    global i
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
#Main
#Test here: https://deniz.co/8-puzzle-solver/
ss = [[0,1,6],[4,8,5],[3,7,2]] #016485372 Depth: 18 Iteration: 162 Expanded nodes: 163 / 163 Frontier nodes: 103 / 103
#ss = [[1,2,3],[4,5,6],[7,0,8]] #123456708
#ss = [[1,2,3],[0,8,7],[6,5,4]] #123087654 Depth: 15 Iteration: 106 Expanded nodes: 106 / 106 Frontier nodes: 68 / 69
#ss = [[5,2,0],[8,7,6],[4,3,1]] #520876431 Depth: 22 Iteration: 823 Expanded nodes: 823 / 823 Frontier nodes: 473 / 474
#ss = [[0,3,2],[1,7,6],[8,4,5]] #032176845 Depth: 22 Iteration: 1972 Expanded nodes: 1972 / 1972 Frontier nodes: 1138 / 1139
s = Node(ss,Man(ss),blank(ss),0,[])
ex = 0 #number of nodes expanded
listnode = [] #List of next nodes
successor = [s] #Nodes went through
while loop(successor[-1],listnode,successor) != 1:
    pass
# for i in range(len(successor)):
#     print(successor[i].st,successor[i].de)
# print(i)
sol(successor)
print('Depth = ',i)
print('Memory = ',len(listnode)+len(successor))
print('Node expanded = ',ex)
