from manimlib.imports import *
from logo import LogoMixin
from linked_list import Node, LinkedListVMobject
from math import sin, cos, pi


class LinkedListCycleBase(Scene, LogoMixin):

    CONFIG = {"show_construction": False}

    def construct(self):
        LogoMixin.construct(self)

        self.l1 = Node(
            1,
            Node(
                2,
                Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10)))))))),
            ),
        )

        node = self.l1

        to_add = []

        for i in range(-3, 7):
            node.scale(0.5)
            node.set_color(BLUE)
            to_add.append(node)
            if i < 0:
                node.move_to(RIGHT * (i + 3) * 2.5 + LEFT * 6.4 + UP * 3)
            else:
                loc = (
                    3 * RIGHT * sin(i / 7 * pi * 2)
                    + 3 * UP * cos(i / 7 * pi * 2)
                    + RIGHT
                    + UP * 0.5
                )
                node.move_to(loc + DOWN)

            node = node.next

        node = self.l1
        tail = None

        while node:
            if node.next:
                arrow = Arrow(node, node.next)
                to_add.append(arrow)
                self.add(arrow)
                arrow.set_opacity(0.5)
                node.arrow = arrow
            tail = node
            node = node.next

        tail.arrow = Arrow(tail, self.l1.next.next.next)
        self.add(tail.arrow)
        tail.next = self.l1.next.next.next
        tail.arrow.set_opacity(0.5)
        to_add.append(tail.arrow)

        if self.CONFIG["show_construction"]:
            self.play(LaggedStart(*[Write(x) for x in to_add], lag_ratio=0.1))
        else:
            self.add(*to_add)

        self.wait(1)


class LinkedListCyclePlain(LinkedListCycleBase):

    CONFIG = {"show_construction": True}

    def construct(self):
        LinkedListCycleBase.construct(self)


class LinkedListCycleFastSlow(LinkedListCycleBase):

    CONFIG = {"show_construction": False}

    def construct(self):
        LinkedListCycleBase.construct(self)

        node = self.l1

        dot1 = Dot()
        dot1.move_to(self.l1)
        dot1.set_fill(RED, opacity=0.8)

        dot2 = Dot()
        dot2.move_to(self.l1)
        dot2.set_fill(RED, opacity=0.8)

        def move(src, dest, dot):
            return (
                ApplyMethod(
                    dot.move_to,
                    dest.val_obj.get_center(),
                    path_arc=120 * DEGREES,
                ),
            )

        fast = node
        for i in range(20):
            if fast == node and i != 0:
                break
            single = move(node, node.next, dot1)
            double = move(node, fast.next.next, dot2)
            self.play(*(single + double))
            fast = fast.next.next
            node = node.next

        self.play(Indicate(node))

        self.wait(3)


class LinkedListCycleStartNode(LinkedListCycleBase):

    CONFIG = {"show_construction": False}

    def construct(self):
        LinkedListCycleBase.construct(self)

        node = self.l1

        dot1 = Dot()
        dot1.move_to(self.l1)
        dot1.set_fill(RED, opacity=0.8)

        dot2 = Dot()
        dot2.move_to(self.l1.next.next.next.next.next.next.next)
        dot2.set_fill(RED, opacity=0.8)

        def move(src, dest, dot):
            return (
                ApplyMethod(
                    dot.move_to,
                    dest.val_obj.get_center(),
                    path_arc=120 * DEGREES,
                ),
            )

        fast = node.next.next.next.next.next.next.next
        for i in range(20):
            if fast == node and i != 0:
                break
            single = move(node, node.next, dot1)
            double = move(node, fast.next, dot2)
            self.play(*(single + double))
            fast = fast.next
            node = node.next

        self.play(Indicate(node))

        self.wait(3)
