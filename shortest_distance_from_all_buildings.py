from logo import LogoMixin
from tree import *
from manimlib.imports import *
from random import randint
from collections import defaultdict as dd
from copy import deepcopy

dot = Dot(TOP)
dot.set_fill(RED, opacity=0.8)

class MyMatrix(Matrix):

    def __init__(self, *args, brackets=True, **kwargs):
        self.use_brackets = brackets
        Matrix.__init__(self, *args, **kwargs)
        self.m = self.mob_matrix

    def add_brackets(self):
        if self.use_brackets:
            Matrix.add_brackets(self)

    def set(self, i, j, val, color=None):
        obj = TexMobject(val)
        obj.move_to(self.m[i][j])
        if color:
            obj.set_color(color)
        trans = Transform(self.m[i][j], obj)
        return trans

class ShortestDistanceFromAllBuildings(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)

        def parkour(TODO_COL, method):
            dist, visited, Q = dd(int), dd(set), set()

            for i, (hi, hj) in enumerate(H):
                self.play(mat.m[hi][hj].set_color, COLS[i])
                Q.add((hi, hj, hi, hj))
                visited[(hi, hj)].add((hi, hj))
                house_cols[(hi, hj)] = COLS[i]

            distances = []

            while Q:
                next_q = set()
                for hi, hj, i, j in Q:
                    for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        v_bounds = ni >= 0 and ni < len(M)
                        h_bounds = nj >= 0 and nj < len(M[0])
                        in_bounds = v_bounds and h_bounds
                        if in_bounds:
                            was_visited = (ni, nj) in visited[(hi, hj)]
                            blocked = M[ni][nj] == 2
                            house = M[ni][nj] == 1
                            if in_bounds and not (was_visited or blocked or house):
                                M[ni][nj] -= 1
                                dist[(hi, hj, ni, nj)] = dist[(hi, hj, i, j)] + 1
                                if M[ni][nj] == -len(H):
                                    distances.append(sum(dist[(a, b, ni, nj)] for a, b in H))
                                visited[(hi, hj)].add((ni, nj))
                                if method == 'show_total_dist':
                                    if M[ni][nj] == -len(H):
                                        dist_obj = TexMobject(sum(dist[(a, b, ni, nj)] for a, b in H))
                                        dist_obj.scale(0.3)
                                        dist_obj.next_to(mat.m[ni][nj], (LEFT+UP)*0.3)
                                        self.play(Write(dist_obj))
                                if method == 'color_individual':
                                    if house_cols[(hi, hj)] == TODO_COL:
                                        cell_dist = dist[(hi, hj, ni, nj)]
                                        dist_obj = TexMobject(cell_dist)
                                        dist_obj.scale(0.3)
                                        dist_obj.next_to(mat.m[ni][nj], ((RIGHT+UP)*(TODO_COL==RED) + (RIGHT+DOWN)*(TODO_COL==GREEN) + (LEFT+DOWN)*(TODO_COL==BLUE))*0.3)
                                        a = (20-cell_dist) / 20.0
                                        col = rgb_to_color([a*(TODO_COL==RED),a*(TODO_COL==GREEN),a*(TODO_COL==BLUE)])
                                        dist_obj.set_color(TODO_COL)
                                        col_method = ApplyMethod(mat.m[ni][nj].set_color, col)
                                        self.play(Write(dist_obj), col_method, run_time=0.2)
                                next_q.add((hi, hj, ni, nj))
                Q = next_q

        M = [
          [1,0,2,2,0,1],
          [0,0,0,2,0,0],
          [0,0,0,2,0,0],
          [2,2,0,0,0,0],
          [1,0,0,0,0,0]
        ]

        mat = MyMatrix(M, h_buff=2, v_buff=1.2)
        self.play(Write(mat, brackets=False))
        H = set([(i, j) for i in range(len(M)) for j in range(len(M[i])) if M[i][j] == 1])

        COLS = [RED, GREEN, BLUE]
        house_cols = {}
        for i, (hi, hj) in enumerate(H):
            self.play(mat.m[hi][hj].set_color, COLS[i], run_time=0.3)
            house_cols[(hi, hj)] = COLS[i]

        M_copy = deepcopy(M)

        parkour(RED, method='color_individual')
        parkour(GREEN, method='color_individual')
        parkour(BLUE, method='color_individual')

        self.play(mat.set_color, WHITE)

        self.wait(3)


class ShortestDistanceFromAllBuildingsTotal(ShortestDistanceFromAllBuildings):
    def construct(self):
        LogoMixin.construct(self)

        def parkour():
            dist, visited, Q = dd(int), dd(set), set()

            for i, (hi, hj) in enumerate(H):
                self.play(mat.m[hi][hj].set_color, COLS[i])
                Q.add((hi, hj, hi, hj))
                visited[(hi, hj)].add((hi, hj))
                house_cols[(hi, hj)] = COLS[i]

            distances = []

            while Q:
                next_q = set()
                for hi, hj, i, j in Q:
                    for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        v_bounds = ni >= 0 and ni < len(M)
                        h_bounds = nj >= 0 and nj < len(M[0])
                        in_bounds = v_bounds and h_bounds
                        if in_bounds:
                            was_visited = (ni, nj) in visited[(hi, hj)]
                            blocked = M[ni][nj] == 2
                            house = M[ni][nj] == 1
                            if in_bounds and not (was_visited or blocked or house):
                                M[ni][nj] -= 1
                                dist[(hi, hj, ni, nj)] = dist[(hi, hj, i, j)] + 1
                                if M[ni][nj] == -len(H):
                                    distances.append(sum(dist[(a, b, ni, nj)] for a, b in H))
                                visited[(hi, hj)].add((ni, nj))
                                if M[ni][nj] == -len(H):
                                    total_dist_obj = TexMobject(sum(dist[(a, b, ni, nj)] for a, b in H))
                                    total_dist_obj.scale(0.3)
                                    total_dist_obj.next_to(mat.m[ni][nj], (LEFT+UP)*0.3)
                                    self.play(Write(total_dist_obj))
                                cell_dist = dist[(hi, hj, ni, nj)]
                                dist_obj = TexMobject(cell_dist)
                                dist_obj.scale(0.3)
                                TODO_COL = house_cols[(hi, hj)]
                                dist_obj.next_to(mat.m[ni][nj], ((RIGHT+UP)*(TODO_COL==RED) + (RIGHT+DOWN)*(TODO_COL==GREEN) + (LEFT+DOWN)*(TODO_COL==BLUE))*0.3)
                                a = (20-cell_dist) / 20.0
                                col = rgb_to_color([a*(TODO_COL==RED),a*(TODO_COL==GREEN),a*(TODO_COL==BLUE)])
                                dist_obj.set_color(TODO_COL)
                                self.play(Write(dist_obj), run_time=0.2)
                                next_q.add((hi, hj, ni, nj))
                Q = next_q

        M = [
          [1,0,2,2,0,1],
          [0,0,0,2,0,0],
          [0,0,0,2,0,0],
          [2,2,0,0,0,0],
          [1,0,0,0,0,0]
        ]

        mat = MyMatrix(M, h_buff=2, v_buff=1.2)
        self.play(Write(mat, brackets=False))
        H = set([(i, j) for i in range(len(M)) for j in range(len(M[i])) if M[i][j] == 1])

        COLS = [RED, GREEN, BLUE]
        house_cols = {}
        for i, (hi, hj) in enumerate(H):
            self.play(mat.m[hi][hj].set_color, COLS[i], run_time=0.3)
            house_cols[(hi, hj)] = COLS[i]

        parkour()
        self.wait(3)

class ShortestDistanceFromAllBuildingsFinal(ShortestDistanceFromAllBuildings):
    def construct(self):
        LogoMixin.construct(self)

        def parkour():
            dist, visited, Q = dd(int), dd(set), set()

            for i, (hi, hj) in enumerate(H):
                self.play(mat.m[hi][hj].set_color, COLS[i])
                Q.add((hi, hj, hi, hj))
                visited[(hi, hj)].add((hi, hj))
                house_cols[(hi, hj)] = COLS[i]

            distances = []

            while Q:
                next_q = set()
                for hi, hj, i, j in Q:
                    for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        v_bounds = ni >= 0 and ni < len(M)
                        h_bounds = nj >= 0 and nj < len(M[0])
                        in_bounds = v_bounds and h_bounds
                        if in_bounds:
                            was_visited = (ni, nj) in visited[(hi, hj)]
                            blocked = M[ni][nj] == 2
                            house = M[ni][nj] == 1
                            if in_bounds and not (was_visited or blocked or house):
                                M[ni][nj] -= 1
                                dist[(hi, hj, ni, nj)] = dist[(hi, hj, i, j)] + 1
                                if M[ni][nj] == -len(H):
                                    distances.append(sum(dist[(a, b, ni, nj)] for a, b in H))
                                visited[(hi, hj)].add((ni, nj))
                                if M[ni][nj] == -len(H):
                                    total_dist_obj = TexMobject(sum(dist[(a, b, ni, nj)] for a, b in H))
                                    total_dist_obj.scale(0.3)
                                    total_dist_obj.next_to(mat.m[ni][nj], (LEFT+UP)*0.3)
                                else:
                                    total_dist_obj = None
                                cell_dist = dist[(hi, hj, ni, nj)]
                                dist_obj = TexMobject(cell_dist)
                                dist_obj.scale(0.3)
                                TODO_COL = house_cols[(hi, hj)]
                                dist_obj.next_to(mat.m[ni][nj], ((RIGHT+UP)*(TODO_COL==RED) + (RIGHT+DOWN)*(TODO_COL==GREEN) + (LEFT+DOWN)*(TODO_COL==BLUE))*0.3)
                                a = (20-cell_dist) / 20.0
                                v = M[ni][nj]
                                cola = [(ni, nj) in visited[(0, 0)], (ni, nj) in visited[(0, 5)], (ni, nj) in visited[(4, 0)]]
                                print(cola)
                                col = rgb_to_color(cola)
                                dist_obj.set_color(TODO_COL)
                                self.play(Write(dist_obj), mat.set(ni, nj, M[ni][nj], color=col), run_time=0.2)
                                if total_dist_obj:
                                    self.play(Write(total_dist_obj))
                                next_q.add((hi, hj, ni, nj))
                Q = next_q

        M = [
          [1,0,2,2,0,1],
          [0,0,0,2,0,0],
          [0,0,0,2,0,0],
          [2,2,0,0,0,0],
          [1,0,0,0,0,0]
        ]

        mat = MyMatrix(M, h_buff=2, v_buff=1.2)
        self.play(Write(mat, brackets=False))
        H = set([(i, j) for i in range(len(M)) for j in range(len(M[i])) if M[i][j] == 1])

        COLS = [RED, GREEN, BLUE]
        house_cols = {}
        for i, (hi, hj) in enumerate(H):
            self.play(mat.m[hi][hj].set_color, COLS[i], run_time=0.3)
            house_cols[(hi, hj)] = COLS[i]

        parkour()
        self.wait(3)
