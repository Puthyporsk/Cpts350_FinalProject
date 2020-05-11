# Puthypor Sengkeo
# 011646389
# Cpts 350 - Final Exam

# Algorithm to solve the LD problem

# Q is a linear constraint e.g. 2X₁ - 3X₂ + 4 = 0 (Q is the all of the constraints)
# there are m constraints in Q (m are individual lines of constraints)
# Implement a graph composition algorithm to convert the m graphs into one final graph.
# Then perform basic graph search on the final graph to finally solve the LD problem.

# For this problem, we are dealing with Q with three variables X₁, X₂, X₃, and two constraints (m = 2)
# Being Diophantine, the variables are nonnegative integers

# Implement a function to return Cₘₐₓ
def findCMax(C1, C2, C3):
    d1 = d2 = d3 = d = 1
    if (C1 < 0):
        d1 = 0
    if (C2 < 0):
        d2 = 0
    if (C3 < 0):
        d3 = 0

    return (C1*d1 + C2*d2 + C3*d3 + d)

# Implement a functions to return Kc from a given contatn C >= 0
def findKC(C):
    if (C == 0):
        return 0
    else:
        b = '{:b}'.format(C)
        print("Binary representation of", C, "is", b)
        return len(b)

# Implment a function that returns the value bᵢ from a given constant C >= 0 and i; 1 <= i <= Kc + 1
def findBi(C, i):
    b = '{:b}'.format(C)
    b = ''.join(reversed(b))
    b += "0"
    counter = 0
    for x in b:
        counter+=1
        if (1 <= i) and (i <= (len(b) + 1)):
            if (counter == i):
                return int(x)

# Construct a FA M that contains exactly eight input symbols
# Each symbols is in the form of (a₁, a₂, a₃) with a₁, a₂, a₃ in {0,1}
# A state in M is a pair of values: [carry, i], where -Cₘₐₓ <= carry <= Cₘₐₓ
# Initial state M is [carry = 0, i = 1]
# Accepting state M is [carry = 0, i = Kc + 1]
def findM(C1, C2, C3, C, P, M):
    carry = 0
    i = 1
    carryPrime = 0
    iPrime = 1

    Cmax = findCMax(C1,C2,C3)
    print("Cmax =", Cmax)
    Kc = findKC(C)
    print("Kc =", Kc)

    # for i in range(1, Kc+2):
    #     carry = carryPrime
    L = []

    M[(carry, i)] = {}
    if (i >= Kc + 1):
        bi = 0
    else:
        bi = findBi(C,i)
    for a1,a2,a3 in P:
        R = C1*a1 + C2*a2 + C3*a3 + bi + carry
        if (R%2 == 0):
            carryPrime = int(R/2)
            if (1 <= i) and (i <= Kc):
                iPrime = i+1
            else:
                iPrime = i
            M[(carry, i)][(a1,a2,a3)] = (carryPrime, iPrime)
            L.append((carryPrime, iPrime))
    LL = []
    for x,y in L:
        carry = x
        i = y
        M[(carry, i)] = {}
        if (i >= Kc + 1):
            bi = 0
        else:
            bi = findBi(C,i)
        for a1,a2,a3 in P:
            R = C1*a1 + C2*a2 + C3*a3 + bi + carry
            if (R%2 == 0):
                carryPrime = int(R/2)
                if (1 <= i) and (i <= Kc):
                    iPrime = i+1
                else:
                    iPrime = i
                M[(carry, i)][(a1,a2,a3)] = (carryPrime, iPrime)
                LL.append((carryPrime, iPrime))
    LL = list(set(LL))
    LLL = []
    for x,y in LL:
        carry = x
        i = y
        M[(carry, i)] = {}
        if (i >= Kc + 1):
            bi = 0
        else:
            bi = findBi(C,i)
        for a1,a2,a3 in P:
            R = C1*a1 + C2*a2 + C3*a3 + bi + carry
            if (R%2 == 0):
                carryPrime = int(R/2)
                if (1 <= i) and (i <= Kc):
                    iPrime = i+1
                else:
                    iPrime = i
                M[(carry, i)][(a1,a2,a3)] = (carryPrime, iPrime)
                LLL.append((carryPrime, iPrime))
    LLL = list(set(LLL))
    for x,y in LLL:
        carry = x
        i = y
        M[(carry, i)] = {}
        if (i >= Kc + 1):
            bi = 0
        else:
            bi = findBi(C,i)
        for a1,a2,a3 in P:
            R = C1*a1 + C2*a2 + C3*a3 + bi + carry
            if (R%2 == 0):
                carryPrime = int(R/2)
                if (1 <= i) and (i <= Kc):
                    iPrime = i+1
                else:
                    iPrime = i
                M[(carry, i)][(a1,a2,a3)] = (carryPrime, iPrime)
    
    return M

def findCartesianM(M1, M2, P, L, P1, P2, CM):
    CM[(P1, P2)] = {}
    for a1,a2,a3 in P:
        try:
            # print("(0,1)(0,1) following (", a1,",",a2,",",a3,")", "can reach", M1[(0,1)][(a1,a2,a3)], M2[(0,1)][(a1,a2,a3)])
            CM[(P1, P2)][(a1,a2,a3)] = (M1[P1][(a1,a2,a3)], M2[P2][(a1,a2,a3)])
            L.append((M1[P1][(a1,a2,a3)], M2[P2][(a1,a2,a3)]))
        except:
            # print("Error")
            pass
    # print(L)
    LL = []
    for x,y in L:
        CM[(x,y)] = {}
        for a1,a2,a3 in P:
            try:
                # print(x,y,"following (", a1,",",a2,",",a3,")", "can reach", M1[x][(a1,a2,a3)], M2[y][(a1,a2,a3)])
                CM[(x, y)][(a1,a2,a3)] = (M1[x][(a1,a2,a3)], M2[y][(a1,a2,a3)])
                LL.append((M1[x][(a1,a2,a3)], M2[y][(a1,a2,a3)]))
            except:
                # print("Error")
                pass
    # print(LL)
    LLL = []
    for x,y in LL:
        CM[(x,y)] = {}
        for a1,a2,a3 in P:
            try:
                # print(x,y,"following (", a1,",",a2,",",a3,")", "can reach", M1[x][(a1,a2,a3)], M2[y][(a1,a2,a3)])
                CM[(x, y)][(a1,a2,a3)] = (M1[x][(a1,a2,a3)], M2[y][(a1,a2,a3)])
                LLL.append((M1[x][(a1,a2,a3)], M2[y][(a1,a2,a3)]))
            except:
                # print("Error")
                pass
    # print(LLL)

    return CM

def dfs(graph, node, end, visited, path):
    visited.add(node)
    if (node == end):
        # print(path)
        b = bb = bbb = ""
        for a in path:
            b += str(a[0])
            bb += str(a[1])
            bbb += str(a[2])
        print("The solution is:")
        print("X₁ =", int(b,2))
        print("X₂ =", int(bb,2))
        print("X₃ =", int(bbb,2))
        return path
    for x in graph[node]:
        try:
            path.append(x)
            if (graph[node][x] not in visited):
                dfs(graph,graph[node][x],end,visited,path)
                if (graph[node][x] in visited):
                    path.pop()
            else:
                path.pop()
        except:
            pass

    # pass



def findSolution(CM):
    if not (CM[((0,1),(0,1))].values()):
        print("Equation system doesnot have solution")
        return -1
    else:
        start = ((0,1),(0,1))
        end = ((0,3),(0,3))
        dfs(CM, start, end, set(), [])
        return 1


if __name__ == '__main__':
    # Symbols / Path
    P = [   (0,0,0),
            (0,0,1),
            (0,1,0),
            (1,0,0),
            (1,0,1),
            (1,1,0),
            (0,1,1),
            (1,1,1)     ]

    # FA M
    M1 = {}
    M2 = {}
    CM = {}

    # Does not have nonnegative integer solutions
    # print("T1 inputs:")
    # M1 = findM(3, -2, 1, 5, P, M1)
    # M2 = findM(6, -4, 2, 9, P, M2) 

    # Have nonnegative integer solutions
    print("T2 inputs:")
    M1 = findM(3, -2, -1, 3, P, M1)
    M2 = findM(6, -4, 1, 3, P, M2)

    CM = findCartesianM(M1, M2, P, [], (0,1), (0,1), CM)

    findSolution(CM)

    # print("M1 = [")
    # for x,y in M1.items():
    #     print("",str(x),':',str(y))
    # print("]")

    # print("M2 = [")
    # for x,y in M2.items():
    #     print("",str(x),':',str(y))
    # print("]")

    # print("M1xM2 = [")
    # for x,y in CM.items():
    #     print("",str(x),':',str(y))
    # print("]")