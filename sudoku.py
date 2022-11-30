from manimlib.imports import *
from time import time
from logo import LogoMixin

from collections import defaultdict as ddict
from collections import deque
from itertools import product
from random import shuffle, randint, seed
from collections import defaultdict


class RawSudoku(list):
    def __init__(self, fill=False):
        if fill:
            data = [
                [".", ".", "3", "8", ".", ".", "4", ".", "."],
                [".", ".", ".", ".", "1", ".", ".", "7", "."],
                [".", "6", ".", ".", ".", "5", ".", ".", "9"],
                [".", ".", ".", "9", ".", ".", "6", ".", "."],
                [".", "2", ".", ".", ".", ".", ".", "1", "."],
                [".", ".", "4", ".", ".", "3", ".", ".", "2"],
                [".", ".", "2", ".", ".", ".", "8", ".", "."],
                [".", "1", ".", ".", ".", ".", ".", "5", "."],
                ["9", ".", ".", ".", ".", "7", ".", ".", "3"],
            ]
            self.extend(data)
        else:
            self.extend([["0"] * 9 for _ in range(9)])


class MyMatrix(Matrix):
    def set_number(self, i, j, v, run_time=1):
        self.mob_matrix[i][j]
        digobj = TexMobject(v)
        digobj.move_to(self.mob_matrix[i][j])
        trans = Transform(self.mob_matrix[i][j], digobj)
        # self.play(trans, run_time=run_time)
        return trans


class SudokuScene(Scene, LogoMixin):
    def create_grid(self, m):
        squares, rows, cols = [], [], []
        m_cols = m.get_columns()
        for i in range(9):
            row = SurroundingRectangle(VGroup(*m.mob_matrix[i]), color=WHITE)
            col = SurroundingRectangle(m_cols[i], color=WHITE)
            rows.append(row)
            cols.append(col)
        for r, c in product(range(3), repeat=2):
            square = Square()
            square.move_to((LEFT, ORIGIN, RIGHT)[c] * 2 + (UP, ORIGIN, DOWN)[r] * 2)
            squares.append(square)
        grid_obj = VGroup(*squares)
        grid_obj.scale(1.2)
        return squares, rows, cols, grid_obj

    def animate_rows(self, rows, hide=True):
        self.play(LaggedStart(*[FadeIn(rows[i]) for i in range(9)]), run_time=2)
        if hide:
            self.play(LaggedStart(*[FadeOut(rows[i]) for i in range(9)]), run_time=2)

    def animate_columns(self, cols, hide=True):
        self.animate_rows(cols, hide)

    def animate_squares(self, squares, hide=True):
        self.animate_rows(squares, hide)

    def play_grid_creation(self, squares, rows, cols):
        self.animate_rows(rows)
        self.animate_columns(cols)
        self.animate_squares(squares)

    def construct(self):
        self.config = {
            "add_background_rectangles_to_entries": False,
            "include_background_rectangle": False,
            "bracket_h_buff": SMALL_BUFF,
            "bracket_v_buff": SMALL_BUFF,
            "element_alignment_corner": ORIGIN,
            "v_buff": 0.8,
            "h_buff": 0.8,
        }

        LogoMixin.construct(self)


class SudokuCreationScene(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku()
        m = Matrix(A, **self.config)
        m.brackets.scale(0)
        self.play(Write(m))
        squares, rows, cols, grid_obj = self.create_grid(m)
        self.play_grid_creation(squares, rows, cols)
        self.play(FadeIn(grid_obj))
        self.wait(3)


class SudokuColumns(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku()
        m = MyMatrix(A, **self.config)
        m.brackets.scale(0)
        self.add(m)
        squares, rows, cols, grid_obj = self.create_grid(m)
        self.animate_columns(cols, hide=False)
        self.wait()
        self.play(
            *(
                [FadeOut(c) for c in cols[1:]]
                + [
                    FadeOut(VGroup(*m.mob_matrix[:, i]))
                    for i in range(1, m.mob_matrix.shape[1])
                ]
            )
        )
        self.play(*[m.set_number(i, 0, ".") for i in range(9)])

        text = TexMobject("Candidate: ")
        self.play(Write(text))
        v_array = [*range(1, 10)]
        p_array = [*range(9)]
        vals = ["."] * 9
        shuffle(v_array)
        shuffle(p_array)
        for i in range(3):
            vals[p_array[i]] = str(v_array[i])
        self.play(*[m.set_number(p_array[i], 0, v_array[i]) for i in range(3)])
        val = 1
        pos = 0
        while True:
            if pos == 9 or val == 9:
                break
            if vals[pos] != ".":
                pos += 1
                continue
            num = TexMobject(val, color=WHITE)
            num.next_to(text, RIGHT)
            self.play(Write(num))
            if str(val) in vals:
                self.play(
                    ApplyMethod(num.set_color, RED),
                    ApplyMethod(m.mob_matrix[pos][0].set_color, RED),
                )
                self.play(
                    FadeOut(num), ApplyMethod(m.mob_matrix[pos][0].set_color, WHITE)
                )
                val += 1
                continue
            else:
                self.play(
                    ApplyMethod(num.move_to, m.mob_matrix[pos][0]),
                    FadeOut(m.mob_matrix[pos][0]),
                )
                vals[pos] = str(val)
            val += 1
            pos += 1
        self.wait(3)


class SudokuRows(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku()
        m = MyMatrix(A, **self.config)
        m.brackets.scale(0)
        self.add(m)
        squares, rows, cols, grid_obj = self.create_grid(m)
        self.animate_rows(rows, hide=False)
        self.play(
            *(
                [FadeOut(r) for r in rows[1:]]
                + [FadeOut(VGroup(*m.mob_matrix[i])) for i in range(1, 9)]
            )
        )
        self.play(*[m.set_number(0, i, ".") for i in range(9)])
        text = TexMobject("Candidate: ")
        self.play(Write(text))
        v_array = [*range(1, 10)]
        p_array = [*range(9)]
        vals = ["."] * 9
        shuffle(v_array)
        shuffle(p_array)
        for i in range(3):
            vals[p_array[i]] = str(v_array[i])
        self.play(*[m.set_number(0, p_array[i], v_array[i]) for i in range(3)])
        val = 1
        pos = 0
        while True:
            if pos == 9 or val == 10:
                break
            if vals[pos] != ".":
                pos += 1
                continue
            num = TexMobject(val, color=WHITE)
            num.next_to(text, RIGHT)
            self.play(Write(num))
            if str(val) in vals:
                self.play(
                    ApplyMethod(num.set_color, RED),
                    ApplyMethod(m.mob_matrix[0][pos].set_color, RED),
                )
                self.play(
                    FadeOut(num), ApplyMethod(m.mob_matrix[0][pos].set_color, WHITE)
                )
                val += 1
                continue
            else:
                self.play(
                    ApplyMethod(num.move_to, m.mob_matrix[0][pos]),
                    FadeOut(m.mob_matrix[0][pos]),
                )
                vals[pos] = str(val)
            val += 1
            pos += 1
        self.wait(3)


class SudokuSquares(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku()
        m = MyMatrix(A, **self.config)
        m.brackets.scale(0)
        self.add(m)
        squares, rows, cols, grid_obj = self.create_grid(m)
        self.animate_squares(squares, hide=False)
        self.wait()
        self.play(
            *(
                [FadeOut(squares[i]) for i in range(1, 9)]
                + [
                    FadeOut(VGroup(*m.mob_matrix[:, i]))
                    for i in range(3, m.mob_matrix.shape[1])
                ]
                + [FadeOut(VGroup(*m.mob_matrix[i][:3])) for i in range(3, 9)]
            )
        )
        self.play(*[m.set_number(i, j, ".") for i in range(3) for j in range(3)])

        text = TexMobject("Candidate: ")
        self.play(Write(text))
        v_array = [*range(1, 10)]
        vert_array = [*range(3)]
        hori_array = [*range(3)]
        vals = defaultdict(lambda: ".")
        val_pos = {}
        shuffle(v_array)
        shuffle(vert_array)
        shuffle(hori_array)
        print(vert_array, hori_array)
        for i in range(3):
            vals[(hori_array[i], vert_array[i])] = str(v_array[i])
            val_pos[str(v_array[i])] = (hori_array[i], vert_array[i])
        self.play(
            *[m.set_number(hori_array[i], vert_array[i], v_array[i]) for i in range(3)]
        )
        val = 1
        pos = 0
        while True:
            if pos == 9 or val == 10:
                break
            if vals[(pos // 3, pos % 3)] != ".":
                pos += 1
                continue
            num = TexMobject(val, color=WHITE)
            num.next_to(text, RIGHT)
            self.play(Write(num))
            if str(val) in vals.values():
                x, y = val_pos[str(val)]
                self.play(
                    ApplyMethod(num.set_color, RED),
                    ApplyMethod(m.mob_matrix[x][y].set_color, RED),
                )
                self.play(
                    FadeOut(num), ApplyMethod(m.mob_matrix[x][y].set_color, WHITE)
                )
                val += 1
                continue
            else:
                self.play(
                    ApplyMethod(num.move_to, m.mob_matrix[pos // 3][pos % 3]),
                    FadeOut(m.mob_matrix[pos // 3][pos % 3]),
                )
                vals[(pos // 3, pos % 3)] = str(val)

            print(vals)
            print(vals.values())

            val += 1
            pos += 1
        self.wait(3)


class SolveSudoku(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku(fill=False)
        m = MyMatrix(A, **self.config)
        m.to_edge(LEFT)
        m.brackets.scale(0)
        squares, rows, cols, grid_obj = self.create_grid(m)

        A = RawSudoku(fill=True)
        m = MyMatrix(A, **self.config)
        m.brackets.scale(0)

        self.play(Write(m), FadeIn(grid_obj))

        self.iterations = 0

        num_obj = TexMobject(0)
        num_obj.move_to(DL)

        square = Square()
        square.scale(0.4)
        square.to_edge(TOP)
        self.play(Write(square))

        max_iterations = 10

        def solveSudoku(board):
            rows, cols, triples = ddict(set), ddict(set), ddict(set)
            for r, c in product(range(9), repeat=2):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r // 3, c // 3)].add(board[r][c])

            def dfs(r, c, from_r, from_c):
                if self.iterations > max_iterations:
                    return True
                if r == 9:
                    return True
                self.play(ApplyMethod(square.move_to, m.mob_matrix[r][c]))
                if A[r][c] != ".":
                    return dfs((r, r + 1)[c == 8], (c + 1, 0)[c == 8], r, c)
                t = (r // 3, c // 3)
                for dig in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    num = TexMobject(dig, color=WHITE)
                    num.move_to(m.mob_matrix[r][c])
                    self.play(Transform(m.mob_matrix[r][c], num))
                    row_collision = dig in rows[r]
                    if row_collision:
                        ind = board[r].index(dig)
                        self.play(m.mob_matrix[r][ind].set_color, RED)
                        self.play(m.mob_matrix[r][ind].set_color, WHITE)
                    col_collision = dig in cols[c]
                    if col_collision:
                        ind = [board[i][c] for i in range(9)].index(dig)
                        self.play(m.mob_matrix[ind][c].set_color, RED)
                        self.play(m.mob_matrix[ind][c].set_color, WHITE)
                    section_collision = dig in triples[t]
                    if not any([row_collision, col_collision, section_collision]):
                        self.play(FadeOut(num))
                        board[r][c] = dig
                        digobj = TexMobject(dig)
                        digobj.move_to(m.mob_matrix[r][c])
                        self.play(FadeOut(m.mob_matrix[r][c]), FadeIn(digobj))
                        m.mob_matrix[r][c] = digobj
                        self.iterations += 1
                        rows[r].add(dig)
                        cols[c].add(dig)
                        triples[t].add(dig)
                        if dfs((r, r + 1)[c == 8], (c + 1, 0)[c == 8], r, c):
                            return True
                        else:
                            if self.iterations > max_iterations:
                                return True
                            self.play(ApplyMethod(square.move_to, m.mob_matrix[r][c]))
                            board[r][c] = "."
                            digobj = TexMobject(".")
                            digobj.move_to(m.mob_matrix[r][c])
                            self.remove(m.mob_matrix[r][c])
                            self.add(digobj)
                            # self.play(FadeOut(m.mob_matrix[r][c]), FadeIn(digobj))
                            m.mob_matrix[r][c] = digobj
                            rows[r].discard(dig)
                            cols[c].discard(dig)
                            triples[t].discard(dig)
                    else:
                        digobj = TexMobject(".")
                        digobj.move_to(m.mob_matrix[r][c])
                        self.play(FadeOut(m.mob_matrix[r][c]), FadeIn(digobj))
                        m.mob_matrix[r][c] = digobj
                return False

            dfs(0, 0, 0, 0)

        solveSudoku(A)

        self.wait(3)


class SudokuLinearScan(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku(fill=False)
        m = MyMatrix(A, **self.config)
        m.to_edge(LEFT)
        m.brackets.scale(0)
        squares, rows, cols, grid_obj = self.create_grid(m)

        A = RawSudoku(fill=True)
        m = MyMatrix(A, **self.config)
        m.brackets.scale(0)

        self.play(Write(m), FadeIn(grid_obj))

        square = Square()
        square.scale(0.4)
        square.to_edge(TOP)
        self.play(Write(square))

        for i in range(9):
            for j in range(9):
                self.play(square.move_to, m.mob_matrix[i][j], run_time=0.2)

        self.wait(3)
