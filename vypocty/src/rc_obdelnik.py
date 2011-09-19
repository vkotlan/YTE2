from scipy.integrate import odeint
import pylab as pl
import numpy as np

pl.rcParams['figure.figsize'] = 11, 4
pl.rcParams['font.size'] = 20
pl.rcParams['xtick.labelsize'] = 20
pl.rcParams['ytick.labelsize'] = 20
pl.rcParams['legend.fontsize'] = 20

R1 = 2e3
R2 = 0.5e3
C = 1e-6
U0 = 10

# initial condition
y0 = [0]

print (R1*C)/5.0

def func(y, t):
    if (t % (R1*C)/5.0 < (R1*C)/5.0/1.5):
        return [(U0 - y[0])/(R1*C) - y[0]/(R2*C)]
    else:
        return [( 0 - y[0])/(R1*C) - y[0]/(R2*C)]

t = np.arange(0, 4*R1*C, R1*C/100)
y = odeint(func, y0, t)

# chart
pl.close()
fig = pl.figure()
ax1 = fig.add_subplot(111)
ax1.plot(t, U0 * (t % (R1*C)/5.0 < (R1*C)/5.0/1.5), 'r', label="$u_\mathrm{0}$")
ax1.set_ylim(0, 11)
ax1.set_ylabel("$u_\mathrm{0}\,\mathrm{(V)}$")

ax2 = ax1.twinx()
ax2.plot(t, y, 'b', label='$u_\mathrm{C}$')
ax2.ticklabel_format(style='sci', scilimits=(0,0), axis='x')
ax2.set_ylim(0, 2.5)
ax2.set_ylabel("$u_\mathrm{C}\,\mathrm{(V)}$")
ax2.legend(loc="lower right")
pl.grid(True)
pl.xlabel("$t\,\mathrm{(s)}$")
pl.savefig('obvod_rc_obdelnik.pdf', bbox_inches='tight')
pl.show()