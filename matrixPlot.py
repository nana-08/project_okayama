import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2,11)

# ITERATIONS
diagIterThreads = [19,36,52,65,80,95,107,121,134]
diagIterRpi = [19,35.67,39.5,53.6,67.67,79.29,90]
upTriIterThreads = [44,123,1227.6,4789.3,10645.4,47014.3]
upTriIterRpi = []
lowTriIterThreads = []
lowTriIterRpi = []
symIterThreads = []
symIterRpi = []

# TIME
diagTimeThreads = [0.00324,0.01005,0.02378,0.04123,0.06523,0.09537,0.12883,0.16911,0.21951]
diagTimeRpi = [0.53991,2.09453,3.25948,5.09765,7.36286,9.94951,12.85357]
upTriTimeThreads = [0.00683,0.03656,0.55841,2.95468,8.42703,46.11916] 
upTriTimeRpi = []
lowTriTimeThreads = []
lowTriTimeRpi = []
symTimeThreads = []
symTimeRpi = []