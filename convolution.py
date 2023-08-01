from manim import *

class Draw(Scene):
    def construct(self):
        input = MathTable(
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, -0.5, 0.0)))

        mul = Tex("*").next_to(input, np.array((1.5, 0.0, 0.0))).scale(0.5)

        kernel = MathTable(
            [[0, 1],
             [2, 3]],
            include_outer_lines=True).next_to(mul, np.array((0.25, 0.0, 0.0))).scale(0.5)

        equal = Tex("=").next_to(kernel, np.array((1.5, 0.0, 0.0))).scale(0.5)

        output = MathTable(
            [[19, 25],
             [37, 43]],
            include_outer_lines=True).next_to(equal, np.array((0.25, 0.0, 0.0))).scale(0.5)

        man = Tex("Convolution").move_to(np.array((0.0, 2.5, 0.0)))

        rectangle = Rectangle(height=6, width=10).move_to(np.array((0.0, 0.0, 0.0)))
        self.play(FadeIn(rectangle), run_time=1)
        self.wait()

        self.play(FadeIn(man), run_time=1)
        self.wait()
        self.play(man.animate.set_color(BLUE_B))
        self.wait(1)

        self.play(FadeIn(input), run_time=1)
        self.wait()

        self.play(FadeIn(mul), run_time=1)
        self.wait()

        self.play(FadeIn(kernel), run_time=1)
        self.wait()

        self.play(FadeIn(equal), run_time=1)
        self.wait()

        self.play(FadeIn(output), run_time=1)
        self.wait()

        table_names = ["Input", "Kernel", "Output"]

        in_text = Tex(table_names[0]).next_to(input, np.array((0.0, -1.0, 0.0))).scale(0.5)
        self.play(FadeIn(in_text), run_time=1)
        self.wait()

        k_text = Tex(table_names[1]).next_to(kernel, np.array((0.0, -2.0, 0.0))).scale(0.5)
        self.play(FadeIn(k_text), run_time=1)
        self.wait()

        out_text = Tex(table_names[2]).next_to(output, np.array((0.0, -1.75, 0.0))).scale(0.5)
        self.play(FadeIn(out_text), run_time=1)
        self.wait()