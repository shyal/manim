from logo import LogoMixin
from manimlib.imports import *

class LevenshteinDistanceBase(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)

        sat = TextMobject(*['s','a','t','u','r','d','a','y'])
        sun = TextMobject(*['s','u','n','d','a','y'])
        self.sat = sat
        self.sun = sun

        w1 = VGroup(*sat)
        w2 = VGroup(*sun)

        w2.move_to(DOWN)

        words = VGroup(w1, w2)
        words.scale(2)
        words.move_to(RIGHT*2)
        braces = Brace(words, LEFT)

        w_text = braces.get_text("Levenshtein Distance:")

        self.play(Write(sat), Write(sun))
        self.play(GrowFromCenter(braces), Write(w_text))

        self.wait()

class LevenshteinDistance(LevenshteinDistanceBase):
    def construct(self):
        LevenshteinDistanceBase.construct(self)
        sat, sun = self.sat, self.sun

        # align
        self.play(*[ApplyMethod(sun[a].align_to, sat[b], LEFT) for a, b in zip(range(3,6), range(5, 8))])
        # make red
        self.play(*([ApplyMethod(sat[x].set_color, RED_B) for x in [5,6,7]] + [ApplyMethod(sun[x].set_color, RED_B) for x in [3,4,5]]))
        # fade out
        self.play(*([FadeOut(sun[x]) for x in range(3, 6)] + [FadeOut(sat[x]) for x in range(5, 8)]))

        self.wait()

        # align
        self.play(*[ApplyMethod(sun[a].align_to, sat[b], LEFT) for a, b in zip([0,1,2], [0,3,4])])
        # make red
        self.play(*([ApplyMethod(sat[x].set_color, RED_B) for x in [0,3]] + [ApplyMethod(sun[x].set_color, RED_B) for x in [0,1]]))
        # fade out
        self.play(*([FadeOut(sun[x]) for x in [0,1]] + [FadeOut(sat[x]) for x in [0,3]]))

        brace_top = Brace(VGroup(sat[1], sat[2], sat[4]), TOP)
        res_text = brace_top.get_text("3")
        self.play(GrowFromCenter(brace_top))
        self.play(Write(res_text))
        self.play(ApplyMethod(res_text.set_color, GREEN_B))

        self.wait(5)

class LevenshteinDistanceEdits(LevenshteinDistanceBase):
    def construct(self):
        LevenshteinDistanceBase.construct(self)
        sat, sun = self.sat, self.sun
        # align
        self.play(*[ApplyMethod(sun[a].align_to, sat[b], LEFT) for a, b in zip([0,1,2,3,4,5],[0,3,4,5,6,7])])
        # make red
        self.play(*[ApplyMethod(sat[x].set_color, RED_B) for x in [1,2]])
        # fade out
        self.play(*[FadeOut(sat[x]) for x in [1,2]])

        n = TextMobject('n')
        n.scale(2)
        n.move_to(sat[4])

        # make red
        self.play(ApplyMethod(sat[4].set_color, RED_B))
        # transform
        self.play(Transform(sat[4], n))

        self.wait(5)
