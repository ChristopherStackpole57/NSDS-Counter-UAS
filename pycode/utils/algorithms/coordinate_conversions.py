import math

from typing import Tuple

def rae_xyz(rae: Tuple[float, float, float]) -> Tuple[float, float, float]:
    r, a, e = rae

    x = r * math.cos(e) * math.cos(a)
    y = r * math.cos(e) * math.sin(a)
    z = r * math.sin(e)

    return (x, y, z)