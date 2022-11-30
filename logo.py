from manimlib.imports import *

class LogoMixin:
    def construct(self, location=DOWN + RIGHT):
        logo = TextMobject('www.shyal.com')
        # logo.move_to(location)
        # logo.move_to(TOP*3.8 + RIGHT*4.5)
        logo.scale(0.7)
        logo.to_edge(location)
        self.add(logo)
