from math import sin, cos, pi
from itertools import product
from itertools import starmap 
from manimlib.imports import *
from functools import reduce
from logo import LogoMixin

HEAD_INDEX   = 0
BODY_INDEX   = 1
ARMS_INDEX   = 2
LEGS_INDEX   = 3

SVG_IMAGE_DIR = 'images'

class StickMan(SVGMobject):
    CONFIG = {
        "color" : BLUE_E,
        "file_name_prefix": "stick_man",
        "stroke_width" : 2,
        "stroke_color" : WHITE,
        "fill_opacity" : 0.0,
        "height" : 1,
    }
    def __init__(self, mode = "plain", **kwargs):
        digest_config(self, kwargs)
        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" %
                            (self.file_name_prefix, mode))
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "stick_man_plain.svg",
            )
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


    def name_parts(self):
        self.head = self.submobjects[HEAD_INDEX]
        self.body = self.submobjects[BODY_INDEX]
        self.arms = self.submobjects[ARMS_INDEX]
        self.legs = self.submobjects[LEGS_INDEX]
        self.parts_named = True

M = [
[1,1,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0],
[1,1,1,1,0,0,0,0],
[0,1,1,1,0,0,1,0],
[0,1,0,0,1,0,0,1],
[0,1,0,1,0,1,0,0],
[0,1,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1],
]

def knows(a, b):
    return M[a][b]

class Party:

    def construct_circle(self):
        self.locations = []
        self.stickmen = []
        for i in range(8):
            stickman = StickMan()
            self.stickmen.append(stickman)
            if not self.quick:
                self.wait(0.1)
            self.add(stickman)
            loc = 3*LEFT*sin(i/8*pi*2)+3*DOWN*cos(i/8*pi*2)
            number = TextMobject(i)
            number.move_to(loc+DOWN/2)
            number.scale(0.6)
            self.add(number)
            stickman.move_to(loc)
            self.locations.append(loc)


class CelebrityNaive(Scene, Party, LogoMixin):
    keep_graph = False
    quick = False
    draw_arrows = True

    def construct(self):
        LogoMixin.construct(self)
        self.construct_circle()
        if self.draw_arrows:
            for i in range(8):
                arrows_to_remove = []
                for j in range(8):
                    if i != j:
                        arrow = Arrow(RIGHT,DOWN)
                        arrow.put_start_and_end_on(self.locations[i], self.locations[j])
                        arrow.set_color(BLUE if M[i][j] else GREY)
                        self.add(arrow)
                        if not self.quick:
                            self.wait(0.1)
                        if self.keep_graph == False:
                            arrows_to_remove.append(arrow)
                        elif not M[i][j]:
                            arrows_to_remove.append(arrow)
                if not self.quick:
                    self.wait(0.5)
                [self.remove(a) for a in arrows_to_remove]
        self.wait(1)

class CelebrityGraph(CelebrityNaive):
    keep_graph = True

class CelebrityGraphDFS(CelebrityNaive):
    keep_graph = True
    quick = True
    draw_arrows = False

    def construct(self):
        CelebrityNaive.construct(self)

        def func(a, b):
            does_know = M[a][b]
            c = (a, b)[does_know]
            self.stickmen[a].set_color(WHITE)
            self.stickmen[b].set_color(WHITE)
            self.stickmen[c].set_color(BLUE)
            arrow = Arrow(RIGHT,DOWN)
            arrow.put_start_and_end_on(self.locations[a], self.locations[b])
            self.add(arrow)
            self.wait()
            self.remove(arrow)
            return c

        c = reduce(func, range(1, len(M)), 0)
        self.wait(1)


class CelebrityConfirmation(CelebrityNaive):
    keep_graph = True
    quick = True
    draw_arrows = False

    def construct(self):
        CelebrityNaive.construct(self)

        def func(a, b):
            does_know = M[a][b]
            c = (a, b)[does_know]
            arrow = Arrow(RIGHT,DOWN)
            arrow.put_start_and_end_on(self.locations[a], self.locations[b])
            self.add(arrow)
            self.wait(0.25)
            self.remove(arrow)
            self.wait(0.25)
            return c
        c = reduce(lambda a, b: (a, b)[knows(a, b)], range(1, len(M)), 0)
        self.stickmen[c].set_color(BLUE)
        [(func(j, c) and not func(c, j)) for j in range(len(M))]

        self.wait(1)

