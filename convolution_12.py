from manim import *

class Conv(Scene):
    def construct(self):
        input = MathTable(
            [[1, 2, 0],
             [4, 5, 1],
             [7, 8, 2]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, 0.0, 0.0)))
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
            [[25, 13],
             [43, 17]],
            include_outer_lines=True).next_to(equal, np.array((0.25, 0.0, 0.0))).scale(0.5)
        output.add_highlighted_cell((1, 1), color=BLUE_E)
        man = Tex("Convolution").move_to(np.array((0.0, 2.5, 0.0))).scale(1.5)

        rectangle = Rectangle(height=6, width=10).move_to(np.array((0.0, 0.0, 0.0)))
        self.add(rectangle)

        self.add(man)
        man.set_color(BLUE_B)
        table_names = ["Input", "Kernel", "Result"]

        self.add(input)

        in_text = Tex(table_names[0]).next_to(input, np.array((0.0, -1.0, 0.0))).scale(0.75)
        self.add(in_text)

        self.add(mul)

        self.add(kernel)

        k_text = Tex(table_names[1]).next_to(kernel, np.array((0.0, -2.0, 0.0))).scale(0.75)
        self.add(k_text)

        self.add(equal)

        self.add(output)

        out_text = Tex(table_names[2]).next_to(output, np.array((0.0, -1.75, 0.0))).scale(0.75)
        self.add(out_text)

        cal_text = Tex("(1*0)+(2*1)+(4*2)+(5*3) =").next_to(kernel, np.array((0.0, -6.0, 0.0))).scale(0.75)
        self.add(cal_text)

        res_text = Tex("25").next_to(cal_text, np.array((1.0, 0.0, 0.0))).scale(0.75)
        self.add(res_text)

        res_text.set_color(BLUE_D)

        self.wait(2)

        input_2 = MathTable(
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, 0.0, 0.0)))
        input_2.add_highlighted_cell((1, 1), color=BLUE_E)
        input_2.add_highlighted_cell((1, 2), color=BLUE_E)
        input_2.add_highlighted_cell((2, 1), color=BLUE_E)
        input_2.add_highlighted_cell((2, 2), color=BLUE_E)

        output_2 = MathTable(
            [[19, 25],
             [37, 43]],
            include_outer_lines=True).next_to(equal, np.array((0.25, 0.0, 0.0))).scale(0.5)
        output_2.add_highlighted_cell((1, 1), color=BLUE_E)

        self.play(ReplacementTransform(input, input_2), run_time=1)
        self.wait()

        self.play(ReplacementTransform(output, output_2), run_time=1)
        self.wait()

        cal_text2 = Tex("(0*0)+(1*1)+(3*2)+(4*3) =").next_to(kernel, np.array((0.0, -6.0, 0.0))).scale(0.75)
        self.play(ReplacementTransform(cal_text, cal_text2), run_time=1)
        self.wait()

        res_text2 = Tex("19").next_to(cal_text, np.array((1.0, 0.0, 0.0))).scale(0.75)
        self.play(ReplacementTransform(res_text, res_text2), run_time=0.5)
        self.wait()

        self.play(res_text2.animate.set_color(BLUE_D), run_time=0.3)
        self.wait(1)

        input_3 = MathTable(
            [[1, 2, 0],
             [4, 5, 1],
             [7, 8, 2]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, 0.0, 0.0)))
        input_3.add_highlighted_cell((1, 1), color=BLUE_E)
        input_3.add_highlighted_cell((1, 2), color=BLUE_E)
        input_3.add_highlighted_cell((2, 1), color=BLUE_E)
        input_3.add_highlighted_cell((2, 2), color=BLUE_E)

        output_3 = MathTable(
            [[25, 13],
             [43, 17]],
            include_outer_lines=True).next_to(equal, np.array((0.25, 0.0, 0.0))).scale(0.5)
        output_3.add_highlighted_cell((1, 1), color=BLUE_E)

        self.play(ReplacementTransform(input_2, input_3), run_time=1,)
        self.wait()

        self.play(ReplacementTransform(output_2, output_3), run_time=1)
        self.wait()
        cal_text3 = Tex("(1*0)+(2*1)+(4*2)+(5*3) =").next_to(kernel, np.array((0.0, -6.0, 0.0))).scale(0.75)
        self.play(ReplacementTransform(cal_text2, cal_text3), run_time=1)
        self.wait()

        res_text3 = Tex("25").next_to(cal_text, np.array((1.0, 0.0, 0.0))).scale(0.75)
        self.play(ReplacementTransform(res_text2, res_text3), run_time=0.5)
        self.wait()

        self.play(res_text3.animate.set_color(BLUE_D), run_time=0.3)
        self.wait(1)






