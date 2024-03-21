import sys
import os
from ase.io import read, iread, write
from ase.io.trajectory import Trajectory

if os.path.exists("vasp.xyz"):
  os.remove("vasp.xyz")

traj = iread(sys.argv[1], index = ":")
frame = 0
for atoms in traj:
    write('vasp.xyz', atoms, append = True)
    frame += 1
    print(f"Processed frame {frame}")
