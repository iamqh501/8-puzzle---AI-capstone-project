def X(v):
    return (v%3)+1
def Y(v):
    return v//3+1
def mat(s,x,y):  #convert from string configuration to matrix
    return s[x*3+y-4]
def check(s): #Check if s is solution
    return s == '123456789'
def nine(s): #Determine the place of the blank
    for i in range(9):
        if s[i] == '9':
            break
    return i
def Man(s): #Manhattan distance
    if s == '':
        return 36
    t = 0
    for i in range(9):
        t+= abs(X(i)-X(s[i])) +abs(Y(i)-Y(s[i]))
    return t
def gen(s):
    up = ''
    do = ''
    le = ''
    ri = ''
    if X(t) != 1:
        for i in range(9):
            if i == t:
                up += s[t-3]
            elif i == t-3:
                up += s[t]
            else:
                up += s[i]
    if X(t) != 3:
        for i in range(9):
            if i == t:
                do += s[t+3]
            elif i == t+3:
                do += s[t]
            else:
                do += s[i]
    if Y(t) != 1:
        for i in range(9):
            if i == t:
                le += s[t-1]
            elif i == t-1:
                le += s[t]
            else:
                le += s[i]
    if Y(t) != 3:
        for i in range(9):
            if i == t:
                le += s[t+1]
            elif i == t+1:
                le += s[t]
            else:
                le += s[i]
    return (up,do,le,ri)
def loop():
    pass
# Main
s = '916485372'
b = '123456789'
t = nine(s)
print(t)
print(s)
print(gen(s))



