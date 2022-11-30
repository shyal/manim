from sudoku import *

from manimlib.animation import transform


class RowValidation(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)
        items = ["[", ".", ".", "3", "8", ".", ".", "4", ".", "3", "]"]
        line = TexMobject(*items)
        line.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF)
        line.scale(2)
        line.break_up_by_substrings()
        self.play(FadeIn(line))
        self.wait()
        A = line.submobjects
        self.play(
            ApplyMethod(
                line.set_color_by_tex_to_color_map,
                {"texs_to_color_map": {".": RED}},
            )
        )
        self.play(
            ApplyMethod(
                line.set_color_by_tex_to_color_map,
                {"texs_to_color_map": {".": BLACK}},
            )
        )
        listg = VGroup(A[0], A[3], A[4], A[7], A[9], A[-1])
        self.play(ApplyMethod(listg.arrange_submobjects, RIGHT, dict(buff=LARGE_BUFF)))
        setg = listg.deepcopy()
        self.play(ApplyMethod(listg.shift, UP), ApplyMethod(setg.shift, DOWN))

        braces = TexMobject("\\{\\}")
        braces.scale(2)
        s_bracket_open = braces.submobjects[0][0]
        s_bracket_close = braces.submobjects[0][1]
        s_bracket_open.move_to(setg[0])
        s_bracket_close.move_to(setg[-1])

        self.play(
            Transform(setg[0], s_bracket_open), Transform(setg[-1], s_bracket_close)
        )
        self.play(
            ApplyMethod(setg[1].set_color, RED),
            ApplyMethod(setg[4].set_color, RED),
            run_time=0.5,
        )
        self.play(
            ApplyMethod(setg[1].set_color, BLACK),
            ApplyMethod(setg[4].set_color, WHITE),
            run_time=0.5,
        )

        setg[1].to_edge(DOWN)

        self.play(
            ApplyMethod(setg[0].shift, RIGHT * 0.65),
            ApplyMethod(setg[1:].shift, LEFT * 0.65),
        )

        len1 = TextMobject("len() = 4")
        len1.scale(2)
        len1[0][:4].next_to(listg, LEFT)
        len1[0][4:].next_to(listg, RIGHT)

        len2 = TextMobject("len() = 3")
        len2.scale(2)
        len2[0][:4].next_to(setg, LEFT)
        len2[0][4:].next_to(setg, RIGHT)
        len2.shift(UP)

        self.play(Write(len1), Write(len2))
        self.play(
            ApplyMethod(len1[0][-1].set_color, RED),
            ApplyMethod(len2[0][-1].set_color, RED),
        )

        not_unique = TextMobject("not unique")
        not_unique.set_color(RED)
        not_unique.scale(2)
        not_unique.to_edge(DOWN)
        self.play(Write(not_unique))

        self.wait(3)


class SudokuValidateColumns(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku(fill=False)
        m = MyMatrix(A, **self.config)
        squares, rows, cols, grid_obj = self.create_grid(m)
        A = RawSudoku(fill=True)
        m = MyMatrix(A, **self.config)
        self.add(m)
        self.animate_columns(cols, hide=True)
        self.wait(3)


class SudokuValidateRows(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku(fill=False)
        m = MyMatrix(A, **self.config)
        squares, rows, cols, grid_obj = self.create_grid(m)
        A = RawSudoku(fill=True)
        m = MyMatrix(A, **self.config)
        self.add(m)
        self.animate_rows(rows, hide=True)
        self.wait(3)


class SudokuValidateSections(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku(fill=False)
        m = MyMatrix(A, **self.config)
        squares, rows, cols, grid_obj = self.create_grid(m)
        A = RawSudoku(fill=True)
        m = MyMatrix(A, **self.config)
        self.add(m)
        self.animate_rows(squares, hide=True)
        self.wait(3)


class SudokuValidateAll(SudokuScene):
    def construct(self):
        SudokuScene.construct(self)
        A = RawSudoku(fill=False)
        m = MyMatrix(A, **self.config)
        squares, rows, cols, grid_obj = self.create_grid(m)
        A = RawSudoku(fill=True)
        m = MyMatrix(A, **self.config)
        self.add(m)
        self.animate_rows(rows, hide=True)
        self.animate_rows(cols, hide=True)
        self.animate_rows(squares, hide=True)
        self.wait(3)
