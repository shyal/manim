from logo import LogoMixin
from manimlib.imports import *
from tree import TreeMobject, Node
from random import randint

root = Node()

class BinaryTreeBFS(Scene, LogoMixin):
    def construct(self):
        def anim_bfs(scene, root):
            q = [(root, None)]
            prev = None
            q_obj = TextMobject('q')
            children_obj = TextMobject('children')
            q_obj.to_edge(UP + LEFT)
            children_obj.to_edge(UP + RIGHT)
            self.play(Write(children_obj), Write(q_obj))
            level = 0
            while q:
                children = []
                nodes = [node.obj for node, _ in q]
                q_rect = SurroundingRectangle(VGroup(*nodes), color=BLUE)
                if prev:
                    self.play(FadeIn(q_rect), ApplyMethod(children_obj.next_to, q_rect, (LEFT, DOWN)[level == 3]), ApplyMethod(q_obj.next_to, prev, LEFT))
                else:
                    self.play(FadeIn(q_rect), ApplyMethod(q_obj.next_to, q_rect, LEFT))
                for node, parent in q:
                    if parent:
                        dot = Dot()
                        dot.set_fill(RED, opacity=0.8)
                        dot.move_to(parent.obj)
                    if parent:
                        arc = Line(parent.obj, node.obj, path_arc=120*DEGREES, buff=SMALL_BUFF)
                        scene.play(ShowCreationThenDestruction(arc), ApplyMethod(dot.move_to, node.obj, path_arc=120*DEGREES))
                        self.play(FadeOut(dot), run_time=0.2)
                    scene.play(ApplyMethod(node.obj.set_color, WHITE), run_time=0.1)
                    scene.play(ApplyMethod(node.obj.scale, 2), ApplyMethod(mat.mob_matrix[0][self.it].set_color, BLUE), run_time=0.5)
                    scene.play(ApplyMethod(node.obj.scale, 0.5), run_time=0.5)
                    if node.left:
                        children.append((node.left, node))
                    if node.right:
                        children.append((node.right, node))
                    self.it += 1
                q = children
                if prev:
                    scene.play(FadeOut(prev))
                prev = q_rect
                level += 1

        LogoMixin.construct(self)
        mat = Matrix([list('abicfjmdeghklno')])
        mat.set_color(BLACK)
        mat.scale(0.7)
        mat.to_edge(UP)
        tree = Node('a', Node('b', Node('c', Node('d'), Node('e')), Node('f', Node('g'), Node('h'))), Node('i', Node('j', Node('k'), Node('l')), Node('m', Node('n'), Node('o'))))
        tree_obj = TreeMobject(tree)
        self.play(Write(mat), Write(tree_obj))
        self.it = 0
        anim_bfs(self, tree)
        self.wait()
