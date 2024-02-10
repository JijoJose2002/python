import math
import matplotlib.pyplot as plt

#Define engine kinematics

def engine_kinematics(bore,stroke,con_rod,cr,start_crank,end_crank):
    a=stroke/2
    R=con_rod/a
    v_s=(math.pi/4)*pow(bore,2)*stroke
    v_c=v_s/(cr-1)
    sc=math.radians(start_crank)
    ec=math.radians(end_crank)
    num_value=50
    dtheta=(ec-sc)/(num_value-1)
    V=[]
    for i in range(0,num_value):
        theta=sc+i*dtheta
        term1 = 0.5*(cr-1)
        term2 = R+1-math.cos(theta)
        term3 = pow(R,2)-pow(math.sin(theta),2)
        term3 = pow(term3,0.5)
        V.append((1+term1*(term2-term3))*v_c)
    return V

#step 3: Define inputs
p1 = 102325
t1 = 500
gamma = 1.4
t3 = 2300
bore = 0.1
stroke = 0.1
con_rod = 0.15
cr = 9

#step 4 : calculate initial and final volumes
v_s=(math.pi/4)*pow(bore,2)*stroke
v_c=v_s/(cr-1)
v1=v_s+v_c
v2=v_c

#step 4:Calculate state point 2
p2=p1*pow(v1,gamma)/pow(v2,gamma)
rhs = p1*v1/t1
t2=p2*v2/rhs

#state 6: Characterize compression process
V_compression = engine_kinematics(bore,stroke,con_rod,cr,180,0)
constant = p1*pow(v1,gamma)
P_compression = [constant/pow(v,gamma) for v in V_compression]


#step7 : Calculate for state point 3 
v3 = v2
rhs = p2*v2/t2
p3 = rhs*t3/v3


#step 8 : characterize expansion process
V_expansion = engine_kinematics(bore,stroke,con_rod,cr,0,180)
constant = p3*pow(v3,gamma)
P_expansion = [constant/pow(v,gamma) for v in V_expansion]

#step 9 : Calculate for state point 4
v4 = v1
p4=p3*pow(v3,gamma)/pow(v4,gamma)
rhs=p3*v3/t3
t4 = p4*v4/rhs

#step 10: plot PV Diagram
plt.figure(1)
plt.plot(V_compression,P_compression,label = 'Adiabatic Compression')
plt.plot([v2,v3],[p2,p3],label='Constant volume heat addition')
plt.plot(V_expansion,P_expansion, label = 'Adiabatic')
plt.plot([v4,v1],[p4,p1],label='constant volume heat rejection')
plt.xlabel('volume')
plt.ylabel('pressure')
plt.legend()
plt.title('Otto cycle PV diagram')
plt.savefig('Otto cycle pv diagram')
plt.show()


#step 11: Calculate and Display Thermal Efficiency
eff=1-(1/pow(cr,(gamma-1)))
eff_percent = eff*100
print(f'Thermal efficiency: {eff_percent:.2f}%')

