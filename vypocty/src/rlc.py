from scipy.integrate import odeint
import pylab as pl
import numpy as np
import math

pl.rcParams['figure.figsize'] = 11, 3.5
pl.rcParams['font.size'] = 20
pl.rcParams['xtick.labelsize'] = 20
pl.rcParams['ytick.labelsize'] = 20
pl.rcParams['legend.fontsize'] = 20

U0 = 10
L = 1e-3
C = 1e-6
Rk = 2*math.sqrt(L/C)
Rape = 3*Rk
Rmez = Rk
Rkmit = Rk/4

print(Rk)

# initial conditions
y0 = [0, 0]
def func_ape(y, t):
    return [U0/L - Rape*y[0]/L - y[1]/L, y[0]/C]
def func_mez(y, t):
    return [U0/L - Rmez*y[0]/L - y[1]/L, y[0]/C]
def func_kmit(y, t):
    return [U0/L - Rkmit*y[0]/L - y[1]/L, y[0]/C]
    
t = np.arange(0, 5e-4, 5e-4/300)
yape = odeint(func_ape, y0, t)
ymez = odeint(func_mez, y0, t)
ykmit = odeint(func_kmit, y0, t)

# chart
pl.close()
pl.plot(t, yape[:,0], label='$\mathrm{aperiodicky~dej}$')
pl.plot(t, ymez[:,0], label='$\mathrm{mez~aperiodicity}$')
pl.plot(t, ykmit[:,0], label='$\mathrm{kmitavy~dej}$')
ax = pl.gca()
ax.ticklabel_format(style='sci', scilimits=(0,0), axis='x')
pl.grid(True)
pl.xlabel("$t\,\mathrm{(s)}$")
pl.ylabel("$i_\mathrm{L}\,\mathrm{(A)}$")
pl.legend()
pl.savefig('obvod_rlc_proud.pdf', bbox_inches='tight')
#pl.show()

pl.close()
pl.plot(t, yape[:,1], label='$\mathrm{aperiodicky~dej}$')
pl.plot(t, ymez[:,1], label='$\mathrm{mez~aperiodicity}$')
pl.plot(t, ykmit[:,1], label='$\mathrm{kmitavy~dej}$')
ax = pl.gca()
ax.ticklabel_format(style='sci', scilimits=(0,0), axis='x')
pl.grid(True)
pl.xlabel("$t\,\mathrm{(s)}$")
pl.ylabel("$u_\mathrm{C}\,\mathrm{(V)}$")
pl.legend(loc='lower right')
pl.savefig('obvod_rlc_napeti.pdf', bbox_inches='tight')
#pl.show()

"""
pl.close()
# pl.plot(t, U0*ykmit[:,0], label='$\mathrm{zdroj}$')
# pl.plot(t, Rkmit*ykmit[:,0]**2, label='$\mathrm{rezistor}$')
pl.plot(t, 0.5*L*ykmit[:,0]**2, label='$\mathrm{induktor}$')
pl.plot(t, 0.5*C*ykmit[:,1]**2, label='$\mathrm{kapacitor}$')
ax = pl.gca()
ax.ticklabel_format(style='sci', scilimits=(0,0), axis='x')
pl.grid(True)
pl.xlabel("$t\,\mathrm{(s)}$")
pl.ylabel("$u_\mathrm{C}\,\mathrm{(V)}$")
pl.legend(loc='lower right')
pl.savefig('obvod_rlc_napeti.pdf', bbox_inches='tight')
pl.show()
"""