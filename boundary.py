import numpy as np
import utils
        

bndry_1a = utils.Boundary(param_range=[-1., 1.])
bndry_1a.polar_parametrization(order=1, parametrization={'r0': np.array([1.]), 'cs': np.array([0.]), 'ds': np.array([0.])})

bndry_1b = utils.Boundary(param_range=[-1., 1.], minr=0.3)
bndry_1b.polar_parametrization(order=1, parametrization={'r0': np.array([1.]), 'cs': np.array([-1.]), 'ds': np.array([0.0])})

bndry_2 = utils.Boundary(param_range=[-1., 1.], minr=0.3)
bndry_2.polar_parametrization(order=2, parametrization={'r0': np.array([1.]), 'cs': np.array([.5,.7]), 'ds': np.array([1.2,1.4])})

bndry_R2 = utils.Boundary(param_range=[-1., 1.], minr=0.3)
bndry_R2.polar_parametrization(order=2)

bndry_R3 = utils.Boundary(param_range=[-1., 1.], minr=0.5)
bndry_R3.polar_parametrization(order=3)

bndry_R4 = utils.Boundary(param_range=[-1., 1.], minr=1.)
bndry_R4.polar_parametrization(order=4)

utils.plot([bndry_1a.r, bndry_1b.r, bndry_2.r, bndry_R2.r, bndry_R3.r, bndry_R4.r], 
           labels=['circle', 'cardioid', 'order 2', 'rnd. ord. 2', 'rnd. ord. 3', 'rnd. ord. 4'])