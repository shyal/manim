from manimlib.imports import *


class Node(VMobject):
    def __init__(self, val=0, next=None, scene=None, arc=0.5, run_time=1, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.run_time = run_time
        self.arc = arc
        self.scene = scene
        self.val = val
        self.__next = next
        self.circle = Circle()
        self.arrow = Arrow()
        self.val_obj = TexMobject(val)
        self.val_obj.scale(2)
        self.add(self.val_obj)
        self.add(self.circle)

    @property
    def next(self):
        return self.__next

    def move_to(self, point_or_mobject, *args, **kwargs):
        super().move_to(point_or_mobject, *args, **kwargs)
        if self.arrow and self.next:
            self.arrow.put_start_and_end_on(point_or_mobject, self.next.get_center())

    @next.setter
    def next(self, next):
        if self.scene:
            if next and self.__next:
                if self.arrow and self.__next.arrow:
                    arrow = Arrow(self, next, path_arc=self.arc * DEGREES)
                    if self.run_time:
                        self.scene.play(
                            Transform(self.arrow, arrow), run_time=self.run_time
                        )
                    else:
                        self.remove(self.arrow)
                        self.add(arrow)
                        self.arrow = arrow
            if next and not self.__next:
                self.arrow = Arrow(self, next, path_arc=self.arc * DEGREES)
                if self.run_time:
                    self.scene.play(Write(self.arrow, run_time=self.run_time))
                else:
                    self.add(self.arrow)
        self.__next = next


class LinkedListVMobject(VMobject):
    CONFIG = {
        "v_buff": 0.8,
        "h_buff": 1.3,
        "bracket_h_buff": MED_SMALL_BUFF,
        "bracket_v_buff": MED_SMALL_BUFF,
        "add_background_rectangles_to_entries": False,
        "include_background_rectangle": False,
        "element_to_mobject": TexMobject,
        "element_to_mobject_config": {},
        "element_alignment_corner": DR,
    }

    def __init__(self, root, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.root = root
        node = root
        i = 0
        while node:
            self.add(node)
            node.move_to(RIGHT * i * 4)
            node = node.next
            i += 1

        node = root

        while node:
            if node.next:
                arrow = Arrow(node, node.next)
                # arrow.set_opacity(0.5)
                self.add(arrow)
                node.arrow = arrow
            node = node.next

        self.center()

    def set_color(self, col, arrow=False):
        node = self.root
        while node:
            node.circle.set_color(col)
            if arrow:
                node.arrow.set_color(col)
            node = node.next


class AddTwoNumbers(Scene):
    def construct(self):

        l1 = self.l1
        l2 = self.l2

        list_obj1 = LinkedListVMobject(l1)
        list_obj1.scale(0.5)
        list_obj1.shift(UP * 2)
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
        head.next_to(l2, DOWN * 2 + LEFT * 1.5)
        self.play(Write(head))
        v = 0
        while l1 or l2 or v:
            hide = []
            if l1:
                anchor = l1.val_obj
                self.play(Indicate(l1.val_obj), run_time=0.5)
                if l1 and l2:
                    plus = TexMobject("+")
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
            equals = TexMobject("=")
            equals.move_to(DOWN)
            equals.move_to((anchor_x, equals.get_y(), 0))
            hide.append(equals)
            self.play(Write(equals))

            v, r = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + v, 10)

            if v:
                num = TexMobject(v * 10 + r)
                num.next_to(equals, DOWN)
                self.play(Write(num))
                vobj = TexMobject(f"+{v}")
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

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        self.wait(2)
        self.play(
            FadeOut(list_obj1), FadeOut(list_obj2), FadeOut(head), FadeOut(head.arrow)
        )

        self.wait(5)


class Demo(AddTwoNumbers):
    def construct(self, *args, **kwargs):
        self.l1 = Node(2, Node(5, Node(3, Node(5))))
        self.l2 = Node(5, Node(6, Node(4, Node(7))))
        AddTwoNumbers.construct(self, *args, **kwargs)
