from queue import Queue
from threading import Thread, Lock
import numpy as np
import time


# INERFACE AND PARAMETERS DEFINITION
print("-------------------------------------------------------------")
print("DISTRIBUTED ALGORITHMS FOR SOLVING A SYSTEM OF LINEAR EQUATIONS\nsimplified, single computer version, multithread")
print("-------------------------------------------------------------")
print("--- Please describe the system:")
btype = int(input("------ Type of matrix:\n1. Regular\t2. Diagonal\t3. Upper Triangular\t4. Lower Triangular\t5. Symmetric\n"))

# print("------ Coefficient matrix B (enter each line and separate each value with a space):")
# B = np.zeros((m, m))
# for i in range(m):
#     bi = [int(num) for num in input().split(" ")]
#     while len(bi) != m:
#         print("ERROR: Row must have m elements. Please try again.")
#         bi = [int(num) for num in input().split(" ")]
#     B[i] = np.array(bi)

# print("------ Right hand side vector C (separate each value with a space):")
# C = np.array([int(num) for num in input().split(" ")])
# while C.shape[0] != m:
#     print("ERROR: Row must have m elements. Please try again.")
#     C = np.array([int(num) for num in input().split(" ")])

# print("------ Weight matrix A (enter each line and separate each value with a space):")
# A = np.zeros((m, m))
# for i in range(m):
#     ai = [float(num) for num in input().split(" ")]
#     while len(ai) != m:
#         print("ERROR: Row must have m elements. Please try again.")
#         ai = [float(num) for num in input().split(" ")]
#     while round(sum(ai),1) != 1:
#         print("ERROR: Sum of the row must equal 1. Please try again.")
#         ai = [float(num) for num in input().split(" ")]
#     A[i] = np.array(ai)

# print("EQUATION SYSTEM:")
# for i in range(m):
#     print("|",end=" ")
#     for j in range(m):
#         if j!=0:
#             print(" + ",end="")
#         print(str(B[i,j])+"x"+str(j), end="")
#     print(" =", C[i])


match btype:
    case 1:
        m = int(input("------ Number of agents:\n"))

        B = [[3,8,3,4,2,10,8,6,2,5],
            [10,5,2,1,8,7,4,12,11,3],
            [5,5,8,9,12,13,5,6,7,9],
            [12,13,4,11,2,1,1,8,1,3],
            [9,2,1,2,2,19,10,2,16,4],
            [4,8,9,5,15,1,2,8,7,7],
            [8,7,15,16,2,18,1,9,6,6],
            [7,2,2,1,3,4,14,8,3,16],
            [15,1,3,10,9,6,3,4,7,1],
            [2,4,5,1,19,18,2,6,8,9]]

        C = {"2":[37,80],
            "3":[70,102,133],
            "4":[90,107,178,209],
            "5":[106,171,274,225,104],
            "6":[126,185,300,227,142,290],
            "7":[246,245,375,242,292,320,382],
            "8":[324,400,453,346,318,424,499,426],
            "9":[326,411,460,347,334,431,505,429,378],
            "10":[361,433,523,368,362,480,547,541,385,449]}
    case 2:
        m = int(input("------ Number of agents:\n"))

        B = [[3,0,0,0,0,0,0,0,0,0],
            [0,9,0,0,0,0,0,0,0,0],
            [0,0,7,0,0,0,0,0,0,0],
            [0,0,0,2,0,0,0,0,0,0],
            [0,0,0,0,2,0,0,0,0,0],
            [0,0,0,0,0,3,0,0,0,0],
            [0,0,0,0,0,0,3,0,0,0],
            [0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,8]]

        C = {"2":[3,0],
            "3":[3,0,63],
            "4":[3,0,63,8],
            "5":[3,0,63,8,2],
            "6":[3,0,63,8,2,15],
            "7":[3,0,63,8,2,15,12],
            "8":[3,0,63,8,2,15,12,0],
            "9":[3,0,63,8,2,15,12,0,5],
            "10":[3,0,63,8,2,15,12,0,5,24]}
    case 3:
        m = int(input("------ Number of agents:\n"))

        B = [[5,3,6,5,9,2,4,5,2,9],
            [0,2,2,7,7,4,0,4,9,8],
            [0,0,4,5,7,0,2,9,0,6],
            [0,0,0,1,2,3,5,4,8,6],
            [0,0,0,0,5,8,3,0,3,0],
            [0,0,0,0,0,9,5,5,7,2],
            [0,0,0,0,0,0,1,6,0,9],
            [0,0,0,0,0,0,0,5,2,3],
            [0,0,0,0,0,0,0,0,3,9],
            [0,0,0,0,0,0,0,0,0,1]]

        C = {"2":[50,10],
            "3":[104,28,36],
            "4":[134,70,66,6],
            "5":[152,84,80,10,10],
            "6":[152,84,80,10,10,0],
            "7":[164,84,86,25,19,15,3],
            "8":[179,96,113,37,19,30,21,15],
            "9":[185,123,113,111,28,51,21,21,9],
            "10":[248,179,155,153,28,65,84,42,72,7]}
    case 4:
        m = int(input("------ Number of agents:\n"))

        B = [[5,0,0,0,0,0,0,0,0,0],
            [4,1,0,0,0,0,0,0,0,0],
            [6,1,5,0,0,0,0,0,0,0],
            [9,9,0,2,0,0,0,0,0,0],
            [0,4,2,0,5,0,0,0,0,0],
            [0,2,8,3,1,1,0,0,0,0],
            [8,4,2,3,2,5,2,0,0,0],
            [2,5,3,6,9,6,2,9,0,0],
            [7,4,0,0,5,6,6,7,3,0],
            [8,8,0,7,2,4,4,9,0,2]]

        C = {"2":[25,26],
            "3":[25,26,46],
            "4":[25,26,46,101],
            "5":[25,26,46,101,53],
            "6":[25,26,46,101,53,43],
            "7":[25,26,46,101,53,43,126],
            "8":[25,26,46,101,53,43,126,185],
            "9":[25,26,46,101,53,43,126,185,202],
            "10":[25,26,46,101,53,43,126,185,202,195]}
    case 5:
        m = int(input("------ Number of agents:\n"))

        B = [[1,4,9,3,2,2,0,0,4,2],
            [4,5,5,2,4,3,7,2,5,0],
            [9,5,3,1,3,4,8,3,2,4],
            [3,2,1,1,3,3,7,9,5,3],
            [2,4,3,3,4,1,6,2,9,0],
            [2,3,4,3,1,6,7,6,2,9],
            [0,7,8,7,6,7,0,3,4,5],
            [0,2,3,9,2,6,3,4,6,9],
            [4,5,2,5,9,2,4,6,6,1],
            [2,0,4,3,0,9,5,9,1,4]]

        C = {"2":[9,14],
            "3":[41,34,31],
            "4":[56,44,36,16],
            "5":[58,48,39,19,41],
            "6":[62,54,47,25,43,52],
            "7":[62,75,71,46,61,73,101],
            "8":[62,79,77,64,65,85,107,92],
            "9":[66,84,79,69,74,87,111,98,90],
            "10":[72,84,91,78,74,114,126,125,93,97]}


A = {"2":[0.5,0.5],
     "3":[0.33,0.33,0.34],
     "4":[0.25,0.25,0.25,0.25],
     "5":[0.2,0.2,0.2,0.2,0.2],
     "6":[0.166,0.166,0.166,0.166,0.166,0.17],
     "7":[0.14,0.14,0.14,0.14,0.14,0.14,0.16],
     "8":[0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125],
     "9":[0.11,0.11,0.11,0.11,0.11,0.11,0.11,0.11,0.12],
     "10":[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]}


Bm = [[j for j in B[i][:m]] for i in range(m)]
Cm = C[str(m)]
Am = A[str(m)]
trueSolution = list(map(round, np.linalg.solve(Bm,Cm)))
print("Solution found with numpy:", trueSolution)


points = np.zeros((m+1,2))    # graph in 2D
points[0] = trueSolution[:2]
nbIterTot = 0
tempsTot = 0
solutions = []
file = open("points.txt","w")

nbIterTotLock = Lock()
tempsTotLock = Lock()
solutionsLock = Lock()
pointsLock = Lock()
fileLock = Lock()

# COMPUTING
def agent(queues, i, bi, ci, ai):
    global nbIterTot
    global tempsTot
    global solutions
    global file

    prevXHat = np.zeros((m))
    xHat = np.zeros((m))
    # how many neighbors do I have ?
    nbNeighbors = 0    
    for j in range(m):
        if i!=j and ai[j]>0.:   # do not count yourself as a neighbor
            nbNeighbors+=1

    iter = 0
    start = time.time()
    while True:

        # STEP 1: Projection
        xi = np.zeros((m))
        if iter == 0:
            # initial state: agent has to compute a solution
            # idea: everything but the first xj where bij isn't null is zero
            j = 0
            while bi[j] == 0:
                j+=1
            xi[j] = ci/bi[j]
        else:
            # every other states: project xHat on hyperplane
            xi = (np.identity(m) - np.outer(bi.T,bi)/(np.linalg.norm(bi)**2))@xHat + ci*bi.T/(np.linalg.norm(bi)**2)
            
        # communicate your solution to your neighbors
        for k in range(m):
            if k != i and ai[k] > 0:
                queues[k].put((i, xi)) # each agent communicates their id and their current solution


        # STEP 2: Compare solutions
        # each agent expects a message only from the agents they are connected to => nbNeighbors messages in total
        X = np.zeros((m, m))
        X[i] = xi
        try:
            for _ in range(nbNeighbors):
                j, xj = queues[i].get(timeout=1)
                X[j] = xj
        except:
            break

        # weighted average
        prevXHat = xHat.copy()
        xHat = ai@X
        pointsLock.acquire()
        points[i+1] = xHat[:2]
        fileLock.acquire()
        file = open("points.txt","w")
        strPoints = ""
        for point in points:
            strPoints += str(point[0]) + "," + str(point[1]) + "\n"
        file.write(strPoints)
        fileLock.release()
        pointsLock.release() 

        dist = np.linalg.norm(xHat - prevXHat)
        if dist < 1E-10:
            break

        iter = iter + 1
            
    temps = time.time()-start
    # print("Solution found by the agent",i+1,":",list(map(round, xHat)),", in",iter,"iterations,",round(temps,3),"seconds")
    solutionsLock.acquire()
    solutions.append(xHat)
    solutionsLock.release()
    nbIterTotLock.acquire()
    nbIterTot += iter
    nbIterTotLock.release()
    tempsTotLock.acquire()
    tempsTot += temps
    tempsTotLock.release()
            

# Create the shared queue and variables and launch both threads
queues = []
for i in range(m):
    qi = Queue()
    queues.append(qi)

threads = []
for i in range(m):
    ti = Thread(target = agent, args =(queues, i, np.array(Bm[i]), np.array(Cm[i]), np.array(Am)))    # each thread ti only knows the i-th row of each matrix
    threads.append(ti)
    ti.start()

for ti in threads:
    ti.join()

file.close()
avgSolution = np.mean(solutions, axis=0)
nbIterTot = nbIterTot/m
tempsTot = tempsTot/m
print("\nSolutions =",solutions,"\nAverage solution =",avgSolution,"\nAverage time =", round(tempsTot,5), "s\nAverage number of iterations =", round(nbIterTot, 2))

