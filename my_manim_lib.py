from manimlib.imports import *

class MatrixNoBrackets(Matrix):
    def add_brackets(self):
        pass

def lerp_t(_min, _max, val):
    return ((val - _min) / (_max - _min))

def damp_t(damp, res):
    return damp + res * (1 - damp*2)

def damp_lerp_t(_min, _max, val, damp):
    res = lerp_t(_min = _min, _max = _max, val = val)
    return damp_t(damp, res)

colmap = {k:interpolate_color(GREEN, BLUE, damp_lerp_t(-1, 10, k, 0.2)) for k in range(-1, 10)}

class GradientMatrix(Matrix):

    def __init__(self, matrix, **kwargs):
        Matrix.__init__(self, matrix, **kwargs)
        self.matrix = matrix
        self.init_col(True)

    def init_col(self, init=False):
        _min = min(min(x) for x in self.matrix)
        _max = max(max(x) for x in self.matrix)
        col_objs = []
        for i, row in enumerate(self.mob_matrix):
            for j, obj in enumerate(row):
                res = damp_lerp_t(_min, _max, self.matrix[i][j], 0.2)
                col = interpolate_color(GREEN, BLUE, res)
                for sub in obj.family_members_with_points():
                    col_objs.append(sub.set_color(col, family=False))
                    if init:
                        sub.color = col
        return col_objs
        # colors = [GREEN, BLUE]
        # if len(colors) == 0:
        #     raise Exception("Need at least one color")
        # elif len(colors) == 1:
        #     return self.set_color(*colors)

        # mobs = self.family_members_with_points()
        # new_colors = color_gradient(colors, len(mobs))

        # for mob, color in zip(mobs, new_colors):
        #     mob.set_color(color, family=False)
        # return self


class GradientMatrixNoBrackets(GradientMatrix):
    def add_brackets(self):
        pass


class OpenPolygon(Polygon):
    def __init__(self, *vertices, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.set_points_as_corners(
            [*vertices]
        )


# class Sphere(Mobject2D):
#     def generate_points(self):
#         self.add_points([
#             (
#                 np.sin(phi) * np.cos(theta),
#                 np.sin(phi) * np.sin(theta),
#                 np.cos(phi) / 2
#             )
#             for phi in np.arange(self.epsilon, np.pi, self.epsilon)
#             for theta in np.arange(0, 2 * np.pi, 2 * self.epsilon / np.sin(phi)) 
#         ])
#         self.set_color(RED)

#     def unit_normal(self, coords):
#         return np.array(coords) / get_norm(coords)

#         