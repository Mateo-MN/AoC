import numpy as np
from pathlib import Path
from itertools import product

mapa = []
with open(Path(__file__).parent / "4.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        mapa.append(list(line))

mapa = np.array(mapa)
total = 0
while True:
    padded = np.pad(mapa,1, constant_values=".")

    adjacent = np.zeros(mapa.shape)
    for i, j in product(range(-1, 2), repeat=2):
        if (i, j) == (0, 0):
            continue
        mask = padded[1+i : 1+i + mapa.shape[0], 
                      1+j : 1+j + mapa.shape[1]]
        adjacent += (mask == mapa).astype(int)

    removable_mask = ((mapa == "@") & (adjacent < 4))
    
    remove = np.count_nonzero(removable_mask)
    total += remove
    if total == remove:
        print("First part:", total)
    
    if remove == 0:
        print("Second part:", total)
        break
    
    mapa[removable_mask] = "."