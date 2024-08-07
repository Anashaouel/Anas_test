import numpy as np
import matplotlib.pyplot as plt

E=28000

def S(x):
    return (E*x)

E1=[-0.0001769, -0.0001818, -0.0001866, -0.0001915, -0.0001963, -0.0002012,
   -0.0002060, -0.0002109, -0.000158, -0.0002206, -0.0002255, -0.0002303, -0.000352]
S1=[-5.201,-5.340,-5.479,-5.618,-5.757,-5.895,-6.034,-6.173,-6.312,-6.451,-6.590,-6.729,-6.867]

E2=np.linspace(-0.0002,0,100)
S2=np.array([S(i) for i in E2])
plt.plot(E1,S1,label='La courbe déformation-contrainte pratique',color='r')
plt.plot(E2,S2,label='La courbe déformation-contrainte théorique',color='b')
plt.xlabel('La déformation')
plt.ylabel('La contrainte')
plt.grid()
plt.legend()
plt.show()
