import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.integrate import odeint

def harmonic_motion_damping(y, t, omega, damping):
    dydt = [y[1], -2 * damping * omega * y[1] - omega**2 * y[0]]
    return dydt

def simulate_harmonic_motion(omega, damping, initial_conditions, time):
    result = odeint(harmonic_motion_damping, initial_conditions, time, args=(omega, damping))
    return result

def update(val):
    damping = damping_slider.val
    displacement = simulate_harmonic_motion(omega, damping, initial_conditions, time)
    line.set_ydata(displacement[:, 0])
    fig.canvas.draw_idle()

# Set the parameters
omega = 2 * np.pi  # Angular frequency
initial_damping = 0.1  # Initial damping coefficient
initial_conditions = [1.0, 0.0]

# Set time points for simulation
time = np.linspace(0, 10, 1000)

# Create the initial plot
displacement = simulate_harmonic_motion(omega, initial_damping, initial_conditions, time)
fig, ax = plt.subplots()
line, = ax.plot(time, displacement[:, 0], label='Displacement')

# Add a damping coefficient slider
ax_damping = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
damping_slider = Slider(ax_damping, 'Damping Coefficient', 0.1, 2.0, valinit=initial_damping)
damping_slider.on_changed(update)

# Customize the plot
plt.title(f'Simple Harmonic Motion with Damping (Damping Coefficient: {initial_damping})')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
