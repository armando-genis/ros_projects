from spatialmath.base import rot2
from sympy import simplify, Matrix
import spatialmath.base as base
import numpy as np
import math
# 2d case
# Numeric

R = rot2(math.pi/2) #Radians
print(R)
det = np.linalg.det(R)
print("EL DETERMINANTE ES: ",det)
theta = base.sym.symbol('\u03B8')
rot_sym = base.rot2(theta)
print(rot_sym)
RxR_sym = rot_sym.dot(rot_sym)
print(RxR_sym)