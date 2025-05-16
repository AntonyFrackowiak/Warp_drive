"""caustic_constant_velocity"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Initial parameters
R = 1
sigma = 5
v_s = 0.9
t_0 = 0.0
Y = 0.0

# Define a range for t
t = np.linspace(-1.4, 1.4, 500)

# List of different X values
X_values = [-1.5, -1.4,-1.3, -1.2,-1.15, -1.01, -1.0,-0.99, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.7, 0.8, 0.99, 1, 1.01, 1.15, 1.2, 1.3, 1.4,1.5]

# Create figure and axis for the main plot
fig, ax_main = plt.subplots(figsize=(10, 6))

# Plot the trajectories on the main axis
for X in X_values:
    r_s = np.sqrt(X**2 + Y**2)
    W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))
    x = X + v_s * W_rs * (t - t_0)
    ax_main.plot(x, t, linewidth=1, label=f'X = {X}')

ax_main.set_xlabel('Position (x)')
ax_main.set_ylabel('Time (t)')
ax_main.legend()

# Add dotted grid to the main plot
ax_main.grid(True, linestyle=':', alpha=0.5)

plt.show()


#or this 


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Initial parameters
R = 1
sigma = 5
v_s = 0.9
t_0 = 0.0
Y = 0.0

# Define a range for t
t = np.linspace(-1.5, 1.5, 500)

# List of different X values
X_values = [-1.4,-1.35, -1.3,-1.25, -1.2,-1.15, -1.1,-1.05, -1.0,-0.95, -0.9,-0.85, -0.8, -0.75, -0.7,-0.65, -0.6, -0.55, -0.5,-0.45, -0.4,-0.35, -0.3,-0.25, -0.2,-0.15, -0.1 ,-0.05, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.90, 0.95, 0.99, 1, 1.01, 1.05, 1.10, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6,1.65, 1.7,1.75, 1.8 ,1.85, 1.9 ,1.95, 2]

# Create figure and axis for the main plot
fig, ax_main = plt.subplots(figsize=(10, 6))

# Plot the trajectories on the main axis
for X in X_values:
    r_s = np.sqrt(X**2 + Y**2)
    W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))
    x = X + v_s * W_rs * (t - t_0)
    ax_main.plot(x, t, linewidth=0.5, color='black')

ax_main.set_xlabel('Position (x)')
ax_main.set_ylabel('Time (t)')
#ax_main.legend()

# Add dotted grid to the main plot
ax_main.grid(True, linestyle=':', alpha=0.5)

# Set limits for the zoomed-in region
zoom_xmin, zoom_xmax = 1.18, 1.22
zoom_ymin, zoom_ymax = 0.40, 0.50

# Create axis for the zoomed-in plot
ax_zoom = fig.add_axes([0.35, 0.45, 0.2, 0.3])  # [left, bottom, width, height]
ax_zoom.set_xlim(zoom_xmin, zoom_xmax)
ax_zoom.set_ylim(zoom_ymin, zoom_ymax)
ax_zoom.set_title('Position of the caustic')

# Plot the zoomed-in trajectories on the zoom axis
for X in X_values:
    r_s = np.sqrt(X**2 + Y**2)
    W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))
    x = X + v_s * W_rs * (t - t_0)
    if 0.8 <= X <= 1.15:  # Add label only for X in the specified range
        ax_zoom.plot(x, t, linewidth=0.6, label=f'X = {X}')
    else:
        ax_zoom.plot(x, t, linewidth=0.6)
        
plt.xticks(np.arange(zoom_xmin,zoom_xmax,0.01))
ax_zoom.legend(bbox_to_anchor=(-1, 1.6), loc='upper left', ncol=10)

# Add grid to the zoomed-in plot
ax_zoom.grid(True, linestyle=':',  alpha=0.5)

# Indicate the zoomed region in ax_main
ax_main.indicate_inset_zoom(ax_zoom, linewidth=1)

plt.show()
