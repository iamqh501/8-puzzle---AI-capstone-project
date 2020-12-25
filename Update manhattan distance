# Updated manhattan distance
def man(gstate,state):
    d = 0
    for i in range(3):
        for j in range(3):
            if gstate[i][j] != 0:
                m = man2(gstate[i][j],state)
                d+= abs(i-m[0])+abs(j-m[1])
    return d

def man2(n,state):
    for i in range(3):
        for j in range(3):
            if n == state[i][j]:
                return (i,j)

# The old one
def Man(s):  # Calculate Manhattan distance
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != 0:
                d += abs(i-(s[i][j]-1)//3) + abs(j-(s[i][j]-1) % 3)
    return d

gstate = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#gstate = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
#state = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
state = [[0, 1, 6], [4, 8, 5], [3, 7, 2]]
print(man(gstate,state))
print(Man(state))
# Same result :))
