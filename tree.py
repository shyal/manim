from manimlib.imports import *

class Node:
    def __init__(self, val = -1, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val
        self.obj = None

class TreeMobject(VMobject):
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
        nodes, edges = self.tree_to_mob_tree(root)
        self.nodes = VGroup(*nodes)
        self.edges = VGroup(*edges)
        self.add(self.nodes)
        self.add(self.edges)
        self.center()

    def tree_to_mob_tree(self, root):
        def dfs(root, depth = 0, pos = ORIGIN, parent = None):
            if root:
                root_obj = self.element_to_mobject(root.val)
                root_obj.set_color(GREY)
                root.obj = root_obj
                root_obj.move_to(pos)
                if parent:
                    edge = Line(parent, root_obj)
                    edge.set_length(edge.get_length() - 1)
                    edges.append(edge)
                nodes.append(root_obj)
                if root.left:
                    dfs(root.left, depth + 1, pos + LEFT * 3 / depth + DOWN * 1.5, root_obj)
                if root.right:
                    dfs(root.right, depth + 1, pos + RIGHT * 3 / depth + DOWN * 1.5, root_obj)
        nodes = []
        edges = []
        dfs(root, 1, ORIGIN, None)
        return nodes, edges
