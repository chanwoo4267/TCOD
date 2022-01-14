import numpy as np
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width:int, height:int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F") # currently visible
        self.explored = np.full((width, height), fill_value=False, order="F") # explored before

    def in_bounds(self, x:int, y:int) -> bool:
        """Return True if x and y are insied of the bounds of this map """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console:Console) -> None:
        """
        Render Map
        If a tile is in visible area, then draw it with light colors
        If a tile isn't , but explored, then draw it with dark colors
        Otherwise, default is SHROUD
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored], 
            choicelist=[self.tiles["light"], self.tiles["dark"]], 
            default=tile_types.SHROUD
            )
