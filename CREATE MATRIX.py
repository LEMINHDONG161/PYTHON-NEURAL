import tensorflow as tf
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import random
import math
# create input and output data for training
input_data = [[0 for a in range(100)] for b in range(2)] 
output_data = [[0 for a1 in range(100)] for b1 in range(1)] 
for i in range(100):
    x1=random.uniform(-3,3)
    x2=random.uniform(-3,3)
    y1= 0.4*(np.power(2.71, -0.5*(x1*x1+x2*x2)))
    input_data[0][i]=x1
    input_data[1][i]=x2
    output_data[0][i]=y
# Parameters