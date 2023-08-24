# author Loona Macabre
# simplified version of the Projected Consensus Alorithm                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
# for a single computer

import numpy as np


# INERFACE AND PARAMETERS DEFINITION
print("-------------------------------------------------------------")
print("DISTRIBUTED ALGORITHMS FOR SOLVING A SYSTEM OF LINEAR EQUATIONS\nsimplified, single computer version, sequential")
print("-------------------------------------------------------------")
print("--- Please describe the system:")
m = int(input("------ Number of agents:\n"))

print("------ Coefficient matrix B (enter each line and separate each value with a space):")
B = np.zeros((m, m))
for i in range(m):
    bi = [int(num) for num in input().split(" ", m-1)]
    B[i] = np.array(bi)

print("------ Right hand side vector C (separate each value with a space):")
C = np.array([int(num) for num in input().split(" ", m-1)])

print("------ Weight matrix A (enter each line and separate each value with a space):")
A = np.zeros((m, m))
for i in range(m):
    ai = [float(num) for num in input().split(" ", m-1)]
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

# for each agent, projection onto the hyperplane
# initially each agent computes a solution
X = np.zeros((m, m))
prevXHat = np.zeros((m, m))
xHat = np.zeros((m, m))
iter = 0
while 1:  # todo
    for i in range(m):
        # STEP 1: Projection
        bi = B[i]
        ci = C[i]
        xi = np.zeros((m))
        if iter == 0:
            # initial state: agent has to compute a solution
            # idea: everything but x1 is zero
            xi[0] = ci/bi[0]
        else:
            # every other states: project xHat on hyperplane
            xi = (np.identity(m) - np.outer(bi.T,bi)/(np.linalg.norm(bi)**2))@xHat[i] + ci*bi.T/(np.linalg.norm(bi)**2)
            #print("projection x",i,":",xi)
        
        X[i] = xi

    # STEP 2: Compare solutions
    # weighted average
    prevXHat = xHat.copy()
    xHat = A@X

    # print("X = ", X)
    # print("xHat = ", xHat)
    dist = np.linalg.norm(xHat - prevXHat)
    if dist < 1E-10:
        print("Solution found by the agents:", np.mean(xHat, axis=0))
        break

    iter = iter + 1
