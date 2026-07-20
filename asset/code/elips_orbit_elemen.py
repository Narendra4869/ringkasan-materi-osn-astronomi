import math
from pathlib import Path
import matplotlib.pyplot as plt


def ellipse(a,b,e,theta):
    x = a*math.cos(theta)
    y = b*math.sin(theta)
    return x,y


def main():
    out = Path(__file__).parent.parent / 'images' / 'elips_orbit_elemen.png'
    a = 1.0
    e = 0.6
    b = a*math.sqrt(1-e*e)
    thetas = [i*math.pi/180 for i in range(0,361)]
    xs = [ellipse(a,b,e,t)[0] for t in thetas]
    ys = [ellipse(a,b,e,t)[1] for t in thetas]
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(xs, ys)
    # focus at (ae,0)
    ax.scatter([a*e], [0], color='orange', label='Focus (Sun)')
    ax.scatter([a], [0], color='C1')
    ax.text(a*e+0.02,0.02,'S (focus)')
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title('Elips Orbit dengan Elemen Geometris')
    fig.savefig(out, dpi=150)


if __name__=='__main__':
    main()
