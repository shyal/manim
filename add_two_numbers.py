from manimlib.imports import *
from logo import LogoMixin
from linked_list import Node, LinkedListVMobject


class AddTwoNumbers(Scene, LogoMixin):
    def construct(self):
        LogoMixin.construct(self)

        l1 = self.l1
        l2 = self.l2

        list_obj1 = LinkedListVMobject(l1)
        list_obj1.scale(0.5)
        list_obj1.shift(UP*2)
        list_obj1.set_color(GREEN)

        list_obj2 = LinkedListVMobject(l2)
        list_obj2.scale(0.5)
        list_obj2.set_color(BLUE)

        left_most = min(l1.get_x(), l2.get_x())
        if left_most != l1.get_x():
            list_obj1.shift((left_most - l1.get_x(), 0, 0))
        else:
            list_obj2.shift((left_most - l2.get_x(), 0, 0))

        self.play(Write(list_obj1))
        self.play(Write(list_obj2))

        head = node = Node(-1)
        head.scale(0.5)
        head.next_to(l2, DOWN*2 + LEFT*1.5)
        self.play(Write(head))
        v = 0
        while l1 or l2 or v:
            hide = []
            if l1:
                anchor = l1.val_obj
                self.play(Indicate(l1.val_obj), run_time=0.5)
                if l1 and l2:
                    plus = TexMobject('+')
                    plus.next_to(l1.val_obj, DOWN * 3)
                    self.play(Write(plus))
                    hide.append(plus)
                anchor_x = anchor.get_x()
            if l2:
                anchor = l2.val_obj
                self.play(Indicate(l2.val_obj), run_time=0.5)
                anchor_x = anchor.get_x()
            if not l1 and not l2:
                anchor_x = node.get_x() + 2
            equals = TexMobject('=')
            equals.move_to(DOWN)
            equals.move_to((anchor_x, equals.get_y(), 0))
            hide.append(equals)
            self.play(Write(equals))
            
            v, r = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + v, 10)

            if v:
                num = TexMobject(v * 10 + r)
                num.next_to(equals, DOWN)
                self.play(Write(num))
                vobj = TexMobject(f'+{v}')
                robj = TexMobject(r)
                vobj.move_to(num)
                robj.next_to(vobj, RIGHT)
                self.play(FadeOut(num), FadeIn(vobj), FadeIn(robj))
                if l1.next:
                    move = ApplyMethod(vobj.next_to, l1.next, UP)
                elif l2.next:
                    move = ApplyMethod(vobj.next_to, l2.next, UP)
                else:
                    move = ApplyMethod(vobj.move_to, (anchor_x + 2, num.get_y() + 1, 0))
                self.play(move, FadeOut(robj))
                hide.append(vobj)

            node.next = Node(r)
            node.next.scale(0.5)
            node.next.next_to(equals, DOWN)
            arrow = Arrow(node, node.next)
            node.arrow = arrow
            anims = [Write(node.next), Write(arrow)]
            anims.extend([FadeOut(x) for x in hide])
            if l1:
                anims.append(ApplyMethod(l1.set_stroke, None, None, 0.5, False, True))
            if l2:
                anims.append(ApplyMethod(l2.set_stroke, None, None, 0.5, False, True))
            self.play(*anims)
            self.play(Indicate(node.next))
            node = node.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        self.wait(2)
        self.play(FadeOut(list_obj1), FadeOut(list_obj2), FadeOut(head), FadeOut(head.arrow))

        self.wait(5)

class AddTwoNumbers1(AddTwoNumbers):
    def construct(self, *args, **kwargs):
        self.l1 = Node(2, Node(5, Node(3, Node(5))))
        self.l2 = Node(5, Node(6, Node(4, Node(7))))
        AddTwoNumbers.construct(self, *args, **kwargs)

class AddTwoNumbers2(AddTwoNumbers):
    def construct(self, *args, **kwargs):
        self.l1 = Node(2, Node(5))
        self.l2 = Node(5, Node(6, Node(4, Node(7))))
        AddTwoNumbers.construct(self, *args, **kwargs)

class AddTwoNumbers3(AddTwoNumbers):
    def construct(self, *args, **kwargs):
        self.l1 = Node(9, Node(6, Node(4, Node(7))))
        self.l2 = Node(2, Node(5))
        AddTwoNumbers.construct(self, *args, **kwargs)

