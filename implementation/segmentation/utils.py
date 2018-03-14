from math import sqrt


def point_distance_2d(x1, y1, x2, y2):
    """
    Euclidean distance between 2 points in 2d space
    """
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def point_distance_3d(x1, y1, z1, x2, y2, z2):
    """
    Euclidean distance between 2 points in 3d space
    """
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    z1 = int(z1)
    z2 = int(z2)
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))


def feature_distance_5d(r1, g1, b1, r2, g2, b2, x1, y1, x2, y2):
    """
    Euclidean distance between 2 points in 5d space

    r, g, b should be the rgb coordinates ; which are scaled
    x,y are the positions
    """
    r1 = 0.5 * int(r1)
    r2 = 0.5 * int(r2)
    g1 = 0.5 * int(g1)
    g2 = 0.5 * int(g2)
    b1 = 0.5 * int(b1)
    b2 = 0.5 * int(b2)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    return sqrt(((r2 - r1) ** 2) + ((g2 - g1) ** 2) + ((b2 - b1) ** 2) + ((x2 - x1) ** 2) + ((y2 - y1) ** 2))