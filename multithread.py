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

        B = [[1,2,0,3,5,1,4,2,7,3],
            [0,1,3,4,6,2,2,8,1,1],
            [7,7,8,2,1,1,1,0,2,9],
            [2,3,4,7,2,6,11,8,9,7],
            [6,3,13,5,0,1,2,1,8,1],
            [4,2,4,4,1,3,8,7,9,3],
            [3,2,2,8,6,7,1,9,4,0],
            [8,8,1,9,2,10,6,1,7,4],
            [12,2,1,0,9,8,6,7,3,7],
            [4,10,6,8,1,1,2,3,8,4]]

        C = {"2":[16,7],
            "3":[16,16,87],
            "4":[19,20,89,44],
            "5":[19,20,89,44,77],
            "6":[27,36,97,92,85,62],
            "7":[63,54,106,191,103,134,99],
            "8":[87,150,106,287,115,218,207,230],
            "9":[164,161,128,386,203,317,251,307,276],
            "10":[176,165,164,414,207,329,251,323,304,270]}
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
print("Solution found with numpy:",list(map(round, np.linalg.solve(Bm,Cm))))


nbIterTot = 0
tempsTot = 0
solutions = []
r = 10
for repet in range(r):
    print("+", end="")

    # semaphores
    nbIterTotRLock = Lock()
    tempsTotRLock = Lock()
    solutionsRLock = Lock()


    nbIterTotR = 0
    tempsTotR = 0
    solutionsR = []
    # COMPUTING
    def agent(queues, i, bi, ci, ai):
        global nbIterTotR
        global tempsTotR
        global solutionsR

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

            dist = np.linalg.norm(xHat - prevXHat)
            if dist < 1E-6:
                break

            iter = iter + 1
            
        temps = time.time()-start
        # print("Solution found by the agent",i,":",list(map(round, xHat)),", in",iter,"iterations,",round(temps,3),"seconds")
        solutionsRLock.acquire()
        solutionsR.append(xHat)
        solutionsRLock.release()

        nbIterTotRLock.acquire()
        nbIterTotR += iter
        nbIterTotRLock.release()

        tempsTotRLock.acquire()
        tempsTotR += temps
        tempsTotRLock.release()
            
        
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

    nbIterTot += nbIterTotR/m
    tempsTot += tempsTotR/m
    solutions.append(solutionsR)


nbIterTot = nbIterTot/r   
tempsTot = tempsTot/r  
avgSolution = np.mean([np.mean(solR, axis=0) for solR in solutions], axis=0)
print("\nSolutions =",solutions,"\nAverage solution =",avgSolution,"\nAverage time =", round(tempsTot,5), "s\nAverage number of iterations =", round(nbIterTot, 2))

