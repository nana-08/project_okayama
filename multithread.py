from queue import Queue
from threading import Thread
import numpy as np


# INERFACE AND PARAMETERS
print("-------------------------------------------------------------")
print("DISTRIBUTED ALGORITHMS FOR SOLVING A SYSTEM OF LINEAR EQUATIONS\nsimplified, single computer version")
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


# A thread that produces data
def producer(out_q):
    for i in range(10):
        # Produce some data
        data = "coucou"
        out_q.put(data)
          
# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        print(data)
        # Indicate completion
        in_q.task_done()
          
# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target = consumer, args =(q, ))
t2 = Thread(target = producer, args =(q, ))
t1.start()
t2.start()
  
# Wait for all produced items to be consumed
q.join()
        

