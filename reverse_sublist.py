from manimlib.imports import *
from logo import LogoMixin
from linked_list import Node, LinkedListVMobject


class ReverseSublist1(Scene, LogoMixin):
    CONFIG = {
        'creation': False,
        'tail': False,
        'iteration': False,
        'play_tail_creation': True,
        'tail_visible_in_it': True,
        'tmp_visible_in_it': True,
    }
    def construct(self):
        LogoMixin.construct(self)

        # list creation
        node_kwargs = dict(scene=self)
        l1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, **node_kwargs), **node_kwargs), **node_kwargs), **node_kwargs), **node_kwargs), **node_kwargs)

        list_obj1 = LinkedListVMobject(l1)
        list_obj1.scale(0.5)
        list_obj1.set_color(BLUE)

        # play list creation
        if self.CONFIG['creation']:
            self.play(Write(list_obj1))
        else:
            self.add(list_obj1)

        # dummy creation
        dummy = p = Node(-1, scene=self, run_time=0)
        dummy.scale(0.5)
        dummy.next_to(l1, DOWN*2 + LEFT*1.5)

        # play dummy creation
        if self.CONFIG['creation']:
            self.play(Write(dummy))
        else:
            self.add(dummy)

        # play connecting dummy to first node
        dummy.next = l1

        start = 2
        finish = 5

        # play the fading in of the 'P' pointer
        p_obj = TexMobject('P')
        p_obj.next_to(dummy, UP)
        if self.CONFIG['creation']:
            self.play(FadeIn(p_obj))
        else:
            self.add(p_obj)

        # play the pointer P getting in position
        for _ in range(1, start):
            if self.CONFIG['creation']:
                self.play(ApplyMethod(p_obj.next_to, p.next, UP))
            else:
                p_obj.next_to(p.next, UP)
            p = p.next

        if self.CONFIG['creation']:
            self.wait(3)
            return
    
        p.arc = -120

        tail = p.next
        tail.arc = 120

        # play the tail fading into place
        tail_obj = TexMobject('tail')
        tail_obj.next_to(tail, DOWN)

        if self.CONFIG['play_tail_creation']:
            self.play(FadeIn(tail_obj))
        else:
            self.add(tail_obj)

        if self.CONFIG['tail']:
            self.wait(3)
            return

        for _ in range(finish - start):
            tmp = tail.next
            tmp.arc = 120

            if self.CONFIG['tmp_visible_in_it']:
                tmp_obj = TexMobject('tmp')
                tmp_obj.next_to(tmp, UP)
                self.play(FadeIn(tmp_obj))

            tail.next, tmp.next, p.next = (tmp.next, p.next, tmp)

            if self.CONFIG['tmp_visible_in_it']:
                self.play(FadeOut(tmp_obj))

        self.wait(1)
        self.play(FadeOut(dummy), FadeOut(dummy.arrow), FadeOut(p_obj), FadeOut(tail_obj))

        self.wait(5)

class ReverseSublistCreation(ReverseSublist1):
    CONFIG = {
        'creation': True,
        'tail': False,
        'iteration': False,
        'play_tail_creation': True,
        'tail_visible_in_it': False,
        'tmp_visible_in_it': False,
    }
    def construct(self, *args, **kwargs):
        ReverseSublist1.construct(self, *args, **kwargs)

class ReverseSublistTail(ReverseSublist1):
    CONFIG = {
        'creation': False,
        'tail': True,
        'iteration': False,
        'play_tail_creation': True,
        'tail_visible_in_it': False,
        'tmp_visible_in_it': False,
    }
    def construct(self, *args, **kwargs):
        ReverseSublist1.construct(self, *args, **kwargs)


class ReverseSublistTailStatic(ReverseSublist1):
    CONFIG = {
        'creation': False,
        'tail': False,
        'iteration': False,
        'play_tail_creation': True,
        'tail_visible_in_it': True,
        'tmp_visible_in_it': False,
    }
    def construct(self, *args, **kwargs):
        ReverseSublist1.construct(self, *args, **kwargs)

class ReverseSublistTailStaticTmpMoving(ReverseSublist1):
    CONFIG = {
        'creation': False,
        'tail': False,
        'iteration': False,
        'play_tail_creation': False,
        'tail_visible_in_it': True,
        'tmp_visible_in_it': True,
    }
    def construct(self, *args, **kwargs):
        ReverseSublist1.construct(self, *args, **kwargs)



