from math import acos
from operator import mul

# oa = toVec(o, a), ob = toVec(o, b)

toVec = lambda p1, p2: (j - i for i, j in zip(p1, p2))


scale = lambda v, s: (i*s for i in v)


translate = lambda p, v: (pi + vi for pi, vi in zip(p, v))


dot = lambda v1, v2: sum(map(mul, v1, v2))


norm_sq = lambda v: sum(i*i for i in v)


angle = lambda oa, ob: acos(dot(oa, ob) / (norm_sq(oa) * norm_sq(ob))**0.5)


cross2d = lambda v1, v2: v1[0] * v2[1] - v1[1] * v2[0]


cross3d = lambda v1, v2: (v1[1] * v2[2] - v1[2] * v2[1],
                          v1[2] * v2[0] - v1[0] * v2[2],
                          v1[0] * v2[1] - v1[1] * v2[0])


dist = lambda p1, p2: sum((a - b)*(a - b) for a, b in zip(p1, p2))**0.5


def distToLine(p, a, b):
    ap, ab = toVec(a, p), toVec(a, b)

    u = dot(ap, ab) / norm_sq(ab)
    c = translate(a, scale(ab, u))

    return dist(p, c)


def distToSegment(p, a, b):
    ap, ab = toVec(a, p), toVec(a, b)
    u = dot(ap, ab) / norm_sq(ab)

    if u < 0:
        return dist(p, a)
    if u > 1:
        return dist(p, b)
    return distToLine(p, a, b)
