from itertools import product
from itertools import starmap 
from manimlib.imports import *
from functools import reduce
from logo import LogoMixin
from my_manim_lib import *

class LongestArithmeticSequenceProblemStatement(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)
        A = [1,2,4,3,4,5,6]
        mat = Matrix([A])
        mat.set_color(BLUE)
        self.play(Write(mat))
        m = mat.mob_matrix
        for i in [0,1,3,4,5,6]:
            self.play(ApplyMethod(m[0][i].set_color, YELLOW), run_time=0.6)
        self.play(ApplyMethod(m[0][2].set_color, BLACK), run_time=0.6)
        self.wait()
        self.play(ApplyMethod(mat.set_color, BLUE))
        for i in [0,3,5]:
            self.play(ApplyMethod(m[0][i].set_color, YELLOW), run_time=0.6)
        self.play(*[ApplyMethod(m[0][i].set_color, BLACK) for i in [1,2,4,6]], run_time=0.6)
        self.wait()
        self.play(ApplyMethod(mat.set_color, BLUE))
        for i in [1,2,6]:
            self.play(ApplyMethod(m[0][i].set_color, YELLOW), run_time=0.6)
        self.play(*[ApplyMethod(m[0][i].set_color, BLACK) for i in [0,3,4,5]], run_time=0.6)
        self.wait()
        self.play(ApplyMethod(mat.set_color, BLUE))
        self.wait()


class LongestArithmeticSequenceIteration(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)
        A = [1,2,4,3,4,5,6]
        mat = Matrix([A])
        mat.set_color(BLUE)
        self.play(Write(mat))
        d = {}
        iobj = TextMobject('i')
        iobj.set_color(YELLOW)
        iobj.to_edge(DOWN)
        jobj = TextMobject('j')
        jobj.set_color(ORANGE)
        jobj.next_to(iobj, RIGHT)
        self.play(Write(iobj), Write(jobj), run_time=0.4)
        for i in range(1, len(A)):
            self.play(ApplyMethod(iobj.next_to, mat.mob_matrix[0][i], DOWN), run_time=0.4)
            if i > 0:
                jobj.next_to(mat.mob_matrix[0][0], DOWN)
                self.play(FadeIn(jobj), run_time=0.4)
            for j in range(i):
                self.play(ApplyMethod(jobj.next_to, mat.mob_matrix[0][j], DOWN), run_time=0.4)
            self.play(FadeOut(jobj), run_time=0.4)
        self.wait(2)

class LongestArithmeticSequenceFirst(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)
        A = [1,2,4,3,4,5,6]
        mat = Matrix([A])
        mat.set_color(BLUE)
        mat.to_edge(UP)
        mat.shift(UP/2)
        self.play(Write(mat))
        d = {}
        iobj = TextMobject('i')
        iobj.set_color(YELLOW)
        iobj.to_edge(DOWN)
        jobj = TextMobject('j')
        jobj.set_color(ORANGE)
        jobj.next_to(iobj, RIGHT)

        v_mat = [-1,0,1,2,3,4,5]

        delta_v_mat = MatrixNoBrackets(v_mat)
        delta_v_mat.to_edge(LEFT)
        delta_v_mat.shift(DOWN/2)
        self.play(Write(delta_v_mat))

        delta_mat = MatrixNoBrackets([[0]*len(A) for _ in range(len(v_mat))])
        delta_mat.shift(DOWN/2)
        delta_mat.set_color(BLACK)
        self.add(delta_mat)
        self.delta_obj = None

        def show_delta():
            delta = A[i] - A[j]
            self.delta_obj = TextMobject(f"{A[i]} - {A[j]} = {delta}")
            self.delta_obj.next_to(iobj, RIGHT)
            self.play(Write(self.delta_obj))
            self.wait()

        def hide_delta():
            self.play(FadeOut(self.delta_obj))

        doti = Dot()
        doti.scale(1)
        doti.set_color(RED)
        dotj = Dot()
        dotj.scale(1)
        dotj.set_color(RED)

        self.play(Write(iobj), Write(jobj))
        for i in range(1, len(A)):
            self.play(ApplyMethod(iobj.next_to, mat.mob_matrix[0][i], DOWN))
            for j in range(i):
                self.play(ApplyMethod(jobj.next_to, mat.mob_matrix[0][j], DOWN))
                delta = A[i] - A[j]
                show_delta()
                m = delta_mat.mob_matrix
                doti.move_to(m[0][i])
                dotj.move_to(m[0][j])
                row = v_mat.index(delta)
                self.play(ApplyMethod(doti.move_to, m[row][i]), ApplyMethod(dotj.move_to, m[row][j]))
                if (j, delta) in d:
                    val = d[(j, delta)] + 1
                    d[(i, delta)] = val
                else:
                    one = TextMobject(1)
                    one.set_opacity(1/6)
                    one.move_to(m[row][j])
                    self.play(Transform(m[row][j], one))
                    val = 2
                    d[(i, delta)] = val
                    d[(j, delta)] = 1
                new_val = TextMobject(val)
                new_val.set_opacity(val/6)
                new_val.move_to(m[row][i])
                self.play(Transform(m[row][i], new_val), FadeOut(doti), FadeOut(dotj))
                hide_delta()
                d[(i, delta)] = d[(j, delta)] + 1 if (j, delta) in d else 2
        self.wait(3)
















