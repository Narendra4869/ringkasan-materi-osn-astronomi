"""Run all diagram scripts to generate images into ../images/"""
import subprocess
from pathlib import Path


SCRIPTS = [
    'segitiga_bola_umum.py',
    'bola_langit_kelima_sistem.py',
    'segitiga_pzx.py',
    'orbit_bumi_empat_musim.py',
    'geometri_hari_sideris_surya.py',
    'kurva_analemma.py',
    'elips_orbit_elemen.py',
    'barycenter_bumi_bulan.py',
    'lima_titik_lagrange.py',
    'geometri_pasangsurut_bumi_bulan.py',
    'elemen_orbit_3d.py',
    'tiga_anomali.py',
    'gerhana_matahari_umbra_penumbra.py',
    'gerhana_bulan_umbra_penumbra.py'
]


def main():
    base = Path(__file__).parent
    code_dir = base
    for s in SCRIPTS:
        path = code_dir / s
        print('Running', path)
        subprocess.run(['python3', str(path)], check=True)


if __name__ == '__main__':
    main()
