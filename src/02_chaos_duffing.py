import numpy as np
from scipy.integrate import solve_ivp
from matplotlib.widgets import Button, Slider
import matplotlib.pyplot as plt
from numpy.random import random

colors = [['dodgerblue', 'indigo'], ['orangered', 'sienna'], ['gold', 'olive']]
x_0, v_0 = 0, 0.15
amplitude_0 = 7
t_0 = 8000

a, b = 0, 200
t = np.linspace(a, b, 10000)

def duffing(t, xv, amplitude):
  x, v = xv
  b, a, c, omega = 1, 1, 0.2, 0.213 * 2 * np.pi
  return [v, b * x - a * x**3 - c * v + amplitude * np.cos(omega * t)]

def equilibrium(t, xv):
  x, v = xv
  b, a, c, omega = 1, 1, 0.2, 0.213 * 2 * np.pi
  return [v, b * x - a * x**3 - c * v]

def solve_system(amplitude_value):
  return solve_ivp(duffing, [a, b], [x_0, v_0], t_eval=t, args=(amplitude_value,))

def find_equilibrium(amplitude_value):
  return solve_ivp(equilibrium, [a, b], [x_0, v_0], t_eval=t, args=(amplitude_value,))

def equ_points():
  points = []
  for _ in range(1, 100):
    equ = solve_ivp(equilibrium, [a, b], [x_0 + random(), 20 * v_0 * random()], t_eval=t)
    points.append(equ.y[:, -1])
  return points

points = equ_points()
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

fig, ax = plt.subplots()
sol = solve_system(amplitude_0)
line, = ax.plot(sol.y[0][t_0:], sol.y[1][t_0:])
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-3, 3)
ax.set_xlabel('x(t)')
ax.set_ylabel('v(t)')
fig.subplots_adjust(left=0.25, bottom=0.25)

# Horizontal slider to control the amplitude
ax_amplitude = fig.add_axes([0.25, 0.1, 0.65, 0.03])
amplitude_slider = Slider(
  ax=ax_amplitude,
  label='Amplitude',
  valmin=0,
  valmax=1,
  valinit=amplitude_0,)

# The function to be called anytime a slider's value changes
def update(val):
  sol = solve_system(amplitude_slider.val)
  line.set_xdata(sol.y[0][t_0:])
  line.set_ydata(sol.y[1][t_0:])
  fig.canvas.draw_idle()

# register the update function with each slider
amplitude_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
  amplitude_slider.reset()
    
button.on_clicked(reset)
plt.show()