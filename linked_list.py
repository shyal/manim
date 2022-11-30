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

    # def shift(self, *vectors):
    #     super().shift(*vectors)
    #     if self.arrow and self.next:
    #         self.arrow.put_start_and_end_on(point_or_mobject, self.next.get_center())

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
