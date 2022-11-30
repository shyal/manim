from manimlib.imports import *
from functools import reduce
from logo import LogoMixin

class List:
    def __init__(self, parent, A, init_pos, spacing=RIGHT):
        self.parent = parent
        self.objs = []
        for i, a in enumerate(A):
            obj = TextMobject(a)
            self.objs.append(obj)
            if i == 0:
                obj.move_to(init_pos)
            else:
                obj.next_to(self.objs[i-1], spacing)
            self.parent.add(obj)

    def __getitem__(self, ind):
        return self.objs[ind]

class Reduce(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)
        my_first_text=TextMobject("Python Reduce")
        second_line=TextMobject("Simple addition (sum)")
        second_line.next_to(my_first_text,DOWN)
        self.add(my_first_text, second_line)
        self.wait(2)
        self.remove(my_first_text, second_line)

        res = TextMobject("res")
        acc = TextMobject("acc")
        v = TextMobject("v")
        res.move_to(LEFT*5+UP*3)
        acc.next_to(res, RIGHT*5)
        v.next_to(acc, RIGHT*5)
        self.add(res, acc, v)
        A = [1,2,3,4,5]
        nums = List(self, A, RIGHT+UP*2, RIGHT*3)
        acc_nums = List(self, [1,3,6,10], LEFT*3+UP*2, DOWN*3)
        v_nums = List(self, [2,3,4,5], LEFT*1.5+UP*2, DOWN*3)
        [acc_nums[i].set_color(BLACK) for i in [1,2,3]]
        [v_nums[i].set_color(BLACK) for i in [1,2,3]]
        pluses = List(self, ['+']*4, LEFT*(4.5/2) + UP*2, DOWN*3)
        [pluses[i].set_color(BLACK) for i in [0,1,2,3]]
        self.wait(1)

        pluses[0].set_color(WHITE)
        nums[0].set_color(BLUE)
        nums[1].set_color(BLUE)
        acc_nums[0].set_color(BLUE)
        v_nums[0].set_color(BLUE)

        self.wait(1)

        arrow = Arrow(RIGHT,DOWN*0.6)
        arrow.next_to(pluses[0],DOWN+LEFT*0.2)
        self.add(arrow)

        self.wait(1)

        # show second row
        acc_nums[1].set_color(WHITE)
        self.wait(1)
        nums[0].set_color(WHITE)
        nums[1].set_color(WHITE)
        acc_nums[0].set_color(WHITE)
        v_nums[0].set_color(WHITE)

        self.wait(1)
        pluses[1].set_color(WHITE)
        self.wait(1)
        v_nums[1].set_color(BLUE)
        nums[2].set_color(BLUE)
        self.wait(1)

        arrow = Arrow(RIGHT,DOWN*0.6)
        arrow.next_to(pluses[1],DOWN+LEFT*0.2)
        self.add(arrow)

        self.wait(1)

        # show third row
        acc_nums[2].set_color(WHITE)
        nums[2].set_color(WHITE)
        self.wait(1)
        v_nums[1].set_color(WHITE)
        pluses[2].set_color(WHITE)
        self.wait(1)
        v_nums[2].set_color(BLUE)
        nums[3].set_color(BLUE)

        arrow = Arrow(RIGHT,DOWN*0.6)
        arrow.next_to(pluses[2],DOWN+LEFT*0.2)
        self.add(arrow)

        self.wait(1)

        # show fourth row
        acc_nums[3].set_color(WHITE)
        nums[3].set_color(WHITE)
        self.wait(1)
        v_nums[2].set_color(WHITE)
        pluses[3].set_color(WHITE)
        self.wait(1)
        v_nums[3].set_color(BLUE)
        nums[4].set_color(BLUE)


        arrow = Arrow(RIGHT*2,DOWN*0.6)
        arrow.next_to(pluses[3],DOWN+LEFT*0.2)
        self.add(arrow)

        self.wait(1)

        fifteen = TextMobject('15')
        fifteen.next_to(res,DOWN*20)
        v_nums[3].set_color(WHITE)
        nums[4].set_color(WHITE)
        self.add(fifteen)

        self.wait(4)

