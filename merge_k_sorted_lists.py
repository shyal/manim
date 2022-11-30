from manimlib.imports import *
from logo import LogoMixin
from linked_list import Node, LinkedListVMobject


class MergeKSortedLists(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)

        l1 = self.l1
        l2 = self.l2
        l3 = self.l3

        list_obj1 = LinkedListVMobject(l1)
        list_obj1.scale(0.5)
        list_obj1.shift(UP*2)
        list_obj1.set_color(RED)

        list_obj2 = LinkedListVMobject(l2)
        list_obj2.scale(0.5)
        # list_obj2.shift(UP)
        list_obj2.set_color(GREEN)

        list_obj3 = LinkedListVMobject(l3)
        list_obj3.shift(DOWN*2)
        list_obj3.scale(0.5)
        list_obj3.set_color(BLUE)

        left_most = min(l1.get_x(), l2.get_x(), l3.get_x())
        for L, l in [(list_obj1, l1), (list_obj2, l2), (list_obj3, l3)]:
            L.shift((left_most - l.get_x(), 0, 0))

        A = [l1, l2, l3]

        dot = Dot(TOP)
        dot.set_fill(RED, opacity=0.8)

        def set_rec(head, orig_col, high_col):
            node = head
            while node:
                node.orig_col = orig_col
                node.high_col = high_col
                node = node.next

        set_rec(l1, RED, Color(rgb=[1,0.9,0.9]))
        set_rec(l2, GREEN, Color(rgb=[0.9,1,0.9]))
        set_rec(l3, BLUE, Color(rgb=[0.9,0.9,1]))

        dummy = node = Node(-1, scene=self)
        dummy.scale(0.5)
        dummy.to_edge(LEFT)
        self.play(Write(list_obj1), Write(list_obj2), Write(list_obj3), Write(node), FadeIn(dot))
        OC = [RED, GREEN, BLUE]
        self.play(*[ApplyMethod(x.set_color, x.high_col) for x in A])
        while A:
            A.sort(key = lambda x: x.val)
            node.next = A[0]
            node = node.next
            if node:
                self.play(ApplyMethod(dot.move_to, node), run_time=0.5)
            anims = []
            if A[0].next:
                A.append(A[0].next)
                anims.append(ApplyMethod(A[0].next.set_color, A[0].next.high_col))
            rem = A.pop(0)
            anims.append(ApplyMethod(rem.set_color, rem.orig_col))
            self.play(*anims)

        self.play(FadeOut(dummy))
        self.wait(5)

class MergeKSortedLists1(MergeKSortedLists):
    def construct(self, *args, **kwargs):
        self.l1 = Node(3, Node(4, Node(9, Node(10, scene=self), scene=self), scene=self), scene=self)
        self.l2 = Node(2, Node(5, Node(8, Node(11, scene=self), scene=self), scene=self), scene=self)
        self.l3 = Node(1, Node(6, Node(7, Node(12, scene=self), scene=self), scene=self), scene=self)
        MergeKSortedLists.construct(self, *args, **kwargs)

