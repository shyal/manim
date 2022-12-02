from manimlib.imports import *
from functools import reduce
from random import randint, seed
from itertools import accumulate

from logo import LogoMixin

seed(0)

class ArrayIndexElement(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)
        def doit(A):
            flatten = lambda t: [str(item) for sublist in t for item in sublist]
            l = TextMobject(*flatten([['[']]+[((a, ',') if i < len(A) -1 else (tuple([a])) ) for i, a in enumerate(A)]+[[']']]))
            nums = l[1::2]
            idx = TextMobject([str(x) for x in range(len(A))])
            for i, a in zip(idx, nums):
                i.next_to(a, DOWN*0.66)
                i.set_color(GREEN)
                i.scale(0.8)
            self.play(ShowCreation(l), ShowCreation(idx))
            square = Square()
            square.move_to(nums[0])
            square.scale(0.3)
            self.play(ShowCreation(square))

            for i, v in enumerate(nums):
                self.play(ApplyMethod(square.move_to, v), run_time=0.2)
                if A[i] == i:
                    square.set_color(GREEN)
                    self.wait()
                    self.play(FadeOut(l), FadeOut(idx), FadeOut(square))
                    break
            else:
                square.set_color(RED)
                self.wait()
                self.play(FadeOut(square))
                self.play(FadeOut(l), FadeOut(idx))

            self.wait(1)

        doit([-8,0,2,5])
        doit([-1,0,3,6])
        for i in range(8):
            A = [randint(-8, 2)]
            for i in range(randint(8, 10)):
                A.append(A[-1] + randint(1, 2))
            doit(A)
