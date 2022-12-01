from manimlib.imports import *
from logo import LogoMixin
from itertools import accumulate
from my_manim_lib import *

route_initial = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8]]

route_initial_2 = [ [0,   0,  15],
                    [5,   5,  0],
                    [10,  10, 15]]

class Base(GraphScene, LogoMixin):
    CONFIG = {
        "y_axis_label": None,
        "x_axis_label": None,
        "x_min" : 0,
        "x_max" : 11,
        "y_min" : 0,
        "y_max" : 15,
        "graph_origin" : DOWN * 3 + LEFT * 6,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(0, 11),
        "y_labeled_nums" :range(0, 15),
        "y_tick_frequency": 10,
        "y_axis_height": 6,
        "x_axis_width": 10,
        "x_axis_label": ""
    }

class Drone2D(Base):
    CONFIG = {
        'starting_fuel': 0,
        'route': route_initial
    }

    def construct(self):
        route = self.CONFIG['route']
        LogoMixin.construct(self, location=UP + RIGHT)
        self.setup_axes(animate=True)
        pos = [self.coords_to_point(v[0], v[2]) + (0,) for v in route]
        vals_poly = OpenPolygon(*pos)
        self.play(ShowCreation(vals_poly), run_time=3)
        circle = Circle()
        circle.stretch(0.2, 1)
        circle.set_color(BLUE)
        circle.move_to(self.coords_to_point(route[0][0], route[0][2]))
        circlev = Circle()
        circlev.stretch(0.2, 1)
        circlev.set_color(BLUE)

        fuel = TextMobject('fuel: ')
        fuel.next_to(circlev, DOWN)
        fuel.shift(DOWN+LEFT)

        circlev.move_to(self.coords_to_point(13, route[0][2]))
        fuel.move_to(self.coords_to_point(13, 0))

        fuel_amount = TextMobject(str(self.CONFIG['starting_fuel']))
        fuel_amount.next_to(fuel, RIGHT)

        self.play(Write(circle), Write(circlev), Write(fuel), Write(fuel_amount))

        fuel_v = self.CONFIG['starting_fuel']
        for i, p in enumerate(pos[1:], 1):
            v_coord = (self.coords_to_point(13, 0)[0], p[1], 0)
            vmov1 = ApplyMethod(circle.move_to, p)
            vmov2 = ApplyMethod(circlev.move_to, v_coord)
            fuel_v -= (route[i][2] - route[i-1][2])
            fuel_amount_new = TextMobject(str(fuel_v))
            fuel_amount_new.set_color(RED if fuel_v < 0 else GREEN)
            fuel_amount_new.next_to(fuel, RIGHT)
            self.play(vmov1, vmov2, Transform(fuel_amount, fuel_amount_new), run_time=2)
            fuel_amount_new = fuel_amount
        self.wait(2)

class Drone2DSuccess(Drone2D):
    CONFIG = {
        'starting_fuel': 5,
        'route': route_initial
    }

class Drone2DHomeostasis(Drone2D):
    CONFIG = {
        'starting_fuel': 0,
        'route': route_initial_2
    }


class Drone3D(ThreeDScene):
    CONFIG = {
    "default_camera_orientation_kwargs": {
        "phi": 70 * DEGREES,
        "theta": 45 * DEGREES
    }
    }
    def construct(self):
        route = [(x/5,y/5,z/5) for x,y,z in route_initial]
        axes = ThreeDAxes()
        axes.set_stroke(width=1)
        self.add(axes)
        self.set_to_default_angled_camera_orientation()
        sphere = Sphere()
        sphere.move_to(route[0])
        sphere.stretch(0.2, 2)
        self.add(sphere)
        self.begin_ambient_camera_rotation(rate=0.5)
        vals_poly = OpenPolygon(*route)
        vals_poly.set_color(GREEN)
        vals_poly.set_opacity(0.3)
        vals_poly.set_fill(opacity=0)
        self.play(ShowCreation(vals_poly), run_time=3)
        for p in route[1:]:
            self.play(sphere.move_to, p, run_time=2)
        self.wait(6)
