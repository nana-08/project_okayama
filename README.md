# project_okayama
Internship in Okayama University, Japan
Tutor: Norikazu Takahashi

## GOAL of the overall project: 
Develop and implement a distributed algorithm in Python for solving a system of linear equations Bx = C.

## GOALS step by step
- [x] Read [Takahashi and Kawashima's paper](ieeecsl2018_takahashi_kawashima.pdf) and understand what is done in the Projected Consensus Algorithm.

- [x] Implement a simplified version of their algorithm using Python on a single computer (sequential and mutlithread).

- [ ] Implement the program on 10 Raspberry Pi computers communicating witn each other (ex, 10 computers work as web servers and communication is done using http protocols)

## FILES
### singleComputer.py
Execution of the Projected Consensus Algorithm on a single thread. The agents execute the algorithm turn by turn in a for loop. They communicate via these global variables:
- X: m x m matrix, contains the current solutions of every agent -> X[i] is the solution vector of the agent i
- xHat: m x m matrix, contains the weighted average of X computed by every agent -> xHat[i] is the weighted average of X that agent i computed
- prevXHat: xHat at previous iteration

### multithread.py
Execution of the Projected Consensus Algorithm on several threads: each agent executes the algorithm on its dedicated thread. Agents communicate via their queues. 

Notes:
For 10 agents, it takes up to a million iterations for each agent to finish