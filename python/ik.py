import numpy as np


def ik_newton():
    cos=np.cos; sin=np.sin

    q = np.array([0.5, 0.5])
    xd = np.array([1.2, 1.2])

    epsilon = 1e-3
    max_iter = 100


    for i in range(max_iter):
        q1 = q[0]
        q2 = q[1]
        J = np.array([[-sin(q1)-sin(q1+q2), -sin(q1+q2)]
                    [cos(q1)+cos(q1+q2), cos(q1+q2)]])
        f = np.array([cos(q1)+cos(q1+q2), sin(q1)+sin(q1+q2)])
        e = xd-f
        q = q + np.dot(np.linalg.inv(3), e)
        #Condicion de termino
        if (np.linalg.norm(e) < epsilon):
            break
    print(q)