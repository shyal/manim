from itertools import product
from itertools import starmap 
from manimlib.imports import *
from functools import reduce
from logo import LogoMixin

class List:
    def __init__(self, parent, A, init_pos, spacing=RIGHT):
        self.parent = parent
        self.objs = []
        for i, a in enumerate(A):
            obj = TextMobject(str(a))
            self.objs.append(obj)
            if i == 0:
                obj.move_to(init_pos)
            else:
                obj.next_to(self.objs[i-1], spacing)
            self.parent.add(obj)
        self.parent.play(*[FadeIn(o) for o in self.objs], run_time = 0.3)

    def remove(self):
        for o in self.objs:
            self.parent.remove(o)

    def __getitem__(self, ind):
        return self.objs[ind]

    def __setitem__(self, ind, obj):
        self.objs[ind] = obj


class NumberOfIslands(Scene, LogoMixin):
    text = True
    anim_1 = True
    anim_1_dfs = True
    anim_2 = True
    anim_3 = True
    def construct(self):
        LogoMixin.construct(self)

        if self.text:
            my_first_text=TextMobject("Number of Islands")
            second_line=TextMobject("DFS")
            second_line.next_to(my_first_text,DOWN)
            self.add(my_first_text, second_line)
            self.wait(2)
            self.remove(my_first_text, second_line)

            first_step = TextMobject("Step 1: Linear Scan")
            self.add(first_step)
            self.wait(2)
            self.remove(first_step)

        INIT_POS = LEFT*3.2+UP*2.5

        def number_of_islands_anim(M, linear_scan=False, sink_islands=False):
            M_nums = []
            for i, A in enumerate(M):
                nums = List(self, A, INIT_POS+DOWN*i, RIGHT*3)
                M_nums.append(nums)

            square = Square()
            square.scale(0.2)
            square.move_to(INIT_POS)
            self.add(square)

            if linear_scan:
                for i in range(len(M)):
                    for j in range(len(M[i])):
                        self.wait(0.1)
                        square.move_to(INIT_POS+DOWN*i + RIGHT*j*0.94)
                self.wait(2)

            if sink_islands:
                total_obj = TextMobject('Islands:')
                self.n = TextMobject('0')
                total_obj.move_to(LEFT*3 + DOWN*3)
                self.n.next_to(total_obj, RIGHT)
                self.add(total_obj, self.n)
                
                def numIslands(grid):

                    def sink(i, j):
                        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                            grid[i][j] = '0'
                            M_nums[i][j].set_color(RED)
                            self.wait(0.3)
                            new = TextMobject('0')
                            new.move_to(M_nums[i][j])
                            self.remove(M_nums[i][j])
                            M_nums[i][j] = new
                            M_nums[i][j].set_color(BLUE)
                            self.add(M_nums[i][j])
                            [*starmap(sink, product([i-1, i, i+1], [j-1, j+1, j]))]
                            return 1
                        return 0
                    total = 0
                    for i in range(len(grid)):
                        for j in range(len(grid[i])):
                            square.move_to(INIT_POS+DOWN*i + RIGHT*j*0.95)
                            self.wait(0.1)
                            islands = sink(i, j)
                            if islands == 1:
                                total += 1
                                self.remove(self.n)
                                self.n = TextMobject(str(total))
                                self.n.next_to(total_obj)
                                self.add(self.n)

                numIslands(M)
                self.wait(2)
                self.remove(total_obj)
                self.remove(self.n)
            
            [a.remove() for a in M_nums]
            self.remove(square)

        if self.anim_1:
            M = [
            ["1","1","1","1","0","0","0","0"],
            ["1","1","0","1","0","0","0","0"],
            ["1","1","0","0","0","0","1","1"],
            ["0","0","0","1","0","0","1","1"],
            ["0","0","0","1","0","1","1","1"],
            ]
            
            number_of_islands_anim(M, linear_scan=True, sink_islands=False)
            if self.anim_1_dfs:
                number_of_islands_anim(M, linear_scan=False, sink_islands=True)

        if self.text:
            first_step = TextMobject("Step 2: Linear Scan + DFS")
            self.add(first_step)
            self.wait(2)
            self.remove(first_step)

        if self.anim_2:
            M = [
            ["0","0","0","0","1","1","0","0"],
            ["0","1","1","0","1","0","1","0"],
            ["1","1","1","0","0","0","1","1"],
            ["0","1","0","0","0","1","1","0"],
            ["0","0","0","1","0","1","0","0"],
            ]
            
            number_of_islands_anim(M, linear_scan=False, sink_islands=True)

        if self.anim_3:
            M = [
            ["1","0","1","1","0","1","0","1"],
            ["0","0","0","1","0","1","0","0"],
            ["1","1","0","0","0","1","0","1"],
            ["1","0","0","1","0","1","0","0"],
            ["0","0","1","0","0","0","1","1"],
            ]
            
            number_of_islands_anim(M, linear_scan=False, sink_islands=True)


class NumberOfIslandsLinearScan(NumberOfIslands):
    text = False
    anim_1 = True
    anim_1_dfs = False
    anim_2 = False
    anim_3 = False
