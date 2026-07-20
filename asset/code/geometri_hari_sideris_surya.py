import math
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'geometri_hari_sideris_surya.png'
    fig, ax = plt.subplots(figsize=(8,4))
    # two Earth positions A->B on orbit to show extra rotation
    ax.plot([0,1,2],[0,0,0], 'o-')
    ax.annotate('Position A', (0,0.02))
    ax.annotate('Position B', (1,0.02))
    ax.annotate('Position after 1 sideris', (2,0.02))
    ax.text(0.5, -0.1, 'Earth rotates ~360° relative stars\nbut must rotate ~360°+Δ relative Sun')
    ax.axis('off')
    fig.suptitle('Geometri Hari Sideris vs Hari Surya (schematic)')
    fig.savefig(out, dpi=150)


if __name__=='__main__':
    main()
