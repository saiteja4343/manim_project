from manim import *


class MaxPool(Scene):
    def construct(self):
        input = MathTable(
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, -0.5, 0.0)))
        input.add_highlighted_cell((1,1), color=BLUE_E)
        input.add_highlighted_cell((1, 2), color=BLUE_E)
        input.add_highlighted_cell((2, 1), color=BLUE_E)
        input.add_highlighted_cell((2, 2), color=GREEN_E)
        maxpool = VGroup()

        box = Rectangle(  # create a box
            height=2, width=3,
        )
        text = Tex("\\text {2 X 2 Max Pooling}").scale(0.5).move_to(box.get_center()).scale(1.25)  # create text
        maxpool.add(box, text).next_to(input, np.array((2.5, 0.0, 0.0)))

        output = MathTable(
            [[4, 5],
             [7, 8]],
            include_outer_lines=True).next_to(maxpool, np.array((0.25, 0.0, 0.0))).scale(0.5)
        output.add_highlighted_cell((1, 1), color=GREEN_E)
        man = Tex("Max Pooling").move_to(np.array((0.0, 2.5, 0.0))).scale(1.5)

        rectangle = Rectangle(height=6, width=10).move_to(np.array((0.0, 0.0, 0.0)))
        self.play(FadeIn(rectangle), run_time=1)
        self.wait()

        self.play(FadeIn(man), run_time=1)
        self.wait()
        self.play(man.animate.set_color(BLUE_B))
        self.wait(1)

        table_names = ["Input", "Result"]

        self.play(FadeIn(input), run_time=1)
        self.wait()

        in_text = Tex(table_names[0]).next_to(input, np.array((0.0, -1.0, 0.0))).scale(0.75)
        self.play(FadeIn(in_text), run_time=1)
        self.wait()

        self.play(FadeIn(maxpool), run_time=1)
        self.wait()

        self.play(FadeIn(output), run_time=1)
        self.wait()

        out_text = Tex(table_names[1]).next_to(output, np.array((0.0, -1.75, 0.0))).scale(0.75)
        self.play(FadeIn(out_text), run_time=1)
        self.wait()


