from typing import Tuple

import numpy as np

# Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)

# Tile struct used for statically define tile data type
tile_dt = np.dtype(
    [
        ("walkable", np.bool),      # True if can be walked over
        ("transparent", np.bool),   # True if doesnt block FOV
        ("dark", graphic_dt),       # Graphics when is not FOV
    ]
)

def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesnt matter
    walkable:int,
    transparent:int,
    dark:Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """helper function for defining individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)