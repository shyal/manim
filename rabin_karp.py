from manimlib.imports import *
from logo import LogoMixin


class BaseHash(Scene, LogoMixin):
    def construct(self):

        LogoMixin.construct(self)

        b = TexMobject(*list(self.CONFIG["str"]))
        b.arrange(RIGHT, buff=self.CONFIG["buff"], aligned_edge=BOTTOM)
        b.scale(self.CONFIG["scale"])
        b.to_edge(UP)
        self.play(Write(b))

        nums = []
        prev = 0
        prev_obj = None
        for i, n in enumerate(
            [ord(x) for x in (self.CONFIG["str"][: self.CONFIG["len"]])]
        ):
            val = prev * 26 + n
            a = TexMobject(*[prev, "\\times", 26, "+", n, "=", val])
            a.set_color(BLUE)

            for k, col in [(1, GREEN), (2, PURPLE_A), (3, GREEN), (5, GREEN)]:
                a[k].set_color(col)

            a.scale(0.8)
            a.next_to(b[i], DOWN * 2)
            a.shift(DOWN * (i + 0.5) * 1.15)

            nums.append(a)

            for j, aa in enumerate(a):
                if j == 0 and prev_obj:
                    self.play(Write(Arrow(prev_obj, a[0])), run_time=0.5)
                elif j == 4:
                    self.play(ApplyMethod(b[i].set_color, RED), run_time=0.5)
                    self.play(Write(Arrow(b[i], aa)), run_time=0.5)
                    self.play(ApplyMethod(b[i].set_color, WHITE), run_time=0.5)
                self.play(Write(aa), run_time=0.5)

            prev = val
            prev_obj = a[-1]

        self.wait(3)


class StringHash(BaseHash):

    CONFIG = {"str": "algo", "len": 4, "scale": 2, "buff": LARGE_BUFF}

    def construct(self):
        BaseHash.construct(self)


class SentenceHash(BaseHash):

    CONFIG = {"str": "pyth", "len": 4, "scale": 2, "buff": LARGE_BUFF}

    def construct(self):
        BaseHash.construct(self)


class RabinSlidingSimple(LogoMixin, MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        LogoMixin.construct(self)
        a = TextMobject("pythonic0algorithms")
        for i in range(1, len(a[0])):
            a[0][i].set_x(a[0][i - 1].get_x() + 0.5)
        a.center()
        a[0][8].set_color(BLACK)
        a.shift(UP)
        b = TextMobject("algo")
        for i in range(1, len(b[0])):
            b[0][i].set_x(b[0][i - 1].get_x() + 0.5)

        sentence = VGroup(a, b)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)

        b.align_to(a, LEFT)

        self.play(Write(sentence))

        frame = self.camera_frame
        frame.save_state()
        self.play(
            ApplyMethod(frame.move_to, b), ApplyMethod(frame.scale, 0.5), run_time=2
        )

        self.play(ApplyMethod(b.align_to, a[0][9], LEFT), run_time=2)
        self.play(
            ApplyMethod(b.set_color, RED),
            ApplyMethod(a[0][9:13].set_color, RED),
            run_time=0.5,
        )
        self.play(
            ApplyMethod(b.set_color, WHITE),
            ApplyMethod(a[0][9:13].set_color, WHITE),
            run_time=0.5,
        )
        self.play(ApplyMethod(b.align_to, a, RIGHT), run_time=2)

        self.wait(5)


class RabinHashBasicEquation(ZoomedScene, LogoMixin):
    CONFIG = {"str": "abcd", "len": 4, "scale": 2, "buff": LARGE_BUFF}

    def construct(self):

        LogoMixin.construct(self)

        b = TexMobject(*list(self.CONFIG["str"]))
        b.arrange(RIGHT, buff=self.CONFIG["buff"], aligned_edge=BOTTOM)
        b.scale(self.CONFIG["scale"])
        b.to_edge(UP)
        b.shift(LEFT * 2)
        self.play(Write(b))

        prev = ["0"]
        prev_obj = None
        for i, n in enumerate([x for x in (self.CONFIG["str"][: self.CONFIG["len"]])]):
            val = [n] if i == 0 else ["("] + prev + ["\\times", 26, "+", n, ")"]
            a = TexMobject(*(prev + ["\\times", 26, "+", n]))
            a.set_color(BLUE)
            a.set_color_by_tex_to_color_map(
                {"26": PURPLE_A, "+": GREEN, "\\times": GREEN}
            )

            a.scale(0.8)
            a.next_to(b[i], DOWN * 2)
            a.shift(DOWN * (i + 0.5) * 1.15)

            for j, aa in enumerate(a):
                if j == 0 and prev_obj:
                    self.play(Write(Arrow(prev_obj, a[0])), run_time=0.5)
                elif j == len(a) - 1:
                    self.play(ApplyMethod(b[i].set_color, RED), run_time=0.5)
                    self.play(Write(Arrow(b[i], aa)), run_time=0.5)
                    self.play(ApplyMethod(b[i].set_color, WHITE), run_time=0.5)
                self.play(Write(aa), run_time=0.5)

            prev = val
            prev_obj = a

        self.wait()

        frame = self.camera_frame
        frame.save_state()
        self.play(ApplyMethod(frame.move_to, prev_obj))
        self.play(ApplyMethod(frame.scale, 0.5))
        self.wait(10)


class RabinHashReorgEquation(ZoomedScene, LogoMixin):
    def construct(self):

        LogoMixin.construct(self)

        a = TexMobject(
            *"( ( a \\times 26 + b ) \\times 26 + c ) \\times 26 + d".split(" ")
        )
        a.set_color(BLUE)
        a.set_color_by_tex_to_color_map({"26": PURPLE_A, "+": GREEN, r"\times": GREEN})
        a.scale(2)
        a.arrange(RIGHT)

        self.play(Write(a))

        for p in a.get_parts_by_tex("26"):
            b = TexMobject(r"\beta")
            b.scale(2)
            b.set_color(PURPLE_A)
            b.align_to(p, LEFT)
            self.play(Transform(p, b))

        for p in a.get_parts_by_tex(r"\times"):
            self.play(FadeOut(p))
            a.submobjects.remove(p)

        b_square = TexMobject(r"\beta^{2}")
        b_square.scale(2)
        b_square.set_color(PURPLE_A)
        b_square.align_to(a[3], LEFT, alignment_vect=RIGHT)

        b = TexMobject(r"\beta")
        b.scale(2)
        b.set_color(PURPLE_A)

        a.submobjects.insert(6, b.copy())
        self.play(Transform(a[3], b_square), FadeOut(a[8]))
        a.submobjects.pop(8)
        self.play(ApplyMethod(a.arrange, RIGHT))
        self.play(FadeOut(a[1]), FadeOut(a[7]))
        a.submobjects.pop(7)
        a.submobjects.pop(1)
        self.play(ApplyMethod(a.arrange, RIGHT))

        aa = TexMobject(*r"a \beta^{3} + b \beta^{2} + c \beta + d".split(" "))
        aa.set_color(BLUE)
        aa.set_color_by_tex_to_color_map(
            {r"\beta": PURPLE_A, "+": GREEN, r"\times": GREEN}
        )
        aa.scale(2)
        aa.arrange(RIGHT)

        self.play(Transform(a, aa))

        self.wait(5)


class RabinRollingHash(LogoMixin, MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        LogoMixin.construct(self)
        a = TextMobject("pythonic0algorithms")
        for i in range(1, len(a[0])):
            a[0][i].set_x(a[0][i - 1].get_x() + 0.5)
        a.center()
        a.scale(1.4)
        a[0][8].set_color(BLACK)
        a.shift(UP)

        self.play(Write(a))

        i = 0
        stack = []
        pluses = []
        sent = "pythonic0algorithms"
        sents = "pythonic algorithms"
        for obj, letter in zip(a[0], sent):
            aa = TexMobject(*[letter, r"\beta^{" + str(3 - i) + "}" if i <= 3 else 0])
            if i <= 3:
                aa[1].set_color(BLACK)

            col_dict = {
                r"\beta^{0}": PURPLE_A,
                r"\beta^{1}": PURPLE_A,
                r"\beta^{2}": PURPLE_A,
                r"\beta^{3}": PURPLE_A,
                "+": GREEN,
                r"\times": GREEN,
                "0": BLACK,
            }
            aa.set_color_by_tex_to_color_map(col_dict)
            aa.scale(0.8)
            aa.align_to(obj, LEFT)

            anims = []
            out_anims = []

            if i > 0 and i < len(sent):
                plus = TexMobject("+")
                pluses.append(plus)
                plus.scale(0.5)
                plus.set_color(GREEN)
                plus.set_x((aa.get_x() + stack[-1].get_x()) / 2)
                anims.append(Write(plus))
                if len(pluses) > 3:
                    self.play(FadeOut(pluses.pop(0)), FadeOut(stack.pop(0)))

            stack.append(aa)
            anims.append(Write(aa))
            self.play(*anims)

            if i >= 3:
                outside_beta = TexMobject(r"\beta")
                l_brace = TexMobject("(")
                l_brace.next_to(stack[0], LEFT)
                r_brace = TexMobject(")")
                r_brace.next_to(stack[-1], RIGHT)
                outside_beta.next_to(r_brace, RIGHT)
                outside_beta.scale(0.8)
                outside_beta.set_color(PURPLE_A)
                self.play(
                    GrowFromCenter(l_brace),
                    GrowFromCenter(r_brace),
                    GrowFromCenter(outside_beta),
                )
                b_anims = []
                for item, j in zip(stack, range(3, -1, -1)):
                    beta = TexMobject(r"\beta^{" + str(j) + "}")
                    beta.scale(0.8)
                    beta.set_color(PURPLE_A)
                    beta.align_to(item[1], LEFT)
                    b_anims.append(Transform(item[1], beta))
                self.play(
                    *b_anims, FadeOut(outside_beta), FadeOut(l_brace), FadeOut(r_brace)
                )
                # num = sum(ord(sents[j]) * (26 ** (4 - j)) for j in range(i - 4, i))
                # num_obj = TextMobject(str(num))
                # num_obj.next_to(stack[0], DOWN + RIGHT)
                # self.play(Write(num_obj))

            i += 1
            # if i > 3:
            #     self.wait(2)

        self.wait(5)
