from manimlib.imports import *
from logo import LogoMixin

# from .logo import LogoMixin

class NumberGridMixin:
    INIT_COLOR = BLACK
    def construct(self):
        INIT_POS = LEFT*6.5 + UP*3
        SCALE = 0.5

        self.A = []
        g = None
        row = []
        for i in range(100):
            obj = TextMobject(i)
            obj.set_color(self.INIT_COLOR if i > 1 else GREY)
            obj.scale(0.7)
            row.append(obj)
            obj.move_to(INIT_POS + RIGHT*(i%10)*SCALE+DOWN*(i//10)*SCALE)
            self.A.append(obj)
            if (i+1) % 10 == 0:
                self.play(ShowCreation(VGroup(*row)), run_time = 0.01)
                row[:] = []

class PrimesTrialDivision(Scene, LogoMixin):
    INIT_COLOR = BLACK
    def construct(self):
        LogoMixin.construct(self)
        NumberGridMixin.construct(self)

        divisor = TextMobject(2)
        divisor.set_color(BLUE)
        dividend = TextMobject(1)
        dividend.set_color(GREEN)
        line = TextMobject("\%")
        line.scale(0.5)
        divisor.next_to(line, LEFT)
        dividend.next_to(line, RIGHT)
        equation = VGroup(divisor, line, dividend)
        equation.move_to(RIGHT*2)
        equation.scale(2)

        num_ops_text = TextMobject('operations:')
        num_ops_text.scale(0.7)
        num_ops_text.next_to(dividend, RIGHT*2+DOWN*2)
        
        num_ops = TextMobject(0)
        num_ops.scale(0.7)
        num_ops.next_to(num_ops_text, RIGHT)

        self.play(Write(divisor), Write(line), Write(dividend), Write(num_ops_text), Write(num_ops))

        primes = []
        n = 100
        nops = 0
        arrow = None
        for i in range(2, n):
            iobj = TextMobject(i)
            iobj.set_color(GREY)
            iobj.move_to(divisor)
            equation.add(iobj)
            self.add(iobj)
            iobj.scale(2)
            iobj.set_color(BLUE)
            self.remove(divisor)
            divisor = iobj
            for j in range(i-1, 1, -1):
                nops += 1
                op = TexMobject(nops)
                op.scale(0.7)
                op.next_to(num_ops_text, RIGHT)
                self.remove(num_ops)
                self.add(op)
                num_ops = op
                jobj = TexMobject(j)
                jobj.move_to(dividend)
                self.add(jobj)
                jobj.scale(2)
                jobj.set_color(GREEN)
                self.remove(dividend)
                dividend = jobj
                self.wait(0.1)
                if i % j == 0:
                    self.A[i].set_color(GREY)
                    break
            else:
                arrow = Arrow(divisor, self.A[i])
                self.add(arrow)
                self.wait(0.5)
                self.remove(arrow)
                primes.append(i)
                self.A[i].set_color(GREEN)
            self.wait(0.15)

        self.wait(3)


class PrimesSieve(Scene, LogoMixin):
    INIT_COLOR = GREEN
    def construct(self):
        LogoMixin.construct(self)
        NumberGridMixin.construct(self)

        divisor = TextMobject(2)
        divisor.set_color(BLUE)
        dividend = TextMobject(1)
        dividend.set_color(GREEN)
        line = TextMobject("*")
        line.scale(0.5)
        divisor.next_to(line, LEFT)
        dividend.next_to(line, RIGHT)
        equation = VGroup(divisor, line, dividend)
        equation.move_to(RIGHT*2)
        equation.scale(2)

        num_ops_text = TextMobject('operations:')
        num_ops_text.scale(0.7)
        num_ops_text.next_to(dividend, RIGHT*2+DOWN*2)
        
        num_ops = TextMobject(0)
        num_ops.scale(0.7)
        num_ops.next_to(num_ops_text, RIGHT)

        self.play(Write(divisor), Write(line), Write(dividend), Write(num_ops_text), Write(num_ops))

        n = 100
        nops = 0
        arrow = None

        primes = [False, False] + [True] * n
        for i in range(2, n // 2):
            iobj = TextMobject(i)
            iobj.set_color(GREY)
            iobj.move_to(divisor)
            equation.add(iobj)
            self.add(iobj)
            iobj.scale(2)
            iobj.set_color(BLUE)
            self.remove(divisor)
            divisor = iobj
            if primes[i]:
                jj = -1
                for j in range(i*2, n-1, i):
                    jj = j // i + 1
                    if primes[j]:
                        self.A[j].set_color(GREY)
                        self.wait(0.2)
                    else:
                        self.wait(0.1)
                    nops += 1
                    op = TexMobject(nops)
                    op.scale(0.7)
                    op.next_to(num_ops_text, RIGHT)
                    self.remove(num_ops)
                    self.add(op)
                    num_ops = op
                    jobj = TexMobject(jj)
                    jobj.move_to(dividend)
                    self.add(jobj)
                    jobj.scale(2)
                    jobj.set_color(GREEN)
                    self.remove(dividend)
                    dividend = jobj
                    primes[j] = False
                if jj != -1:
                    self.wait(0.5)
            else:
                jobj = TexMobject('1')
                jobj.move_to(dividend)
                self.add(jobj)
                jobj.scale(2)
                jobj.set_color(GREEN)
                self.remove(dividend)
                dividend = jobj

        self.wait(3)
