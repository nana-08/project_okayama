from queue import Queue
from threading import Thread, Lock
import numpy as np
import time


# INERFACE AND PARAMETERS DEFINITION
print("-------------------------------------------------------------")
print("DISTRIBUTED ALGORITHMS FOR SOLVING A SYSTEM OF LINEAR EQUATIONS\nsimplified, single computer version, multithread")
print("-------------------------------------------------------------")
print("--- Please describe the system:")
btype = int(input("------ Type of matrix:\n1. Regular     2. Diagonal     3. Upper Triangular     4. Lower Triangular     5. Symmetric\n"))

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

        B = [[-65,33,28,71,59],
            [56,29,38,-75,-33],
            [72,-91,73,14,-70],
            [16,9,-23,63,-62],
            [-21,86,-6,23,56]]

        C = {"2":[37,80],
            "3":[70,102,133],
            "4":[90,107,178,209],
            "5":[149,634,440,-192,303]}
    case 2:
        m = int(input("------ Number of agents:\n"))

        B = [[3,0,0,0,0,0,0,0,0,0],
            [0,5,0,0,0,0,0,0,0,0],
            [0,0,8,0,0,0,0,0,0,0],
            [0,0,0,11,0,0,0,0,0,0],
            [0,0,0,0,2,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,8,0,0],
            [0,0,0,0,0,0,0,0,7,0],
            [0,0,0,0,0,0,0,0,0,9]]

        C = {"2":[21,10],
            "3":[21,10,88],
            "4":[21,10,88,55],
            "5":[21,10,88,55,16],
            "6":[21,10,88,55,16,2],
            "7":[21,10,88,55,16,2,15],
            "8":[21,10,88,55,16,2,15,104],
            "9":[21,10,88,55,16,2,15,104,7],
            "10":[21,10,88,55,16,2,15,104,7,63]}
    case 3:
        m = int(input("------ Number of agents:\n"))

        B = [[3,8,3,4,2,10,8,6,2,5],
            [0,5,2,1,8,7,4,12,11,3],
            [0,0,8,9,12,13,5,6,7,9],
            [0,0,0,11,2,1,1,8,1,3],
            [0,0,0,0,2,19,10,2,16,4],
            [0,0,0,0,0,1,2,8,7,7],
            [0,0,0,0,0,0,1,9,6,6],
            [0,0,0,0,0,0,0,8,3,16],
            [0,0,0,0,0,0,0,0,7,1],
            [0,0,0,0,0,0,0,0,0,9]]

        C = {"2":[37,10],
            "3":[70,32,88],
            "4":[90,37,133,55],
            "5":[106,101,229,71,16],
            "6":[126,115,255,73,54,2],
            "7":[246,175,330,88,204,32,15],
            "8":[324,330,408,192,230,136,132,104],
            "9":[326,341,415,193,246,143,138,107,7],
            "10":[361,363,478,214,274,192,180,219,14,63]}
    case 4:
        m = int(input("------ Number of agents:\n"))

        B = [[3,0,0,0,0,0,0,0,0,0],
            [10,5,0,0,0,0,0,0,0,0],
            [5,5,8,0,0,0,0,0,0,0],
            [12,13,4,11,0,0,0,0,0,0],
            [9,2,1,2,2,0,0,0,0,0],
            [4,8,9,5,15,1,0,0,0,0],
            [8,7,15,16,2,18,1,0,0,0],
            [7,2,2,1,3,4,14,8,0,0],
            [15,1,3,10,9,6,3,4,7,0],
            [8,8,0,7,2,4,4,9,0,2]]

        C = {"2":[21,80],
            "3":[21,80,133],
            "4":[21,80,133,209],
            "5":[21,80,133,209,104],
            "6":[21,80,133,209,104,290],
            "7":[21,80,133,209,104,290,382],
            "8":[21,80,133,209,104,290,382,426],
            "9":[21,80,133,209,104,290,382,426,378],
            "10":[21,80,133,209,104,290,382,426,378,449]}
    case 5:
        m = int(input("------ Number of agents:\n"))

        B = [[3,8,3,4,2,10,8,6,2,5],
            [8,5,2,1,8,7,4,12,11,3],
            [3,2,8,9,12,13,5,6,7,9],
            [4,1,9,11,2,1,1,8,1,3],
            [2,8,12,2,2,19,10,2,16,4],
            [10,7,13,1,19,1,2,8,7,7],
            [8,4,5,1,10,2,1,9,6,6],
            [6,12,6,8,2,8,9,8,3,16],
            [2,11,7,1,16,7,6,3,7,1],
            [5,3,9,3,4,7,6,16,1,9]]

        C = {"2":[37,66],
            "3":[70,88,113],
            "4":[90,93,158,184],
            "5":[106,157,254,200,188],
            "6":[126,171,280,202,226,386],
            "7":[246,231,355,217,376,434,223],
            "8":[324,387,433,321,402,520,340,443],
            "9":[326,398,440,322,418,527,346,446,396],
            "10":[361,419,503,343,446,576,388,558,403,563]}


A = {"2":[0.5,0.5],
     "3":[0.33,0.33,0.34],
     "4":[0.25,0.25,0.25,0.25],
     "5":[[0.3,0.4,0.3,0,0],
          [0.2,0.4,0.1,0.3,0],
          [0.1,0.3,0.4,0,0.2],
          [0,0.4,0,0.3,0.3],
          [0,0,0.3,0.2,0.5]],
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

nbIterTot = 0
tempsTot = 0
solutions = []
points = np.zeros((m+1,2))
points[0] = trueSolution[:2]

nbIterTotLock = Lock()
tempsTotLock = Lock()
solutionsLock = Lock()
pointsLock = Lock()

# COMPUTING
def agent(queues, i, bi, ci, ai):
    global nbIterTot
    global tempsTot
    global solutions
    global points

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
            # idea: everything but xii is zero. if bii is null, first xij where bij isn't null is zero
            if bi[i] == 0:
                j = 0
                while bi[j] == 0:
                    j+=1
                xi[j] = ci/bi[j]
            else:
                xi[i] = ci/bi[i]
        else:
            # every other states: project xHat on hyperplane
            xi = (np.identity(m) - np.outer(bi.T,bi)/(np.linalg.norm(bi)**2))@xHat + ci*bi.T/(np.linalg.norm(bi)**2)
        
        # pointsLock.acquire()
        # points[i+1] = xi[:2]
        # strPoints = ""
        # for p in points:
        #     strPoints += str(p[0])+", "+str(p[1])+"\n"
        # open("points.txt","w").write(strPoints)
        # pointsLock.release()
            
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
    ti = Thread(target = agent, args =(queues, i, np.array(Bm[i]), np.array(Cm[i]), np.array(Am[i])))    # each thread ti only knows the i-th row of each matrix
    threads.append(ti)
    ti.start()

for ti in threads:
    ti.join()

avgSolution = np.mean(solutions, axis=0)
nbIterTot = nbIterTot/m
tempsTot = tempsTot/m
print("\nSolutions =",solutions,"\nAverage solution =",avgSolution,"\nAverage time =", round(tempsTot,5), "s\nAverage number of iterations =", round(nbIterTot, 2))