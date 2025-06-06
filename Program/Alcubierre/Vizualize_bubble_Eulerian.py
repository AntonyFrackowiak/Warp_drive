"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter

# Paramètres
R = 1.0
sigma = 5.0
g = 9.81
l = 0
t_0 = 0

# Vitesse warp
def v_s(t):
    return 0.9 + g * t

# Grille 2D
x_vals = np.linspace(10, 30, 500)
y_vals = np.linspace(-2.5, 2.5, 500)
X, Y = np.meshgrid(x_vals, y_vals)

# Fonction W(r_s)
def compute_W_rs(t):
	center = l + v_s(t) * t
	# Estimation initiale de W
	r_s_guess = np.sqrt((X - center)**2 + Y**2)
	W_guess = (np.tanh(sigma * (r_s_guess + R)) - np.tanh(sigma * (r_s_guess - R))) / (2 * np.tanh(sigma * R))

	# x dynamique dépendant du champ
	x_dynamic = X + v_s(t) * W_guess * (t - t_0)

	# Recalcul de r_s et de W(r_s) final
	r_s = np.sqrt((x_dynamic - center)**2 + Y**2)
	W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))

	return W_rs

# Figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')
ax.set_title("Fonction de forme W(rₛ)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("W(rₛ)")

# Premier frame
W_rs_init = compute_W_rs(0)
surf = ax.plot_surface(X, Y, W_rs_init, cmap='plasma', rstride=4, cstride=4, linewidth=0, antialiased=True)

# Fonction d'animation
def animate(t):
    ax.clear()
    W_rs = compute_W_rs(t)
    ax.set_title(f"W(rₛ) à t = {t:.2f}s")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("W(rₛ)")
    ax.set_zlim(0, 1.1)
    surf = ax.plot_surface(X, Y, W_rs, cmap='plasma', rstride=4, cstride=4, linewidth=0, antialiased=True)
    return surf,

# Animation
anim = FuncAnimation(fig, animate, frames=np.linspace(1, 1.5, 60), interval=50, blit=False)

# Export GIF (décommente si besoin)
# writer = PillowWriter(fps=10)
# anim.save("W_rs_animation.gif", writer=writer)

plt.tight_layout()
plt.show()

"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# === PARAMÈTRES ===
R = 1.5        # Rayon de la bulle warp
sigma = 5.0    # Échelle de transition de W
g = 9.81       # Accélération (inutile ici car v_s est constant)
l = 0          # Centre initial
t_0 = 0        # Temps initial
R0 = 1.0       # Rayon initial de la sphère

# === VITESSE DE LA BULLE WARP (constante ici) ===
def v_s(t):
    return 0.9

# === COORDONNÉES SPHÉRIQUES INITIALES ===
phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

# Coord sphériques standard
X0 = R0 * np.sin(phi) * np.cos(theta)
Y0 = R0 * np.sin(phi) * np.sin(theta)
Z0 = R0 * np.cos(phi)

# === FONCTION POUR CALCULER LA SPHÈRE DÉFORMÉE AVEC x_dynamic ===
def compute_deformed_sphere(t):
    center = l + v_s(t) * t

    # Estimation initiale de r_s
    r_s_base = np.sqrt((X0 - center)**2 + Y0**2 + Z0**2)
    W_rs_guess = (np.tanh(sigma * (r_s_base + R)) - np.tanh(sigma * (r_s_base - R))) / (2 * np.tanh(sigma * R))

    # Correction dynamique
    x_dynamic = X0 + v_s(t) * W_rs_guess * (t - t_0)

    # r_s corrigé et W final
    r_s = np.sqrt((x_dynamic - center)**2 + Y0**2 + Z0**2)
    W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))

    # Appliquer la déformation radiale
    R_def = R0 * W_rs
    X_def = R_def * np.sin(phi) * np.cos(theta)
    Y_def = R_def * np.sin(phi) * np.sin(theta)
    Z_def = R_def * np.cos(phi)

    return X_def, Y_def, Z_def, W_rs

# === FIGURE INITIALE ===
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])

# === ANIMATION ===
def animate(t):
    ax.clear()
    X_def, Y_def, Z_def, W_rs = compute_deformed_sphere(t)

    ax.plot_surface(X_def, Y_def, Z_def,
                    facecolors=plt.cm.plasma(W_rs),
                    rstride=1, cstride=1, antialiased=True, shade=False)

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_title(f"Déformation de la sphère W(rₛ), t = {t:.2f}s")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    return []

frames = np.linspace(0, 5, 50)
ani = FuncAnimation(fig, animate, frames=frames, interval=80, blit=False)

plt.tight_layout()
plt.show()

# === POUR SAUVEGARDER EN GIF ===
# from matplotlib.animation import PillowWriter
# writer = PillowWriter(fps=10)
# ani.save("deformation_sphere_Wrs.gif", writer=writer)

