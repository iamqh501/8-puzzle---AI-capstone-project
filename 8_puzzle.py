# -*- coding: utf-8 -*-
from copy import deepcopy
import itertools

class Node(object):
    def __init__(self, state, action='', depth=0, parent=None, cost=0):
        self.s = state
        self.s_int = int(''.join(''.join(str(i) for i in row) for row in state))
        self.c = cost
        self.d = depth
        self.a = action
        self.p = parent

    def get_state(self):
        return deepcopy(self.s)
    def get_intState(self):
        return self.s_int
    def get_parent(self):
        return deepcopy(self.p)
    def get_action(self):
        return self.a
    def get_depth(self):
        return self.d
    def get_cost(self):
        return self.c
    def set_cost(self, value):
        self.c = value

    def has_gone(self):
        '''check whether the state has gone in all node on that track
        return True or False'''
        if not self.get_depth():
            return False
        if self.get_intState() == self.get_parent().get_intState():
            return True
        return self.get_parent().has_gone()

    def get_coordinate(self, num):
        '''return the coordinate of the number in matrix'''
        for i, j in itertools.product(range(3), repeat=2):
            if self.s[i][j] == num:
                return i, j

    def man_distance(self, other):
        man = 0
        for i, j in itertools.product(range(3), repeat=2):
            value = self.get_state()[i][j]
            if value != 0:
                x, y = other.get_coordinate(value)
                man += abs(i-x) + abs(j-y)
        return man

    def SuccessorFn(self):
        ''' return a list of (action,result) - the list of all possible action
        and corresponding result based on current state of node'''
        result = []
        actions = ('up', 'down', 'left', 'right')
        i, j = self.get_coordinate(0)
        toGo_position = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
        for a, (x, y) in zip(actions, toGo_position):
            if x in range(3) and y in range(3):
                s = self.get_state()
                s[i][j], s[x][y] = s[x][y], s[i][j]
                result.append((a, s))
        return result

    def Expand(self, goalNode):
        '''return a list of its successors'''
        global Tracker
        successors = []
        for action, state in self.SuccessorFn():
            newNode = Node(state, action, self.get_depth() + 1, self)
            cost = newNode.man_distance(goalNode) + newNode.get_depth()
            newNode.set_cost(cost)
            successors.append(newNode)
            Tracker.addNode()
        return successors

    def delete(self):
        global Tracker
        Tracker.delNode()
        del(self)

################
## ALGORITHMS ##
################

def Greedy(initNode, goalNode):
    global Tracker
    fringe = [initNode]
    while True:
        node_to_expand = min(fringe, key = lambda x: x.get_cost())
        fringe.remove(node_to_expand)
        if node_to_expand.get_intState() == goalNode.get_intState():
            return node_to_expand
        fringe.extend(node_to_expand.Expand(goalNode))

def Recursive_DLS(Node, limit, goalNode, gone_state):
    '''recursive function of Depth Limited Search
    return solution node, False or None - cutoff'''
    if Node.get_intState() == goalNode.get_intState(): return Node
    if Node.get_depth() == limit: return None
    has_cutoff = False
    gone_state.append(Node.get_intState())
    for successor in Node.Expand(goalNode):
        if successor.get_intState() not in gone_state:
            result = Recursive_DLS(successor,limit,goalNode,gone_state)
            if result: return result
            if result == None:
                has_cutoff = True
                successor.delete()
    if has_cutoff:
        Node.delete()
        return None
    return False

def Iterative_Deepening(initNode, goalNode):
    for depth in itertools.count():
        result = Recursive_DLS(initNode, depth, goalNode,[])
        if result != None:
            return result

###############
## DEBUGGING ##
###############

class Tracker(object):
    def __init__(self, time = 0, space = 0):
        '''
        Time complexity (number of nodes expanded)
        Space complexity (number of nodes kept in memory)
        '''
        self.time = time
        self.space = space
    def addNode(self,number = 1):
        self.time += number
        self.space += number
    def delNode(self,number = 1):
        self.space -= number
    def __str__(self):
        return 'Time complexity (number of nodes expanded): %i \nSpace complexity (number of nodes kept in memory): %i' %(self.time,self.space)

# Check whether problem is solvable
def inversions(s):
    '''Calculate total inversions of state'''
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
def solvable(gstate, s):
    return not (inversions(gstate) - inversions(s)) % 2

def print_state(node):
    i,j = node.get_coordinate(0)
    s = node.get_state()
    s[i][j] = ' '
    print('\n-+-+-\n'.join('|'.join(str(i) for i in row) for row in s))

def Print_solution(node):
    if not node.get_depth():
        print_state(node)
        print('----------------------------')
        return
    Print_solution(node.get_parent())
    print('Go ' + node.get_action())
    print_state(node)
    print('----------------------------')

def Search(algoFn):
    global Tracker
    if solvable(goal,start):
        initNode, goalNode = Node(start), Node(goal)
        Tracker.addNode(2)
        solNode = algoFn(initNode, goalNode)
        if solNode:
            Print_solution(solNode)
        print(Tracker)
    else:
        print('Unsolvable')

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state
start = [[0, 1, 6], [4, 8, 5], [3, 7, 2]]

#Search using Greedy and Iterative_Deepening algorithm
Tracker = Tracker()
Search(Greedy)
