from logo import LogoMixin
from tree import *
from manimlib.imports import *

from random import randint


root = Node()


dot = Dot(TOP)
dot.set_fill(RED, opacity=0.8)

class PreOrder(Scene, LogoMixin):
    def construct(self):
        def anim_dfs(scene, root, parent):
            if root:
                if parent:
                    mult = 1 if parent.obj.get_center()[0] - root.obj.get_center()[0] > 0 else -1
                    arc = Line(parent.obj, root.obj, path_arc=120*DEGREES*mult, buff=SMALL_BUFF)
                    scene.play(ShowCreationThenDestruction(arc, run_time=1), ApplyMethod(dot.move_to, root.obj, path_arc=120*DEGREES*mult))
                scene.play(ApplyMethod(root.obj.scale, 2), ApplyMethod(mat.mob_matrix[0][self.it].set_color, BLUE), FadeOut(dot), run_time=0.5)
                scene.play(ApplyMethod(root.obj.set_color, WHITE), run_time=0.1)
                self.it += 1
                scene.play(ApplyMethod(root.obj.scale, 0.5), FadeIn(dot), run_time=0.5)
                anim_dfs(scene, root.left, root)
                anim_dfs(scene, root.right, root)
                if parent:
                    mult = 1 if parent.obj.get_center()[0] - root.obj.get_center()[0] < 0 else -1
                    arc = Line(root.obj, parent.obj, path_arc=120*DEGREES*mult, buff=SMALL_BUFF)
                    scene.play(ShowCreationThenDestruction(arc, run_time=1), ApplyMethod(dot.move_to, parent.obj, path_arc=120*DEGREES*mult))
        LogoMixin.construct(self)
        mat = Matrix([list('abcdefghijklmno')])
        mat.set_color(BLACK)
        mat.scale(0.7)
        mat.to_edge(UP)
        tree = Node('a', Node('b', Node('c', Node('d'), Node('e')), Node('f', Node('g'), Node('h'))), Node('i', Node('j', Node('k'), Node('l')), Node('m', Node('n'), Node('o'))))
        tree_obj = TreeMobject(tree)
        self.play(Write(mat), Write(tree_obj))
        self.it = 0
        anim_dfs(self, tree, None)
        self.wait()

class InOrder(Scene, LogoMixin):
    def construct(self):
        def anim_dfs(scene, root, parent):
            if root:
                if parent:
                    mult = 1 if parent.obj.get_center()[0] - root.obj.get_center()[0] > 0 else -1
                    arc = Line(parent.obj, root.obj, path_arc=120*DEGREES*mult, buff=SMALL_BUFF)
                    scene.play(ShowCreationThenDestruction(arc, run_time=1), ApplyMethod(dot.move_to, root.obj, path_arc=120*DEGREES*mult))
                anim_dfs(scene, root.left, root)
                scene.play(ApplyMethod(root.obj.scale, 2), ApplyMethod(mat.mob_matrix[0][self.it].set_color, BLUE), FadeOut(dot), run_time=0.5)
                scene.play(ApplyMethod(root.obj.set_color, WHITE), run_time=0.1)
                self.it += 1
                scene.play(ApplyMethod(root.obj.scale, 0.5), FadeIn(dot), run_time=0.5)
                anim_dfs(scene, root.right, root)
                if parent:
                    mult = 1 if parent.obj.get_center()[0] - root.obj.get_center()[0] < 0 else -1
                    arc = Line(root.obj, parent.obj, path_arc=120*DEGREES*mult, buff=SMALL_BUFF)
                    scene.play(ShowCreationThenDestruction(arc, run_time=1), ApplyMethod(dot.move_to, parent.obj, path_arc=120*DEGREES*mult))
        LogoMixin.construct(self)
        mat = Matrix([list('dcebfghakjlinmo')])
        mat.set_color(BLACK)
        mat.scale(0.7)
        mat.to_edge(UP)
        tree = Node('a', Node('b', Node('c', Node('d'), Node('e')), Node('f', Node('g'), Node('h'))), Node('i', Node('j', Node('k'), Node('l')), Node('m', Node('n'), Node('o'))))
        tree_obj = TreeMobject(tree)
        self.play(Write(mat), Write(tree_obj))
        self.it = 0
        anim_dfs(self, tree, None)
        self.wait()

class PostOrder(Scene, LogoMixin):
    def construct(self):
        def anim_dfs(scene, root, parent):
            if root:
                if parent:
                    mult = 1 if parent.obj.get_center()[0] - root.obj.get_center()[0] > 0 else -1
                    arc = Line(parent.obj, root.obj, path_arc=120*DEGREES*mult, buff=SMALL_BUFF)
                    scene.play(ShowCreationThenDestruction(arc, run_time=1), ApplyMethod(dot.move_to, root.obj, path_arc=120*DEGREES*mult))
                anim_dfs(scene, root.left, root)
                anim_dfs(scene, root.right, root)
                scene.play(ApplyMethod(root.obj.scale, 2), ApplyMethod(mat.mob_matrix[0][self.it].set_color, BLUE), FadeOut(dot), run_time=0.5)
                scene.play(ApplyMethod(root.obj.set_color, WHITE), run_time=0.1)
                self.it += 1
                scene.play(ApplyMethod(root.obj.scale, 0.5), FadeIn(dot), run_time=0.5)
                if parent:
                    mult = 1 if parent.obj.get_center()[0] - root.obj.get_center()[0] < 0 else -1
                    arc = Line(root.obj, parent.obj, path_arc=120*DEGREES*mult, buff=SMALL_BUFF)
                    scene.play(ShowCreationThenDestruction(arc, run_time=1), ApplyMethod(dot.move_to, parent.obj, path_arc=120*DEGREES*mult))
        LogoMixin.construct(self)
        mat = Matrix([list('decghfbkljnomia')])
        mat.set_color(BLACK)
        mat.scale(0.7)
        mat.to_edge(UP)
        tree = Node('a', Node('b', Node('c', Node('d'), Node('e')), Node('f', Node('g'), Node('h'))), Node('i', Node('j', Node('k'), Node('l')), Node('m', Node('n'), Node('o'))))
        tree_obj = TreeMobject(tree)
        self.play(Write(mat), Write(tree_obj))
        self.it = 0
        anim_dfs(self, tree, None)
        self.wait()
