from manim import *

class Conv(Scene):
    def construct(self):
        input = MathTable(
            [[1, 2, 0],
             [4, 5, 1],
             [7, 8, 2]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, -0.5, 0.0)))
        input.add_highlighted_cell((1, 1), color=BLUE_E)
        input.add_highlighted_cell((1, 2), color=BLUE_E)
        input.add_highlighted_cell((2, 1), color=BLUE_E)
        input.add_highlighted_cell((2, 2), color=BLUE_E)
        mul = Tex("*").next_to(input, np.array((1.5, 0.0, 0.0)))

        kernel = MathTable(
            [[0, 1],
             [2, 3]],
            include_outer_lines=True).next_to(mul, np.array((0.25, 0.0, 0.0))).scale(0.5)

        kernel.add_highlighted_cell((1, 1), color=BLUE_E)
        kernel.add_highlighted_cell((1, 2), color=BLUE_E)
        kernel.add_highlighted_cell((2, 1), color=BLUE_E)
        kernel.add_highlighted_cell((2, 2), color=BLUE_E)

        equal = Tex("=").next_to(kernel, np.array((1.5, 0.0, 0.0)))

        output = MathTable(
            [[25, 00],
             [43, 00]],
            include_outer_lines=True).next_to(equal, np.array((0.25, 0.0, 0.0))).scale(0.5)
        output.add_highlighted_cell((1, 1), color=BLUE_E)
        man = Tex("Convolution").move_to(np.array((0.0, 2.5, 0.0))).scale(1.5)

        rectangle = Rectangle(height=6, width=10).move_to(np.array((0.0, 0.0, 0.0)))
        self.play(FadeIn(rectangle), run_time=1)
        self.wait()

        self.play(FadeIn(man), run_time=1)
        self.wait()
        self.play(man.animate.set_color(BLUE_B))
        self.wait(1)
        table_names = ["Input", "Kernel", "Output"]

        self.play(FadeIn(input), run_time=1)
        self.wait()

        in_text = Tex(table_names[0]).next_to(input, np.array((0.0, -1.0, 0.0))).scale(0.75)
        self.play(FadeIn(in_text), run_time=1)
        self.wait()

        self.play(FadeIn(mul), run_time=1)
        self.wait()

        self.play(FadeIn(kernel), run_time=1)
        self.wait()

        k_text = Tex(table_names[1]).next_to(kernel, np.array((0.0, -2.0, 0.0))).scale(0.75)
        self.play(FadeIn(k_text), run_time=1)
        self.wait()

        self.play(FadeIn(equal), run_time=1)
        self.wait()

        self.play(FadeIn(output), run_time=1)
        self.wait()

        out_text = Tex(table_names[2]).next_to(output, np.array((0.0, -1.75, 0.0))).scale(0.75)
        self.play(FadeIn(out_text), run_time=1)
        self.wait()

