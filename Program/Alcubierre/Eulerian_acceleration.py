import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Constantes
G = 1
R = 1.0
sigma = 5.0
v_s = 0.9

# Grille étendue 3D
x = np.linspace(-0.5, 2.4, 200)
y = np.linspace(-1.5, 1.5, 200)
z = np.linspace(-1.5, 1.5, 200)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')  # Grille 3D

def update_fields(t, dt=1e-70):
    r_s = np.sqrt((X - v_s * t)**2 + Y**2 + Z**2)
    W_rs = (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / (2 * np.tanh(sigma * R))
    V_x = v_s * W_rs

    # V_x(t + dt)
    r_s_dt = np.sqrt((X - v_s * (t + dt))**2 + Y**2 + Z**2)
    W_rs_dt = (np.tanh(sigma * (r_s_dt + R)) - np.tanh(sigma * (r_s_dt - R))) / (2 * np.tanh(sigma * R))
    V_x_dt = v_s * W_rs_dt

    # ∂_i V_x(t)
    dVx_dx = np.gradient(V_x, x, axis=0)
    dVx_dy = np.gradient(V_x, y, axis=1)
    dVx_dz = np.gradient(V_x, z, axis=2)

    # ∂_i V_x(t+dt)
    dVx_dx_dt = np.gradient(V_x_dt, x, axis=0)
    dVx_dy_dt = np.gradient(V_x_dt, y, axis=1)
    dVx_dz_dt = np.gradient(V_x_dt, z, axis=2)

    # ∂_t(∂_i V_x) ≈ (∂_i V_x(t+dt) - ∂_i V_x(t)) / dt
    ddt_dVx_dx = (dVx_dx_dt - dVx_dx) / dt
    ddt_dVx_dy = (dVx_dy_dt - dVx_dy) / dt
    ddt_dVx_dz = (dVx_dz_dt - dVx_dz) / dt

    # (V ⋅ ∇)(∂_i V_x) ≈ V_x * ∂_x(∂_i V_x)
    d2Vx_dxdx = np.gradient(dVx_dx, x, axis=0)
    d2Vx_dydx = np.gradient(dVx_dy, x, axis=0)
    d2Vx_dzdx = np.gradient(dVx_dz, x, axis=0)

    conv_dVx_dx = V_x * d2Vx_dxdx
    conv_dVx_dy = V_x * d2Vx_dydx
    conv_dVx_dz = V_x * d2Vx_dzdx

    Dt_dVx_dx = ddt_dVx_dx + conv_dVx_dx
    Dt_dVx_dy = ddt_dVx_dy + conv_dVx_dy
    Dt_dVx_dz = ddt_dVx_dz + conv_dVx_dz

    # A_x = V_x * ∂_x V_x
    A_x = V_x * dVx_dx

    # ∂_i A_x = ∂_i (V_x * ∂_x V_x) = ∂_i V_x * ∂_x V_x + V_x * ∂_i∂_x V_x
    d2Vx_dxdy = np.gradient(dVx_dx, y, axis=1)
    d2Vx_dxdz = np.gradient(dVx_dx, z, axis=2)

    dA_dx = dVx_dx * dVx_dx + V_x * d2Vx_dxdx
    dA_dy = dVx_dy * dVx_dx + V_x * d2Vx_dxdy
    dA_dz = dVx_dz * dVx_dx + V_x * d2Vx_dxdz

    norm_A = np.sqrt(dA_dx**2 + dA_dy**2 + dA_dz**2)
    
    
    test = (X-v_s*t)/r_s_dt *dA_dx + Y/ r_s_dt * dA_dy+ Z / r_s_dt * dA_dz
    dW_dr = (sigma / (2 * np.tanh(sigma * R))) * (np.tanh(sigma * (r_s - R))**2 - np.tanh(sigma * (r_s + R))**2)

    
    return V_x_dt, Dt_dVx_dx, Dt_dVx_dy, Dt_dVx_dz, dA_dx, dA_dy, dA_dz, norm_A, W_rs_dt, dVx_dx, test, dW_dr


# --- FIGURE PLOT ---
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(12, 10))  # Taille globale
gs = gridspec.GridSpec(1, 3, figure=fig, height_ratios=[ 0.2])
ax1 = fig.add_subplot(gs[0, 0], projection='3d')
ax2 = fig.add_subplot(gs[0, 1], projection='3d')
ax3 = fig.add_subplot(gs[0, 2], projection='3d')
#ax4 = fig.add_subplot(gs[0, 3])  


# --- Animation ---
def animate(t):
    V_x_dt, Dt_dVx_dx, Dt_dVx_dy, Dt_dVx_dz, dA_dx, dA_dy, dA_dz, norm_A, W_rs_dt, dVx_dx, test, dW_dr= update_fields(t)

    # Indices y=0 et z=0 pour affichage 2D dans l'espace 3D
    idx_x0= np.argmin(np.abs(x - 0))
    idx_y0 = np.argmin(np.abs(y - 0))
    idx_z0 = np.argmin(np.abs(z - 0))

    for ax in [ax1, ax2, ax3]:
        ax.cla()

 
    """   
    ax1.plot_surface(X[:, idx_y0, :], Z[:, idx_y0, :], V_x_dt[:, idx_y0, :], cmap='RdYlBu',rstride=1, cstride=1)
    ax1.set_xlabel("x")
    ax1.set_ylabel("z")
    #ax1.set_zlabel(r"$V_x$")
    ax1.set_title(r"$V_S(t,x^k)$",fontsize = 20)
    
    ax2.plot_surface(X[:, idx_y0, :], Z[:, idx_y0, :], v_s *dW_dr[:, idx_y0, :], cmap='RdYlBu',rstride=1, cstride=1)
    ax2.set_xlabel("x")
    ax2.set_ylabel("z")
    #ax2.set_zlabel(r"$\frac{\partial V_S(t,x^k)}{\partial r_S}$")
    ax2.set_zlim(top=-2.5, bottom=0)  
    ax2.set_title(r"$\partial_{r_S} V_S(t,x^k)$",fontsize = 20)
    
   
    ax3.plot_surface(X[:, idx_y0, :], Z[:, idx_y0, :], test[:, idx_y0, :], cmap='nipy_spectral',rstride=1, cstride=1)
    ax3.set_xlabel("x")
    ax3.set_ylabel("z")
    #ax3.set_zlabel(r"$\frac{\partial A_S(t,x^k)}{\partial r_S}$")
    ax3.set_title(r"$\partial_{r_S} A_S(t,x^k)$", fontsize = 20)
   
    ax4.cla()
    im = ax4.imshow(test[:, idx_y0, :].T, 
                    extent=[z.min(), z.max(), x.min(), x.max()],
                    origin='lower',
                    aspect='equal',
                    cmap='nipy_spectral')
    ax4.set_xlabel("x")
    ax4.set_ylabel("z")
    ax4.set_title(r"$\partial_{r_S} A_S(t,x^k)$", fontsize=20)
    
    """
    ax1.plot_surface(X[:, idx_y0, :], Z[:, idx_y0, :], Dt_dVx_dx[:, idx_y0, :], cmap='viridis',rstride=4, cstride=4)
    ax1.set_xlabel("x")
    ax1.set_ylabel("z")
    #ax1.set_zlabel(r"$\frac{d}{dt} \partial_x V_S$")
    ax1.set_title(r"$\frac{d}{dt} \partial_x V_S$",fontsize = 25)

    ax2.plot_surface(X[:, idx_y0, :], Z[:, idx_y0, :], dA_dx[:, idx_y0, :], cmap='viridis',rstride=4, cstride=4)
    ax2.set_xlabel("x")
    ax2.set_ylabel("z")
    #ax2.set_zlabel(r"$\partial_x A_x$")
    ax2.set_title(r"$\partial_x A_S$",fontsize = 25)
   
    ax3.plot_surface(X[:, idx_y0, :], Z[:, idx_y0, :],  (dA_dx - Dt_dVx_dx)[:, idx_y0 , :], cmap='RdYlBu',rstride=1, cstride=1)
    ax3.set_xlabel("x")
    ax3.set_ylabel("z")
    #ax3.set_zlabel(r"$\partial_x A_x - \partial_t \partial_x V_S = \Theta^2$")
    ax3.set_title(r"$\partial_x A_S - \frac{d}{dt}\partial_x V_S = \Theta^2$",fontsize = 25)  
    
    
    
    return []

# Lancer animation
anim = FuncAnimation(fig, animate, frames=np.linspace(1, 1, 1), interval=1000, blit=False)

plt.tight_layout()
fig.subplots_adjust(wspace=0.3, hspace=0.3)

plt.show()
