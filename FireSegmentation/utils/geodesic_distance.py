from math import sqrt,pow,dist

def geodesic_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt(pow((x1 - x2),2) + pow((y1 - y2),2))


def euclidean_distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    """
    This function calculates the Euclidean distance between two points in 2D space.
    Each point is a tuple of two floats representing the x and y coordinates.
    It returns the distance as a float.
    """
    return dist(point1, point2)