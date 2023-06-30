from queue import Queue
from threading import Thread
import numpy as np


# INERFACE AND PARAMETERS DEFINITION
print("-------------------------------------------------------------")
print("DISTRIBUTED ALGORITHMS FOR SOLVING A SYSTEM OF LINEAR EQUATIONS\nsimplified, single computer version, multithread")
print("-------------------------------------------------------------")
print("--- Please describe the system:")
m = int(input("------ Number of agents:\n"))

print("------ Coefficient matrix B (enter each line and separate each value with a space):")
B = np.zeros((m, m))
for i in range(m):
    bi = [int(num) for num in input().split(" ")]
    while len(bi) != m:
        print("ERROR: Row must have m elements. Please try again.")
        bi = [int(num) for num in input().split(" ")]
    B[i] = np.array(bi)

print("------ Right hand side vector C (separate each value with a space):")
C = np.array([int(num) for num in input().split(" ")])
while C.shape[0] != m:
    print("ERROR: Row must have m elements. Please try again.")
    C = np.array([int(num) for num in input().split(" ")])

print("------ Weight matrix A (enter each line and separate each value with a space):")
A = np.zeros((m, m))
for i in range(m):
    ai = [float(num) for num in input().split(" ")]
    while round(sum(ai),1) != 1:
        print("ERROR: Sum of the row must equal 1. Please try again.")
        ai = [float(num) for num in input().split(" ")]
    A[i] = np.array(ai)


# COMPUTING
print("EQUATION SYSTEM:")
for i in range(m):
    print("|",end=" ")
    for j in range(m):
        if j!=0:
            print(" + ",end="")
        print(str(B[i,j])+"x"+str(j), end="")
    print(" =", C[i])

print("Solution found with numpy:",np.linalg.solve(B,C))

_sentinel = object()

def agent(queues, i, bi, ci, ai):
    prevXHat = np.zeros((m))
    xHat = np.zeros((m))
    # how many neighbors do I have ?
    nbNeighbors = 0    
    for j in range(m):
        if i!=j and ai[j]>0.:   # do not count yourself as a neighbor
            nbNeighbors+=1

    iter = 0
    while True:
        # STEP 1: Projection
        xi = np.zeros((m))
        if iter == 0:
            # initial state: agent has to compute a solution
            # idea: everything but x1 is zero
            xi[0] = ci/bi[0]
        else:
            # every other states: project xHat on hyperplane
            xi = (np.identity(m) - np.outer(bi.T,bi)/(np.linalg.norm(bi)**2))@xHat + ci*bi.T/(np.linalg.norm(bi)**2)
        
        # todo: si k!=i et A[i,k] > 0
        for k in range(m):
            if k != i and ai[k] > 0:
                queues[k].put([i, xi]) # each agent communicates their id and their current solution

        # STEP 2: Compare solutions
        # weighted average
        # each agent expects a message from every agent they are connected to
        X = np.zeros((m, m))
        X[i] = xi
        try:
            for _ in range(nbNeighbors):
                data = queues[i].get(timeout=3)
                X[data[0]] = data[1]
        except:
            xi = [round(n, 6) for n in xi]
            print("Solution found by the agent",i,":", xi)
            print("Number of iterations for agent",i,":",iter)
            break

        prevXHat = xHat.copy()
        xHat = ai@X

        dist = np.linalg.norm(xHat - prevXHat)
        if dist < 1E-6:
            xHat = [round(n, 6) for n in xHat]
            print("Solution found by the agent",i,":", xHat)
            print("Number of iterations for agent",i,":",iter)
            break

        iter = iter + 1
        
          
# Create the shared queue and variables and launch both threads
queues = []
for i in range(m):
    qi = Queue()
    queues.append(qi)

for i in range(m):
    ti = Thread(target = agent, args =(queues, i, B[i], C[i], A[i]))    # each thread ti only knows the ith row of each matrix
    ti.start()

        

