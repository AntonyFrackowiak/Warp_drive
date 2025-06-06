"""Lagrange_constant_velocity"""
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters
R = 1
sigma = 5
v_s = 0.9
t_0 = 0.0
pi= np.pi 
G = 1

# Grid
x = np.linspace(-1.5, 1.5, 200)
y = np.linspace(-1.5, 1.5, 200)
X, Y = np.meshgrid(x, y)

# Compute initial fields
def update_fields(X, Y, t):
    r_s = np.sqrt(X**2 + Y**2)
    W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))
    V_x = v_s * W_rs
    dV_x_dX = np.gradient(V_x, x, axis=1)
    dV_x_dY = np.gradient(V_x, y, axis=0)
    theta = dV_x_dX
    return theta, V_x, dV_x_dY

def compute_Omega2(theta0, dVx_dY, t):
    VS_Y = dVx_dY
    Omega_squared = ((-0.5 * VS_Y)**2) / (4 * (1 + theta0 * (t - t_0))**2)
    return Omega_squared

def compute_Sigma2(theta_t, Omega2):
    return (1/3) * theta_t**2 + Omega2


def compute_pi2(theta_t, Omega2, dVx_dY):
	VS_Y = dVx_dY
	pi2 = 1/(64 *pi**2*G**2) * (4 * Omega2**2 + Omega2 * theta_t + 1/8 *(VS_Y)**2)
	#pi2 = 2/3 * theta_t**2 + 2*Omega2
	return pi2
	
# Initial fields at t0
theta0, V_x0, dVx_dY0 = update_fields(X, Y, t_0)

# Setup figure with 3D subplots
fig = plt.figure(figsize=(7, 5))
ax_theta = fig.add_subplot(131, projection='3d')
ax_omega = fig.add_subplot(132, projection='3d')
ax_sigma = fig.add_subplot(133, projection='3d')
#ax_pi2   = fig.add_subplot(144, projection='3d')

# Labels
for ax, title, zlabel in zip([ax_theta, ax_omega, ax_sigma],
                             ["Θ(t,X)", "Ω²(t,X)", "Σ²(t,X)"],
                             ["Θ", "Ω²", "Σ²"]):   #, ax_pi2
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel(zlabel)
    ax.set_title(title)

#["Expansion Θ(t,X)", "Vorticity Ω²(t,X)", "Shear Scalar Σ²(t,X)"]

# Storage for surfaces
surfaces = [None, None, None] #, None]

# Animation function
def animate(t):
    global surfaces
    # Clear previous surfaces
    for surf in surfaces:
        if surf:
            surf.remove()

    # Recompute fields at time t
    theta_t = theta0 / (1 + theta0 * (t - t_0))
    Omega2 = compute_Omega2(theta0, dVx_dY0, t)
    Sigma2 = compute_Sigma2(theta_t, Omega2)
    #pi2   = compute_pi2(theta_t, Omega2,  dVx_dY0)
	

    #i = 2/3*theta_t**2 - (Sigma2*2)+ (Omega2*2) 
    #print("Test of we have 0 for i = ", i)
 
    
    # Plot all four        
    surfaces[0] = ax_theta.plot_surface(X, Y, theta_t, cmap='coolwarm', edgecolor='none',rstride=3, cstride=3)
    surfaces[1] = ax_omega.plot_surface(X, Y, Omega2, cmap='plasma', edgecolor='none',rstride=3, cstride=3) 
    surfaces[2] = ax_sigma.plot_surface(X, Y, Sigma2, cmap='viridis', edgecolor='none',rstride=3, cstride=3)
    #surfaces[3] = ax_pi2.plot_surface(X, Y, pi2, cmap='viridis', edgecolor='none',rstride=1, cstride=1)

    # Set z-axis limits for consistency
    ax_theta.set_zlim( np.min(theta_t)*1.1, np.max(theta_t)*1.1)
    ax_omega.set_zlim(0, np.max(Omega2)*1.1)
    ax_sigma.set_zlim(0, np.max(Sigma2)*1.1)
    #ax_pi2.set_zlim(0, np.max(pi2)*1.1)

    fig.suptitle(f"t = {t:.2f}", fontsize=16)


# Animate over time
anim = FuncAnimation(fig, animate, frames=np.linspace(0.0, 0.43, 44), interval=50)
"""


"""Lagrange_constant_velocity"""
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters
R = 1
sigma = 5
v_s = 0.9
t_0 = 0.0
pi= np.pi 
G = 1

# Grid
x = np.linspace(-1.5, 1.5, 200)
y = np.linspace(-1.5, 1.5, 200)
X, Y = np.meshgrid(x, y)

# Compute initial fields
def update_fields(X, Y, t):
    r_s = np.sqrt(X**2 + Y**2)
    W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))
    V_x = v_s * W_rs
    dV_x_dX = np.gradient(V_x, x, axis=1)
    dV_x_dY = np.gradient(V_x, y, axis=0)
    theta = dV_x_dX
    return theta, V_x, dV_x_dY

def compute_Omega2(theta0, dVx_dY, t):
    VS_Y = dVx_dY
    Omega_squared = ((-0.5 * VS_Y)**2) / (4 * (1 + theta0 * (t - t_0))**2)
    return Omega_squared

def compute_Sigma2(theta_t, Omega2):
    return (1/3) * theta_t**2 + Omega2


def compute_pi2(theta_t, Omega2, dVx_dY):
	VS_Y = dVx_dY
	pi2 = 1/(64 *pi**2) *4 * Omega2**2 + Omega2 * theta_t**2 
	#pi2 = 1/(64 *pi**2) * (5/2) * Omega2**2 + Omega2 * theta_t**2 
	#pi2 = 2/3 * theta_t**2 + 2*Omega2
	return pi2
	
# Initial fields at t0
theta0, V_x0, dVx_dY0 = update_fields(X, Y, t_0)

# Setup figure with 3D subplots
fig = plt.figure(figsize=(7, 5))
ax_theta = fig.add_subplot(141, projection='3d')
ax_omega = fig.add_subplot(142, projection='3d')
ax_sigma = fig.add_subplot(143, projection='3d')
ax_pi2   = fig.add_subplot(144, projection='3d')

# Labels
for ax, title, zlabel in zip([ax_theta, ax_omega, ax_sigma, ax_pi2],
                             ["Θ(t,X)", "Ω²(t,X)", "Σ²(t,X)","Π²(t,X)"],
                             ["Θ", "Ω²", "Σ²","Π²"]):  
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel(zlabel)
    ax.set_title(title)

#["Expansion Θ(t,X)", "Vorticity Ω²(t,X)", "Shear Scalar Σ²(t,X)"]

# Storage for surfaces
surfaces = [None, None, None, None]

# Animation function
def animate(t):
    global surfaces
    # Clear previous surfaces
    for surf in surfaces:
        if surf:
            surf.remove()

    # Recompute fields at time t
    theta_t = theta0 / (1 + theta0 * (t - t_0))
    Omega2 = compute_Omega2(theta0, dVx_dY0, t)
    Sigma2 = compute_Sigma2(theta_t, Omega2)
    pi2   = compute_pi2(theta_t, Omega2,  dVx_dY0)

    
    # Plot all four 
    surfaces[0] = ax_theta.plot_surface(X, Y, theta_t, cmap='coolwarm', edgecolor='none',rstride=3, cstride=3)
    surfaces[1] = ax_omega.plot_surface(X, Y, Omega2, cmap='plasma', edgecolor='none',rstride=3, cstride=3) 
    surfaces[2] = ax_sigma.plot_surface(X, Y, Sigma2, cmap='viridis', edgecolor='none',rstride=3, cstride=3)
    surfaces[3] = ax_pi2.plot_surface(X, Y, pi2, cmap='rainbow', edgecolor='none',rstride=3, cstride=3)

    # Set z-axis limits for consistency
    ax_theta.set_zlim( np.min(theta_t)*1.1, np.max(theta_t)*1.1)
    ax_omega.set_zlim(0, np.max(Omega2)*1.1)
    ax_sigma.set_zlim(0, np.max(Sigma2)*1.1)
    ax_pi2.set_zlim(0, np.max(pi2)*1.1)

    fig.suptitle(f"t = {t:.2f}", fontsize=16)


# Animate over time
anim = FuncAnimation(fig, animate, frames=np.linspace(0.0, 0.44, 50), interval=50)
plt.tight_layout()
plt.show()
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Paramètres
R = 1
sigma = 5
v_s = 0.9
t_0 = 0.0
pi = np.pi
G = 1

# Grille
x = np.linspace(-1.5, 1.5, 200)
y = np.linspace(-1.5, 1.5, 200)
X, Y = np.meshgrid(x, y)

# Fonction pour calculer les champs
def update_fields(X, Y, t):
    r_s = np.sqrt(X**2 + Y**2)
    W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))
    V_x = v_s * W_rs
    dV_x_dX = np.gradient(V_x, x, axis=1)
    dV_x_dY = np.gradient(V_x, y, axis=0)
    theta = dV_x_dX
    return theta, V_x, dV_x_dY

# Champs initiaux
theta0, V_x0, dVx_dY0 = update_fields(X, Y, t_0)

# Temps choisis
times = [0.0, 0.07, 0.25,0.4]

# Création de la figure

fig = plt.figure(figsize=(16, 4))
for i, t in enumerate(times):
    theta_t = theta0 / (1 + theta0 * (t - t_0))
    Omega2 = ((-0.5 * dVx_dY0)**2) / (4 * (1 + theta0 * (t - t_0))**2)
    Sigma2 = (1/3) * theta_t**2 + Omega2
    pi2 = 1/(64 *pi**2) *4* Omega2**2 + Omega2 * theta_t**2

    ax = fig.add_subplot(1, 4, i + 1, projection='3d')
    surf = ax.plot_surface(X, Y, pi2, cmap='rainbow', edgecolor='none', rstride=1, cstride=1)
    ax.set_title(f"Π² at t = {t:.1f}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Π²")
    ax.set_zlim(0, np.max(pi2)*1.1)
""""""
fig = plt.figure(figsize=(16, 4))
for i, t in enumerate(times):
    theta_t = theta0 / (1 + theta0 * (t - t_0))
    Omega2 = ((-0.5 * dVx_dY0)**2) / (4 * (1 + theta0 * (t - t_0))**2)
    Sigma2 = (1/3) * theta_t**2 + Omega2

    ax = fig.add_subplot(1, 4, i + 1, projection='3d')
    surf = ax.plot_surface(X, Y, Sigma2, cmap='viridis', edgecolor='none', rstride=1, cstride=1)
    ax.set_title(f"Σ² at t = {t:.1f}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Σ²")
    ax.set_zlim(0, np.max(Sigma2)*1.1)
""""""
plt.tight_layout()
plt.show()
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters
R = 1
sigma = 5
v_s = 0.9
t_0 = 0.0
pi = np.pi 
G = 1

# Grid
x = np.linspace(-1.5, 1.5, 200)
y = np.linspace(-1.5, 1.5, 200)
X, Y = np.meshgrid(x, y)

# Compute initial fields
def update_fields(X, Y, t):
    r_s = np.sqrt(X**2 + Y**2)
    W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))
    V_x = v_s * W_rs
    dV_x_dX = np.gradient(V_x, x, axis=1)
    dV_x_dY = np.gradient(V_x, y, axis=0)
    d2W_dx2 = np.gradient(np.gradient(W_rs, x, axis=1), x, axis=1)
    theta = dV_x_dX
    return theta, V_x, dV_x_dY, d2W_dx2, W_rs

def compute_Omega2(theta0, dVx_dY, t):
    VS_Y = dVx_dY
    Omega_squared = ((-0.5 * VS_Y)**2) / (4 * (1 + theta0 * (t - t_0))**2)
    return Omega_squared

def compute_Sigma2(theta_t, Omega2):
    return (1/3) * theta_t**2 + Omega2

def compute_pi2(theta_t, Omega2, dVx_dY):
    pi2 = 1/(64 * pi**2) * 4 * Omega2**2 + Omega2 * theta_t**2
    return pi2

def compute_pi_xx(theta0, t, d2W_dx2, Omega2):
    dVx_dt_dx = -v_s**2 * d2W_dx2 / (1 + theta0 * (t - t_0))**3
    pi_xx = (dVx_dt_dx - 3 * Omega2) / (12 * pi * G)
    return pi_xx

def compute_V_lagrangian(W_rs, theta0, t):
    return (v_s * W_rs) / (1 + theta0 * (t - t_0))

# Initial fields at t0
theta0, V_x0, dVx_dY0, d2W_dx2_0, W_rs_0 = update_fields(X, Y, t_0)

# Setup figure with 3D subplots
fig = plt.figure(figsize=(20, 5))
ax_theta = fig.add_subplot(231, projection='3d')
ax_omega = fig.add_subplot(232, projection='3d')
ax_sigma = fig.add_subplot(233, projection='3d')
ax_pi2   = fig.add_subplot(234, projection='3d')
ax_pixx  = fig.add_subplot(235, projection='3d')
ax_vlag  = fig.add_subplot(236, projection='3d')

# Labels and titles
axes = [ax_theta, ax_omega, ax_sigma, ax_pi2, ax_pixx, ax_vlag]
titles = ["Θ(t,X)", "Ω²(t,X)", "Σ²(t,X)", "Π²(t,X)", "πₓₓ(t,X)", "Vitesse Lagrangienne Vˣ(t,X)"]
zlabels = ["Θ", "Ω²", "Σ²", "Π²", "πₓₓ", "Vˣ"]

for ax, title, zlabel in zip(axes, titles, zlabels):
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel(zlabel)
    ax.set_title(title)

# Storage for surfaces
surfaces = [None] * 6

# Animation function
def animate(t):
    global surfaces
    for surf in surfaces:
        if surf:
            surf.remove()

    # Compute fields at time t
    theta_t = theta0 / (1 + theta0 * (t - t_0))
    Omega2 = compute_Omega2(theta0, dVx_dY0, t)
    Sigma2 = compute_Sigma2(theta_t, Omega2)
    pi2 = compute_pi2(theta_t, Omega2, dVx_dY0)
    pi_xx = compute_pi_xx(theta0, t, d2W_dx2_0, Omega2)
    V_lagrangian = compute_V_lagrangian(W_rs_0, theta0, t)

    # Plot surfaces
    surfaces[0] = ax_theta.plot_surface(X, Y, theta_t, cmap='coolwarm', edgecolor='none', rstride=3, cstride=3)
    surfaces[1] = ax_omega.plot_surface(X, Y, Omega2, cmap='plasma', edgecolor='none', rstride=3, cstride=3)
    surfaces[2] = ax_sigma.plot_surface(X, Y, Sigma2, cmap='viridis', edgecolor='none', rstride=3, cstride=3)
    surfaces[3] = ax_pi2.plot_surface(X, Y, pi2, cmap='rainbow', edgecolor='none', rstride=3, cstride=3)
    surfaces[4] = ax_pixx.plot_surface(X, Y, pi_xx*pi_xx, cmap='cividis', edgecolor='none', rstride=3, cstride=3)
    surfaces[5] = ax_vlag.plot_surface(X, Y, V_lagrangian, cmap='cubehelix', edgecolor='none', rstride=3, cstride=3)

    fig.suptitle(f"t = {t:.2f}", fontsize=16)

# Animate
anim = FuncAnimation(fig, animate, frames=np.linspace(0.0, 0.44, 50), interval=60)
plt.tight_layout()
plt.show()

