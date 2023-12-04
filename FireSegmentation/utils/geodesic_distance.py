from math import sqrt,pow

def geodesic_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt(pow((x1 - x2),2) + pow((y1 - y2),2))