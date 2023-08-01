from manim import *

class TextWrap(Scene):
    def construct(self):
        myBaseTemplate = TexTemplate(
            documentclass="\documentclass[preview]{standalone}"
        )
        myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")

        text = Tex(
            "\\justifying{Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus in lacus tristique, interdum turpis sit amet, bibendum felis. Suspendisse mattis arcu quis leo tempus condimentum. Sed luctus turpis mauris, a tristique erat viverra non. Aliquam sed odio convallis, imperdiet mi ac, interdum neque. Donec volutpat quis velit in dictum. Quisque nec quam nec tellus placerat finibus ac nec sapien. Pellentesque maximus velit eu varius lacinia. Pellentesque at nibh nec dolor laoreet vestibulum.}",
            tex_template=myBaseTemplate,
        ).scale(0.6)
        self.play(FadeIn(text))
        self.wait()