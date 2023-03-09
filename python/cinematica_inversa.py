from spatialmath import *
import roboticstoolbox as rtb
import math 
from ik import ik_newton

pi = math.pi
l1 =1 
l2 = 1
x = 1.2
y = 1.2


try:
    #Elbow Down
    cos_theta1 = (x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2)
    sin_theta1 = math.sqrt(1 - (cos_theta1**2))
    theta2_down = math.atan2(sin_theta1, cos_theta1)
    beta = math.acos((x**2 + y**2 + l1**2 - l2**2)/(2*l1*math.sqrt(x**2 + y**2)))
    theta1_down = math.atan2(y, x) - beta
    print("Angles for Elbow Down Config")
    print(theta1_down, theta2_down)

    #Elbow Up
    cos_theta2 = (x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2)
    sin_theta2 = - math.sqrt(1 - (cos_theta2**2))
    theta2_up = math.atan2(sin_theta2, cos_theta2)
    beta = math.acos((x*2 + y*2 + l1**2 - l2**2)/(2*l1*math.sqrt(x*2 + y*2)))
    theta1_up = math.atan2(y, x) + beta
    print("Angles for Elbow Down Config")
    print(theta1_up, theta2_up)

    q_planar = [theta1_up, theta2_up]
    q_planar2 = [theta1_down, theta2_down]

    robot1 = rtb.models.ETS.Planar2()
    robot2 = rtb.models.ETS.Planar2()

    T = robot1.fkine(q_planar)
    T_n = SE3(T)
    print("2-DOF planar robot - IK")
    print("Elbow Up")
    robot1.plot(q_planar, block=True)
    print("Elbow Down")
    robot2.plot(q_planar2, block=True)
except ValueError:
    print("invalidad configuration. Please review desired position")

print("newton Method")
ik_newton()