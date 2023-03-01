from roboticstoolbox import ET2, ET
import roboticstoolbox as rtb
import math

pi = math.pi
q = [pi/6,0.8]
a1 = 1
a2 = 1

#2D
T_01 = ET2.R(q[0],'rad') * ET2.tx(a1)
T_12 = ET2.R(q[1],'rad') * ET2.tx(a2)
T_02 = T_01*T_12
K_2d = T_02.fkine([])
print("2-DOF PLANAR ROBOT (2D SPACE) - FK:")
print(K_2d)

#3D
T_01_3d = ET.Rz(q[0],'rad') * ET.tx(a1)
T_12_3d = ET.Rz(q[1],'rad') * ET.tx(a2)
T_02_2d = T_01_3d*T_12_3d
K_2d_3d = T_02_2d.fkine([])
print("2-DOF PLANAR ROBOT (2D SPACE) - FK:")
print(K_2d_3d)


#RR planar robot from library
robot1 = rtb.models.ETS.Planar2()
robot1.a1 = 0.1
T = robot1.fkine(q)
print("2-DOF PLANAR ROBOT (2D SPACE) - FK:")
print(T)
robot1.plot(q, block=True)