from manimlib.imports import *
from logo import LogoMixin
from my_manim_lib import *


class Avatar(Mobject):

    def __init__(self, name, emails):
        self.emails = emails
        VMobject.__init__(self)
        self.p1 = ImageMobject('images/blank_avatar.png')
        self.p1.scale(0.7)
        self.add(self.p1)
        self.name_obj = TexMobject(name)
        self.name_obj.next_to(self.p1, DOWN/2)
        self.name_obj.scale(0.5)
        self.name_obj.set_color(BLUE)
        prev = self.name_obj
        self.add(self.name_obj)
        self.e_objs = []
        for i, e in enumerate(emails):
            e_obj = TexMobject(e)
            e_obj.next_to(prev, RIGHT)
            e_obj.scale(0.5)
            self.e_objs.append(e_obj)
            prev = e_obj
            self.add(e_obj)

    def add_arrows(self):
        e_obj0 = self.e_objs[0]
        arrows = [Arrow(e_obj0, self.name_obj)]
        for e_obj1 in self.e_objs:
            arrows.append(Arrow(e_obj0, e_obj1, path_arc=120*DEGREES))
            e2 = Arrow(e_obj1, e_obj0, path_arc=120*DEGREES)
            arrows.append(e2)
        return arrows

    def next_to(self, item, pos):
        VMobject.next_to(self, item, pos)

class MergeAccounts(Scene):

    def construct(self):
        john1 = Avatar("John", ["johnsmith@mail.com", "john00@mail.com", "JS01@mail.com"])
        john2 = Avatar("John", ["johnnybravo@mail.com"])
        john3 = Avatar("John", ["johnsmith@mail.com", "john\_newyork@mail.com"])
        mary = Avatar("Mary", ["mary@mail.com"])
        objs = [john1, john2, john3, mary]
        for i, obj in enumerate(objs):
            obj.shift(LEFT*6+UP*3.2)
        for i, obj in enumerate(objs):
            obj.shift(DOWN*i*2)
        self.play(FadeIn(john1), FadeIn(john2), FadeIn(john3), FadeIn(mary))
        for obj in objs:
            self.play(*[Write(x) for x in obj.add_arrows()])
        self.wait(3)









