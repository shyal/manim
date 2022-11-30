from manimlib.imports import *
from logo import LogoMixin

def find_grants_cap(G, b, move_line):
  NG = G[:]
  def comp_total(c):
    for i, g in enumerate(G):
        NG[i] = min(c, g)
    return sum(NG)
  l, r = 0, b
  while l < r:
    m = (l + r) / 2
    total = comp_total(m)
    move_line(m, NG)
    print(m, NG)
    if abs(total - b) < 0.1:
      return m
    else:
      l, r = ((m, r),(l, m))[total > b]

grantsArray = [2, 100, 50, 120, 130]
newBudget = 190

class BudgetCuts(GraphScene, LogoMixin):

    def construct(self):
        LogoMixin.construct(self)
        def move_m_line(p):
            if 'm' in self.anim_type:
                return [ApplyMethod(line.move_to,[p/20-0.25,0,0]), ApplyMethod(m.move_to,[p/20-0.25,-0.6,0])]
            return []
        def move_h_lines(G):
            moves = []
            if 'grants' in self.anim_type:
                for i, g in enumerate(G):
                    h_line_p[i][1] = g/32.5
                    h_line_p[i][0] = lines[i].get_corner(DOWN)[0]
                    moves.append(ApplyMethod(lines[i].move_to,h_line_p[i]))
            return moves

        move_line = lambda m, G: self.play(*(move_m_line(m) + move_h_lines(G)))
        def intro_text():
            pythonical = TextMobject('pythonical.org')
            my_first_text=TextMobject("Award Budget Cuts")
            if self.anim_type == ['m']:
                second_line=TextMobject("mid value updates")
            elif self.anim_type == ['grants']:
                second_line=TextMobject("grants capping")
            elif set(self.anim_type) == set(['m','grants']):
                second_line=TextMobject("grants capping + mid value")
            second_line.next_to(my_first_text,DOWN)
            third_line=TextMobject("via binary search")
            third_line.next_to(my_first_text,DOWN)
            pythonical.move_to(DOWN*3.5 + RIGHT*4.5)
            pythonical.scale(0.5)
            self.add(pythonical, my_first_text, second_line)
            self.wait(2)
            self.play(Transform(second_line,third_line))
            self.wait(2)
            self.remove(my_first_text, second_line, third_line)
            self.wait(1)

        intro_text()
        self.setup_axes(animate=True)

        m = TextMobject('m')
        m.scale(0.75)
        m.move_to([3,-0.6,0])
        line = Line(np.array([3,-0.5,0]),np.array([3,0.5,0]))
        h_line_p = [[i/2, p/100, 0] for i, p in enumerate(grantsArray)]
        lines = [Line(np.array(p),np.array([p[0]+0.4, p[1], 0])) for i, p in enumerate(h_line_p)]
        move_h_lines(grantsArray)
        m_stuff = ([m] + [line] if 'm' in self.anim_type else [])
        self.add(*((lines if 'grants' in self.anim_type else []) + m_stuff))
        find_grants_cap(grantsArray, newBudget, move_line)
        self.wait(2)


class GrantCuts(BudgetCuts):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 1,
        "y_min" : -100,
        "y_max" : 100,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(0,0,1),
        "y_labeled_nums" :range(-100,120,20),
        "y_tick_frequency": 10,
        "x_axis_label": "",
        "x_axis_width": 0
        # "y_axis_height": 0,
        # "y_axis_label": ''
    }
    anim_type = ['grants']


class MidSearch(BudgetCuts):

    CONFIG = {
        "x_min" : -100,
        "x_max" : 100.3,
        "y_min" : 0,
        "y_max" : 1,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-100,120,20),
        "y_labeled_nums" :range(0,0,1),
        "x_tick_frequency": 10,
        "y_tick_frequency": 10,
        'y_axis_height': 0,
        "y_axis_label": '',
        'exclude_zero_label': False
    }

    anim_type = ['m']

class AwardBudgetCuts(BudgetCuts):

    CONFIG = {
        "x_min" : -100,
        "x_max" : 100.3,
        "y_min" : -100,
        "y_max" : 100,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-100,120,20),
        "y_labeled_nums" :range(-100,120,20),
        "x_tick_frequency": 10,
        "y_tick_frequency": 10
    }

    anim_type = ['m', 'grants']

