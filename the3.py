from evaluator import *
from math import *

n = get_data()
forcex = 0
forcey = 0
fx = 0
fy = 0
ax = 0
ay = 0
def new_move():
    l = []
    global forcex, forcey, fx, fy, ax, ay, n

    for j in range(2, len(n)):
        l.append([])

    for i in range(2, len(n)):
        vx = n[i][3]
        vy = n[i][4]
        rx = vx * n[1]
        ry = vy * n[1]
        l[i - 2].append(rx)
        l[i - 2].append(ry)
        n[i][1] = n[i][1] + rx
        n[i][2] = n[i][2] + ry

    for i in range(2, len(n)):
        fx = 0
        fy = 0

        for k in range(2, len(n)):
            if n[i][1] != n[k][1]:
                forcex = n[0] * n[i][0] * n[k][0] * (n[k][1] - n[i][1]) / abs(pow(sqrt(((n[i][1] - n[k][1])**2) + ((n[i][2] - n[k][2])**2)), 3))
            if n[i][2] != n[k][2]:
                forcey = n[0] * n[i][0] * n[k][0] * (n[k][2] - n[i][2]) / abs(pow(sqrt(((n[i][1] - n[k][1])**2) + ((n[i][2] - n[k][2])**2)), 3))
            if n[i][1] == n[k][1]:
                forcex = 0
            if n[i][2] == n[k][2]:
                forcey = 0

            fx += forcex
            fy += forcey
        ax = fx / n[i][0]
        ay = fy / n[i][0]
        n[i][3] = n[i][3] + ax * n[1]
        n[i][4] = n[i][4] + ay * n[1]
    return l
