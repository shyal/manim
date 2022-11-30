from logo import LogoMixin
from tree import *
from manimlib.imports import *
from random import randint

root = Node()

dot = Dot(TOP)
dot.set_fill(RED, opacity=0.8)

class BinaryTreeRightSideView(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)
        def anim_dfs(scene, root, parent, depth=0):
            if root:
                if parent:
                    mult = 1 if parent.obj.get_center()[0] - root.obj.get_center()[0] > 0 else -1
                    arc = Line(parent.obj, root.obj, path_arc=120*DEGREES*mult, buff=SMALL_BUFF)
                    scene.play(ShowCreationThenDestruction(arc, run_time=1), ApplyMethod(dot.move_to, root.obj, path_arc=120*DEGREES*mult))
                anim_dfs(scene, root.left, root, depth+1)
                mat_entry = mat.mob_matrix[depth][0]
                clone = root.obj.deepcopy()
                clone.set_color(BLUE)
                clone.scale(2)
                clone.move_to(mat_entry)
                scene.play(ApplyMethod(root.obj.scale, 2), FadeOut(dot), run_time=0.5)
                scene.play(ApplyMethod(root.obj.set_color, WHITE), Transform(mat_entry, clone), run_time=0.1) # , ApplyMethod(mat_entry.set_color, BLUE)
                self.it += 1
                scene.play(ApplyMethod(root.obj.scale, 0.5), FadeIn(dot), ApplyMethod(mat_entry.set_color, WHITE), ApplyMethod(mat_entry.scale, 0.5), run_time=0.5)
                anim_dfs(scene, root.right, root, depth+1)
                if parent:
                    mult = 1 if parent.obj.get_center()[0] - root.obj.get_center()[0] < 0 else -1
                    arc = Line(root.obj, parent.obj, path_arc=120*DEGREES*mult, buff=SMALL_BUFF)
                    scene.play(ShowCreationThenDestruction(arc, run_time=1), ApplyMethod(dot.move_to, parent.obj, path_arc=120*DEGREES*mult))
        tree = Node('a', Node('b', Node('c', Node('d'), Node('e')), Node('f', Node('g'), Node('h'))), Node('i', Node('j', Node('k'), Node('l')), Node('m', Node('n'), Node('o'))))
        tree_obj = TreeMobject(tree)
        mat = Matrix(['0', '1', '2', '3'], v_buff=2.1)
        # mat.set_color(BLACK)
        mat.scale(0.7)
        mat.to_edge(RIGHT)
        self.play(Write(tree_obj), Write(mat))
        self.it = 0
        anim_dfs(self, tree, None)
        self.wait()