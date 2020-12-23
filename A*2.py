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
def gen(s,listnode): # Generate next node
    x = s.bl[0]
    y = s.bl[1]
    if x != 0:
        ss = copy.deepcopy(s.st)
        ss[x][y] = ss[x-1][y]
        ss[x-1][y] = 0
        nod = Node(ss,Man(ss)+s.de+1,(x-1,y),s.de+1,s.st)
        t = 1
        for i in range(len(listnode)):
            if nod.st == listnode[i].st:
                if listnode[i].co > nod.co:
                    listnode.pop(i)
                else: t = 0
                break
        if t: listnode.append(nod)
    if x != 2:
        ss = copy.deepcopy(s.st)
        ss[x][y] = ss[x+1][y]
        ss[x+1][y] = 0
        nod = Node(ss,Man(ss)+s.de+1,(x+1,y),s.de+1,s.st)
        t = 1
        for i in range(len(listnode)):
            if nod.st == listnode[i].st:
                if listnode[i].co > nod.co:
                    listnode.pop(i)
                else: t = 0
                break
        if t: listnode.append(nod)

    if y != 0:
        ss = copy.deepcopy(s.st)
        ss[x][y] = ss[x][y-1]
        ss[x][y-1] = 0
        nod = Node(ss,Man(ss)+s.de+1,(x,y-1),s.de+1,s.st)
        t = 1
        for i in range(len(listnode)):
            if nod.st == listnode[i].st:
                if listnode[i].co > nod.co:
                    listnode.pop(i)
                else: t = 0
                break
        if t: listnode.append(nod)
    if y != 2:
        ss = copy.deepcopy(s.st)
        ss[x][y] = ss[x][y+1]
        ss[x][y+1] = 0
        nod = Node(ss,Man(ss)+s.de+1,(x,y+1),s.de+1,s.st)
        t = 1
        for i in range(len(listnode)):
            if nod.st == listnode[i].st:
                if listnode[i].co > nod.co:
                    listnode.pop(i)
                else: t = 0
                break
        if t: listnode.append(nod)
    listnode.sort(key=lambda x: x.co)
def loop(s,listnode,successor):
    if not check(s.st):
        gen(s,listnode)
        nod = listnode[0]
        listnode.pop(0)
        successor.append(nod)
        # t = 0
        # while t == 0:
        #     t = 1
        #     for i in range(len(successor)):
        #         if nod.st == successor[i].st:
        #             if successor[i].co > nod.co:
        #                 successor.pop(i)
        #             else: t = 0
        #             break
        #     if t: successor.append(nod)
        #     listnode.pop(0)
        return 0
    else:
        return 1
#Main
#https://deniz.co/8-puzzle-solver/
ss = [[0,1,6],[4,8,5],[3,7,2]] #016485372 Depth: 18 Iteration: 162 Expanded nodes: 163 / 163 Frontier nodes: 103 / 103
#ss = [[1,2,3],[4,5,6],[7,0,8]] #123456708
#ss = [[1,2,3],[0,8,7],[6,5,4]] #123087654 Depth: 15 Iteration: 106 Expanded nodes: 106 / 106 Frontier nodes: 68 / 69
s = Node(ss,Man(ss),blank(ss),0,[])
listnode = []
successor = [s]
while loop(successor[len(successor)-1],listnode,successor) != 1:
    pass
# for i in range(len(successor)):
#     print(successor[i].st,successor[i].de)
# print(i)
l = len(successor)
t = successor[l - 1]
sol = [t]
for i in range(l-1):
    if t.pa == successor[l-i-2].st:
        t = successor[l - i - 2]
        sol.append(t)
sol.reverse()
for i in range(len(sol)):
    print(sol[i].st)
print('depth = ',i)