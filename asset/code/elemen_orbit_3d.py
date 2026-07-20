import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    out = Path(__file__).parent.parent / 'images' / 'elemen_orbit_3d.png'
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')
    # simple inclined orbit
    a=1.0; e=0.3; b=a*np.sqrt(1-e*e)
    t = np.linspace(0,2*np.pi,200)
    x = a*np.cos(t)
    y = b*np.sin(t)
    z = 0.4*np.sin(t)  # simulate inclination
    ax.plot(x,y,z)
    ax.scatter([0],[0],[0], color='orange', s=80)
    ax.set_axis_off()
    fig.suptitle('Elemen Orbit dalam Ruang (schematic)')
    fig.savefig(out, dpi=150)


if __name__=='__main__':
    main()
