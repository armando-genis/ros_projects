import numpy as np

import math
pi = math.pi
q = [pi/4,0.2,pi,0.3,-pi/6,-1.3,0.4]
l = [270.35,69.00,364.35,69.00,374.29,10.00,368.30]


matrix0T1 =  np.array([[np.cos(q[0]), -np.sin(q[0]), 0, 0], [np.sin(q[0]), np.cos(q[0]), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]]);

matrix1T2 =  np.array([[-np.sin(q[1]), -np.cos(q[1]), 0, l[1]], [0, 0, 1, 0],[-np.cos(q[1]), np.sin(q[1]), 0, 0],[0, 0, 0, 1]]);

matrix2T3 =  np.array([[np.cos(q[2]), -np.sin(q[+2]), 0, 0], [0, 0, -1, -l[2]],[np.sin(q[2]), np.cos(q[2]), 0, 0],[0, 0, 0, 1]]);

matrix3T4 =  np.array([[np.cos(q[3]), -np.sin(q[3]), 0, l[3]], [0, 0, 1, 0],[-np.sin(q[3]), -np.cos(q[3]), 0, 0],[0, 0, 0, 1]]);

matrix4T5 =  np.array([[np.cos(q[4]), -np.sin(q[4]), 0, 0], [0, 0, -1, -l[4]],[np.sin(q[4]), np.cos(q[4]), 0, 0],[0, 0, 0, 1]]);

matrix5T6 =  np.array([[np.cos(q[5]), -np.sin(q[5]), 0, l[5]], [0, 0, 1, 0],[-np.sin(q[5]), -np.cos(q[5]), 0, 0],[0, 0, 0, 1]]);

matrix6T7 =  np.array([[np.cos(q[6]), -np.sin(q[6]), 0, 0], [0, 0, -1, 0],[np.sin(q[6]), np.cos(q[6]), 0, 0],[0, 0, 0, 1]]);

print("MATRIX OT1")
print(matrix0T1)
print("MATRIX 1T2")
print(matrix1T2)
print("MATRIX 2T3")
print(matrix2T3)
print("MATRIX 3T4")
print(matrix3T4)
print("MATRIX 4T5")
print(matrix4T5)
print("MATRIX 5T6")
print(matrix5T6)
print("MATRIX 6T7")
print(matrix6T7)

print("multipliacion: ")
matrix0T2 = np.matmul(matrix0T1, matrix1T2)
matrix0T3 = np.matmul(matrix0T2, matrix2T3)
matrix0T4 = np.matmul(matrix0T3, matrix3T4)
matrix0T5 = np.matmul(matrix0T4, matrix4T5)
matrix0T6 = np.matmul(matrix0T5, matrix5T6)
matrix0T7 = np.matmul(matrix0T6, matrix6T7)
print(matrix0T7)

