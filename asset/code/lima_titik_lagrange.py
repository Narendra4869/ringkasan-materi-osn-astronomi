import math
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'lima_titik_lagrange.png'
    fig, ax = plt.subplots(figsize=(6,4))
    # primary bodies
    ax.scatter(-1,0,s=300,color='orange'); ax.text(-1,0.2,'M1')
    ax.scatter(1,0,s=100,color='C0'); ax.text(1,0.2,'M2')
    # L1 between
    ax.scatter(0.3,0,color='k'); ax.text(0.3,0.1,'L1')
    ax.scatter(-0.3,0,color='k'); ax.text(-0.3,0.1,'L3')
    ax.scatter(1.5,0,color='k'); ax.text(1.5,0.1,'L2')
    ax.scatter(0,0.866,color='k'); ax.text(0,0.96,'L4')
    ax.scatter(0,-0.866,color='k'); ax.text(0,-0.96,'L5')
    ax.set_aspect('equal'); ax.axis('off')
    fig.suptitle('Lima Titik Lagrange (schematic)')
    fig.savefig(out,dpi=150)


if __name__=='__main__':
    main()
