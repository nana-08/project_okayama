# author Loona Macabre
# simplified version of the Projected Consensus Alorithm                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
# for a single computer

import numpy as np


# INERFACE AND PARAMETERS
print("-------------------------------------------------------------")
print("DISTRIBUTED ALGORITHMS FOR SOLVING A SYSTEM OF LINEAR EQUATIONS\nsimplified, single computer version")
print("-------------------------------------------------------------")
# print("--- Please describe the system:")
# m = int(input("------ Number of agents:\n"))

# print("------ B matrix (enter each line and separate each value with a space):")
# B = np.zeros((m, m))
# for i in range(m):
#     bi = [int(num) for num in input().split(" ", m-1)]
#     B[i] = np.array(bi)
# print(B)

# print("------ C vector (separate each value with a space):")
# C = np.array([int(num) for num in input().split(" ", m-1)])
# print(C)


# COMPUTING
# B matrix
# B = np.array([[-65, 33, 28, 71, 59, -66],
#               [56, 29, 38, -75, -33, 86],
#               [72, -91, 73, 14, -70, 43],
#               [16, 9, -23, 63, -62, 85],
#               [-21, 86, -6, 23, 56, 24]])
# # C vector
# C = np.array([-115, 978, 612, 148, 399])

m = 2

B = np.array([[3, 7],
     [4, 2]])

C = np.array([16, 14])


# for each agent, projection onto the hyperplane
# initially each agent computes a solution
X = np.zeros((m, m))
prevxMean = np.zeros((m))
xMean = np.zeros((m))
for iter in range(10):  # todo
    for i in range(m):
        # STEP 1: Projection
        bi = B[i]
        ci = C[i]
        if iter == 0:
            # initial state: agent has to compute a solution
            # idea: everything but x1 is zero
            xi = np.zeros((m))
            xi[0] = ci/bi[0]
            print(xi)
            X[i] = xi
        else:
            # every other states: project xMean on hyperplane 
            xi = (np.identity(m) - bi.T@bi/(np.linalg.norm(bi)**2))@xMean + ci*bi.T/(np.linalg.norm(bi)**2)
            X[i] = xi

    # STEP 2: Compare solutions
    # mean
    prevxMean = xMean.copy()
    for i in range(m):
        xMean[i] = X.T[i].mean()

    print("X = ", X)
    print("prevxMean = ", prevxMean, ", xMean = ", xMean)
    dist = np.linalg.norm(prevxMean - xMean)
    if dist < 1E-6:
        break
