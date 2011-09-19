from scipy.integrate import odeint
import pylab as pl
import numpy as np

pl.rcParams['figure.figsize'] = 11, 3.5
pl.rcParams['font.size'] = 20
pl.rcParams['xtick.labelsize'] = 20
pl.rcParams['ytick.labelsize'] = 20
pl.rcParams['legend.fontsize'] = 20

R = 1e3
L = 1e-3
U0 = 10

# initial condition
y0 = [0]

def func(y, t):
    return [- R/L*y[0] + U0/L]

t = np.arange(0, 5*L/R, L/R/10)
y = odeint(func, y0, t)

# chart
pl.close()
pl.plot(t, y)
ax = pl.gca()
ax.ticklabel_format(style='sci', scilimits=(0,0), axis='x')
pl.grid(True)
pl.xlabel("$t\,\mathrm{(s)}$")
pl.ylabel("$i_\mathrm{L}\,\mathrm{(A)}$")
pl.savefig('obvod_rl_proud.pdf', bbox_inches='tight')
pl.show()