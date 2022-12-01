from manimlib.imports import *
from logo import LogoMixin
from itertools import accumulate

vals = [9,6,7,8,3,6,4,6,8,8]
min_vals = [*accumulate(vals, lambda a, b: min(a, b))]

class OpenPolygon(Polygon):
    def __init__(self, *vertices, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.set_points_as_corners(
            [*vertices]
        )

class Base(GraphScene, LogoMixin):
    CONFIG = {
        "y_axis_label": None,
        "x_axis_label": None,
        "x_min" : 0,
        "x_max" : 10,
        "y_min" : 0,
        "y_max" : 10,
        "graph_origin" : DOWN * 3 + LEFT * 6,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(0, 10),
        "y_labeled_nums" :range(0, 10),
        "y_tick_frequency": 10,
        "y_axis_height": 6,
        "x_axis_width": 13,
        "x_axis_label": ""
    }

class BestTimeToBuyAndSellStockSimplePrice(Base):

    def construct(self):
        LogoMixin.construct(self, location=UP + RIGHT)
        self.setup_axes(animate=True)
        prices = [self.coords_to_point(i, v) + (0,) for i, v in enumerate(vals)]
        vals_poly = OpenPolygon(*prices)
        self.play(ShowCreation(vals_poly), run_time=3)
        self.wait(2)

class BestTimeToBuyAndSellStockMinPrice(Base):

    def construct(self):
        LogoMixin.construct(self, location=UP + RIGHT)
        self.setup_axes(animate=False)
        prices = [self.coords_to_point(i, v) + (0,) for i, v in enumerate(vals)]
        vals_poly = OpenPolygon(*prices)
        self.add(vals_poly)
        min_prices = [self.coords_to_point(i, v) + (0,) for i, v in enumerate(min_vals)]
        min_vals_poly = OpenPolygon(*min_prices)
        min_vals_poly.set_color(YELLOW)
        self.play(ShowCreation(min_vals_poly), run_time=3)
        self.wait(2)


class BestTimeToBuyAndSellStockMinPriceMarkers(Base):

    def construct(self):
        LogoMixin.construct(self, location=UP + RIGHT)
        self.setup_axes(animate=False)
        prices = [self.coords_to_point(i, v) + (0,) for i, v in enumerate(vals)]
        vals_poly = OpenPolygon(*prices)
        self.add(vals_poly)
        min_prices = [self.coords_to_point(i, v) + (0,) for i, v in enumerate(min_vals)]
        min_vals_poly = OpenPolygon(*min_prices)
        min_vals_poly.set_color(YELLOW)
        lines = []
        self.play(ShowCreation(min_vals_poly), run_time=3)
        for i, v in enumerate(zip(vals, min_vals)):
            if v[0] != v[1]:
                p0 = self.coords_to_point(i, v[1])
                p1 = self.coords_to_point(i, v[0])
                line = DashedLine(p0, p1)
                lines.append(lines)
                self.play(ShowCreation(line))
        self.wait(2)


class BestTimeToBuyAndSellStockMinPriceMarkersTrade(Base):

    def construct(self):
        LogoMixin.construct(self, location=UP + RIGHT)
        self.setup_axes(animate=False)
        prices = [self.coords_to_point(i, v) + (0,) for i, v in enumerate(vals)]
        vals_poly = OpenPolygon(*prices)
        self.add(vals_poly)
        min_prices = [self.coords_to_point(i, v) + (0,) for i, v in enumerate(min_vals)]
        min_vals_poly = OpenPolygon(*min_prices)
        min_vals_poly.set_color(YELLOW)
        lines = []
        self.add(min_vals_poly)
        for i, v in enumerate(zip(vals, min_vals)):
            if v[0] != v[1]:
                p0 = self.coords_to_point(i, v[1])
                p1 = self.coords_to_point(i, v[0])
                line = DashedLine(p0, p1)
                lines.append(lines)
                dot0 = Dot(p0)
                dot1 = Dot(p1)
                dot0.set_color(RED)
                dot1.set_color(RED)
                self.play(ShowCreation(dot0))
                self.play(GrowFromPoint(line, line.get_bottom()))
                self.play(ShowCreation(dot1))
                diff = TextMobject(str(v[0] - v[1]))
                diff.next_to(p0, DOWN)
                self.play(Write(diff))
                index = vals.index(v[1])
                first_p0 = self.coords_to_point(index, v[1])
                trade_line = DashedLine(first_p0, p1)
                self.play(Transform(line, trade_line), ApplyMethod(dot0.move_to, first_p0))
                self.play(FadeOut(dot0), FadeOut(dot1), FadeOut(trade_line), FadeOut(line))

        self.wait(2)
