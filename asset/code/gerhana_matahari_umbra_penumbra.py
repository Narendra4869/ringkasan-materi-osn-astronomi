from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'gerhana_matahari_umbra_penumbra.png'
    fig, ax = plt.subplots(figsize=(8,3))
    # Sun (left large), Moon (middle), Earth (right)
    ax.scatter(0,0,s=2000,color='orange')
    ax.scatter(3,0,s=200,color='gray')
    ax.scatter(8,0,s=1200,color='C0')
    # draw umbra/penumbra cones as lines
    ax.plot([3,8.5],[0.25,0.6], color='k')
    ax.plot([3,8.5],[-0.25,-0.6], color='k')
    ax.plot([3,6.5],[0.15,0.4], color='k', linestyle='--')
    ax.plot([3,6.5],[-0.15,-0.4], color='k', linestyle='--')
    ax.text(2.8,-0.6,'Moon'); ax.text(8,-0.6,'Earth'); ax.text(-0.5,0.6,'Sun')
    ax.axis('off')
    fig.suptitle('Geometri Gerhana Matahari — Umbra & Penumbra (schematic)')
    fig.savefig(out, dpi=150)


if __name__=='__main__':
    main()
