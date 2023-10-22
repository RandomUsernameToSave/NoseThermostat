import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

def plot_3d_trajectory_animation_with_balls(objet1_positions, objet2_positions):
    
    # Récupérez les coordonnées x, y et z de chaque objet
    x1, y1, z1 = objet1_positions
    x2, y2, z2 = objet2_positions

    min_x = min(np.min(x1), np.min(x2))
    max_x = max(np.max(x1), np.max(x2))
    min_y = min(np.min(y1), np.min(y2))
    max_y = max(np.max(y1), np.max(y2))
    min_z = min(np.min(z1), np.min(z2))
    max_z = max(np.max(z1), np.max(z2))
    # Créez une figure 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)
    ax.set_zlim(min_z, max_z)

    # Créez des boules pour représenter les objets
    ball1, = ax.plot([], [], [], 'bo', markersize=5, label='rH')
    ball2, = ax.plot([], [], [], 'ro', markersize=5, label='rCl')

    # Personnalisez le graphique
    ax.set_xlabel('Position X')
    ax.set_ylabel('Position Y')
    ax.set_zlabel('Position Z')
    ax.set_title('Trajectoire 3D de deux objets avec boules')
    ax.legend()

    # Fonction d'initialisation de l'animation
    def init():
        ball1.set_data([], [])
        ball1.set_3d_properties([])
        ball2.set_data([], [])
        ball2.set_3d_properties([])
        return ball1, ball2

    # Fonction d'animation
    def animate(i):
        ball1.set_data([x1[i]], [y1[i]])
        ball1.set_3d_properties([z1[i]])
        ball2.set_data([x2[i]], [y2[i]])
        ball2.set_3d_properties([z2[i]])
        return ball1, ball2

    # Créez l'animation
    animation = FuncAnimation(fig, animate, init_func=init, frames=len(x1), interval=10, blit=False)

    # Affichez l'animation
    plt.show()

