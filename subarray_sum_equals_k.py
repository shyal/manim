from manimlib.imports import *
import math

from logo import LogoMixin
flatten = lambda t: [str(item) for sublist in t for item in sublist]

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

class SubaraySum(Scene, LogoMixin):

    def add_numbers(self):
        self.A = [1, 2, 2, 0, 3, 2, 5]
        self.l = TextMobject(*flatten([['[']]+[((a, ',') if i < len(self.A) -1 else (tuple([a])) ) for i, a in enumerate(self.A)]+[[']']]))
        self.l.scale(2)
        self.l.to_edge(UP)
        self.nums = self.l[1::2]
        if self.CONFIG['play_creation']:
            self.play(Write(self.l))
        else:
            self.add(self.l)

    def add_accumulated_numbers(self):
        self.ACC = ['0', '1', '3', '5', '5', '8', '10', '15']
        self.ACC_I = [0, 1, 3, 5, 5, 8, 10, 15]
        lacc = TextMobject(*flatten([['[']]+[((a, ',') if i < len(self.ACC) -1 else (tuple([a])) ) for i, a in enumerate(self.ACC)]+[[']']]))
        lacc.scale(2)
        lacc.next_to(self.l, DOWN)
        self.acc_nums = lacc[1::2]
        if self.CONFIG['play_creation']:
            self.play(Write(lacc[0::2]))
        else:
            self.add(lacc)

    def add_stickman(self):
        self.stickman = StickMan()
        if self.CONFIG['stickman_start_at'] == 'start':
            self.play(Write(self.stickman))
            self.play(ApplyMethod(self.stickman.move_to, self.number_line.number_to_point(0) + UP))
        else:
            self.add(self.stickman)
            self.stickman.move_to(self.number_line.number_to_point(15) + UP)
            self.add(self.stickman)
            for num in self.ACC:
                self.number_line.numbers[int(num)].set_color(BLUE)

    def animate_stickman(self):
        d = 0
        self.play(ApplyMethod(self.number_line.numbers[0].set_color, BLUE))
        for i, v in enumerate(self.A):
            d += v
            p = self.number_line.number_to_point(d)
            anims = [
                ApplyMethod(self.stickman.move_to, p + UP), 
                ApplyMethod(self.nums[i].set_color, BLUE)
            ]
            if d < len(self.number_line.numbers):
                anims.append(ApplyMethod(self.number_line.numbers[d].set_color, BLUE))
            self.play(*anims)


    def add_number_line(self):
        number_line = NumberLine(**self.number_line_config)
        number_line.move_to(2 * DOWN)
        number_line.add_numbers()
        number_line.scale(0.8)
        number_line.to_edge(DOWN)
        if self.CONFIG['play_creation']:
            self.play(Write(number_line))
        else:
            self.add(number_line)
        self.number_line = number_line


class HoppingDownTheRoad(SubaraySum):
    CONFIG = {
        "play_creation": True,
        "stickman_start_at": 'start',
        "number_line_config": {
            "x_min": 0,
            "x_max": 16,
            'include_tip': True,
        }
    }

    def construct(self):
        LogoMixin.construct(self)
        self.add_numbers()
        self.add_accumulated_numbers()
        self.add_number_line()
        self.wait(1)
        self.add_stickman()
        self.animate_stickman()
        self.bounce_around()
        self.wait(3)

    def bounce_around(self):
        self.starting_value = 0
        value = self.starting_value
        point = self.number_line.number_to_point(value)
        dot = Dot(point)
        dot.set_fill(RED, opacity=0.8)
        arrow = Vector(DL)
        arrow.next_to(point, UR, buff=SMALL_BUFF)
        arrow.match_color(dot)
        start_here = TextMobject("Start here")
        start_here.next_to(arrow.get_start(), UP, SMALL_BUFF)
        start_here.match_color(dot)

        self.play(Write(self.acc_nums[0]), FadeIn(start_here), GrowArrow(arrow), GrowFromPoint(dot, arrow.get_start()))
        self.play(FadeOut(start_here), FadeOut(arrow))
        self.wait()
        for i, x in enumerate(self.ACC[1:], 1):
            new_value = int(x)
            new_point = self.number_line.number_to_point(new_value)
            if new_value == value:
                new_value -= 0.2
                value += 0.2
                new_point[0] -= 0.2
                point[0] += 0.2
                path_arc = -120 * DEGREES
            elif new_value - value > 0:
                path_arc = -120 * DEGREES
            else:
                path_arc = 120 * DEGREES
            arc = Line(
                point, new_point,
                path_arc=path_arc,
                buff=SMALL_BUFF
            )
            self.play(
                Write(self.acc_nums[i]),
                ShowCreationThenDestruction(arc, run_time=1.5),
                ApplyMethod(
                    dot.move_to, new_point,
                    path_arc=path_arc
                ),
            )
            self.wait(0.5)

            value = new_value
            point = new_point


class HoppingBackK(SubaraySum):
    CONFIG = {
        "play_creation": False,
        "stickman_start_at": 'end',
        "number_line_config": {
            "x_min": 0,
            "x_max": 16,
            'include_tip': True,
        }
    }

    def construct(self):
        LogoMixin.construct(self)
        self.add_numbers()
        self.add_accumulated_numbers()
        self.add_number_line()
        self.add_stickman()
        self.add_total()
        self.bounce_around()
        self.wait(3)

    def add_total(self):
        self.total = 0
        self.total_title = TextMobject('Total: ')
        self.total_title.shift(DOWN*2)
        self.total_obj = TextMobject(str(0))
        self.total_obj.next_to(self.total_title, RIGHT)
        self.play(Write(self.total_title), Write(self.total_obj))

    def incr_total(self):
        self.total += 1
        total_obj = TextMobject(str(self.total))
        total_obj.next_to(self.total_title, RIGHT)
        anims = [FadeIn(total_obj), FadeOut(self.total_obj)]
        self.total_obj = total_obj
        return anims

    def subs(self, *args):
        return []

    def clear_subs(self, *args):
        return []

    def subs_arrow(self, *args):
        return []

    def bounce_around(self):
        value = 0
        point = self.number_line.number_to_point(value)
        dot = Dot(point)
        dot.set_fill(RED, opacity=0.8)
        self.play(GrowFromPoint(dot, point))
        blue_dot = Dot(point)
        blue_dot.set_fill(BLUE, opacity=0.8)
        self.wait()
        for i, new_value in enumerate(self.ACC_I[1:], 1):
            new_point = self.number_line.number_to_point(new_value)
            if new_value == value:
                new_value -= 0.2
                value += 0.2
                new_point[0] -= 0.2
                point[0] += 0.2
                path_arc = -120 * DEGREES
            elif new_value - value > 0:
                path_arc = -120 * DEGREES
            else:
                path_arc = 120 * DEGREES
            arc = Line(point, new_point, path_arc=path_arc, buff=SMALL_BUFF)
            blue_dot.move_to(new_point)
            self.play(ShowCreationThenDestruction(arc, run_time=1.5), ApplyMethod(dot.move_to, new_point,path_arc=path_arc))
            subs = self.subs(i)
            if subs:
                self.play(*subs)
            n = math.ceil(new_value) - 5
            for j in range(self.ACC_I.count(n)):
                blue_dot.move_to(new_point)
                hop_back_point = self.number_line.number_to_point(n)
                arc = Line(new_point, hop_back_point, path_arc=-path_arc, buff=SMALL_BUFF)
                self.play(ShowCreationThenDestruction(arc, run_time=1.5),ApplyMethod(blue_dot.move_to, hop_back_point,path_arc=-path_arc))
                self.play(FadeOut(blue_dot), *(self.incr_total() + self.subs_arrow(self.ACC_I.index(n))))

            self.wait(0.5)
            if subs:
                self.clear_subs()
            value = new_value
            point = new_point


class HoppingBackKSubs(HoppingBackK):
    CONFIG = {
        "play_creation": False,
        "stickman_start_at": 'end',
        "number_line_config": {
            "x_min": 0,
            "x_max": 16,
            'include_tip': True,
        }
    }

    def construct(self):
        self.arrows = []
        HoppingBackK.construct(self)

    def subs(self, val):
        anims = [ApplyMethod(self.acc_nums[0].set_color, BLUE)]
        acc = self.acc_nums[val]
        anims.append(ApplyMethod(acc.set_color, BLUE))
        minus = TextMobject('-')
        k = TextMobject(str(5))
        eq = TextMobject('=')
        r = self.ACC_I[val] - 5
        self.res = TextMobject(str(r))

        self.group = VGroup(minus, k, eq, self.res)
        self.group.scale(1.5)

        minus.next_to(acc, DOWN)
        k.next_to(minus, DOWN)
        eq.next_to(k, DOWN)
        self.res.next_to(eq, DOWN)
        self.play(Write(self.group), run_time=1)
        self.wait(2)
        return anims

    def clear_subs(self):
        self.play(FadeOut(self.group), run_time=1)
        if self.arrows:
            self.play(*[FadeOut(arrow) for arrow in self.arrows])
        self.arrows = []

    def subs_arrow(self, j):
        arrow = Arrow(self.res, self.acc_nums[j])
        print('sub_arrows', arrow)
        self.arrows.append(arrow)
        return [Write(arrow)]

