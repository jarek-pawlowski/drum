import os
import numpy as np
from scipy.linalg import eigh, inv
import matplotlib.pyplot as plt
from matplotlib import colors

theta_sampling = 0.005

class Boundary:
    def __init__(self, param_range=[0.,1.], minr = 0.0, normalization=True):
        self.param_range = param_range 
        self.minr = minr
        self.normalization = normalization
    def polar_parametrization(self, order=1, parametrization=None):
        if parametrization is None:
            self.r0 = (self.param_range[1] - self.param_range[0]) * np.random.random(1) + self.param_range[0]
            self.cs = (self.param_range[1] - self.param_range[0]) * np.random.random(order) + self.param_range[0]
            self.ds = (self.param_range[1] - self.param_range[0]) * np.random.random(order) + self.param_range[0]
        else:
            assert len(parametrization['r0']) == 1 and len(parametrization['cs']) == order and len(parametrization['ds']) == order, "some problem with parametrization"
            self.r0 = parametrization['r0']
            self.cs = parametrization['cs']
            self.ds = parametrization['ds']    
        self.r = lambda theta: self.r0 + np.sum([cn*np.sin(theta*(n+1)) for n, cn in enumerate(self.cs)]) + np.sum([dn*np.cos(theta*(n+1)) for n, dn in enumerate(self.ds)]) 
        if self.normalization:
            # avoiding negative r(\theta)
            rmin = np.amin(np.array([self.r(th) for th in np.arange(0, np.pi*2, theta_sampling)]).flatten())
            if rmin < self.minr:
                self.r0 += self.minr-rmin


def plot(params, labels=None):
    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')
    thetas = np.arange(0, np.pi*2, theta_sampling)
    if labels is None:
        labels = [' ']*len(params)
    for r,l in zip(params, labels):
        ax.plot(thetas, np.array([r(th) for th in thetas]).flatten(), label=l)
    ax.grid(True)
    ax.legend()
    plt.savefig(os.path.join('results', 'boundary'+'.png'), dpi=200)
    plt.close()