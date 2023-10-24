from manim import *

class Conv(Scene):
    def construct(self):
        input = MathTable(
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, 0.0, 0.0)))
        input.add_highlighted_cell((1, 1), color=BLUE_E)
        input.add_highlighted_cell((1, 2), color=BLUE_E)
        input.add_highlighted_cell((2, 1), color=BLUE_E)
        input.add_highlighted_cell((2, 2), color=BLUE_E)
        mul = Tex("*").next_to(input, np.array((1.5, 0.0, 0.0)))

        kernel = MathTable(
            [[4, 2],
             [1, 0]],
            include_outer_lines=True).next_to(mul, np.array((0.25, 0.0, 0.0))).scale(0.5)

        kernel.add_highlighted_cell((1, 1), color=BLUE_E)
        kernel.add_highlighted_cell((1, 2), color=BLUE_E)
        kernel.add_highlighted_cell((2, 1), color=BLUE_E)
        kernel.add_highlighted_cell((2, 2), color=BLUE_E)

        equal = Tex("=").next_to(kernel, np.array((1.5, 0.0, 0.0)))

        output = MathTable(
            [[5, 12],
             [26, 33]],
            include_outer_lines=True).next_to(equal, np.array((0.25, 0.0, 0.0))).scale(0.5)
        output.add_highlighted_cell((1, 1), color=BLUE_E)
        man = Tex("Convolution").move_to(np.array((0.0, 2.5, 0.0))).scale(1.5)

        rectangle = Rectangle(height=6, width=10).move_to(np.array((0.0, 0.0, 0.0)))
        self.play(FadeIn(rectangle), run_time=0.5)
        self.wait()

        self.play(FadeIn(man), run_time=0.5)
        self.wait()
        self.play(man.animate.set_color(BLUE_B))
        self.wait(1)
        table_names = ["Input", "Kernel", "Result"]

        self.play(FadeIn(input), run_time=1)
        self.wait()

        in_text = Tex(table_names[0]).next_to(input, np.array((0.0, -1.0, 0.0))).scale(0.75)
        self.play(FadeIn(in_text), run_time=0.5)
        self.wait()

        self.play(FadeIn(mul), run_time=0.5)
        self.wait()

        self.play(FadeIn(kernel), run_time=0.5)
        self.wait()

        k_text = Tex(table_names[1]).next_to(kernel, np.array((0.0, -2.0, 0.0))).scale(0.75)
        self.play(FadeIn(k_text), run_time=0.5)
        self.wait()

        self.play(FadeIn(equal), run_time=0.5)
        self.wait()

        self.play(FadeIn(output), run_time=0.5)
        self.wait()

        out_text = Tex(table_names[2]).next_to(output, np.array((0.0, -1.75, 0.0))).scale(0.75)
        self.play(FadeIn(out_text), run_time=0.5)
        self.wait()

        cal_text = Tex("(0*4)+(1*2)+(3*1)+(4*0)").next_to(kernel, np.array((0.0, -6.0, 0.0))).scale(0.75)
        self.play(FadeIn(cal_text), run_time=0.5)
        self.wait()

        equal2 = Tex("=").next_to(cal_text, np.array((0.5, 0.0, 0.0))).scale(0.75)
        self.play(FadeIn(equal2), run_time=0.5)
        self.wait()

        res_text = Tex("5").next_to(equal2, np.array((0.5, 0.0, 0.0))).scale(0.75)
        self.play(FadeIn(res_text), run_time=1)
        self.wait()

        self.play(res_text.animate.set_color(BLUE_D))
        self.wait(0.5)

        self.play(FadeOut(cal_text, equal2, res_text), run_time=0.5)
        self.wait()

        self.wait(1)

        input_2 = MathTable(
            [[1, 2, 0],
             [4, 5, 1],
             [7, 8, 2]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, 0.0, 0.0)))
        input_2.add_highlighted_cell((1, 1), color=BLUE_E)
        input_2.add_highlighted_cell((1, 2), color=BLUE_E)
        input_2.add_highlighted_cell((2, 1), color=BLUE_E)
        input_2.add_highlighted_cell((2, 2), color=BLUE_E)

        output_2 = MathTable(
            [[12, 13],
             [33, 30]],
            include_outer_lines=True).next_to(equal, np.array((0.25, 0.0, 0.0))).scale(0.5)
        output_2.add_highlighted_cell((1, 1), color=BLUE_E)

        self.play(ReplacementTransform(input, input_2), run_time=0.5)
        self.wait()

        self.play(ReplacementTransform(output, output_2), run_time=0.5)
        self.wait()



        cal_text2 = Tex("(1*4)+(2*2)+(4*1)+(5*0)").next_to(kernel, np.array((0.0, -6.0, 0.0))).scale(0.75)
        '''
        self.play(ReplacementTransform(cal_text, cal_text2), run_time=1)
        self.wait()
        '''


        res_text2 = Tex("12").next_to(equal2, np.array((1.0, 0.0, 0.0))).scale(0.75)

        self.play(FadeIn(cal_text2), run_time=0.5)
        self.wait()

        self.play(FadeIn(equal2), run_time=0.5)
        self.wait()

        self.play(FadeIn(res_text2), run_time=0.5)
        self.wait()

        self.play(res_text2.animate.set_color(BLUE_D), run_time=0.3)
        self.wait(1)

        self.play(FadeOut(cal_text2, equal2, res_text2), run_time=0.5)
        self.wait()

        input_3 = MathTable(
            [[2, 1, 0],
             [5, 4, 6],
             [8, 7, 3]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, 0.0, 0.0)))
        input_3.add_highlighted_cell((1, 1), color=BLUE_E)
        input_3.add_highlighted_cell((1, 2), color=BLUE_E)
        input_3.add_highlighted_cell((2, 1), color=BLUE_E)
        input_3.add_highlighted_cell((2, 2), color=BLUE_E)

        output_3 = MathTable(
            [[15, 8],
             [36, 35]],
            include_outer_lines=True).next_to(equal, np.array((0.25, 0.0, 0.0))).scale(0.5)
        output_3.add_highlighted_cell((1, 1), color=BLUE_E)

        self.play(ReplacementTransform(input_2, input_3), run_time=0.5)
        self.wait()

        self.play(ReplacementTransform(output_2, output_3), run_time=0.5)
        self.wait()
        cal_text3 = Tex("(2*4)+(1*2)+(5*1)+(4*0)").next_to(kernel, np.array((0.0, -6.0, 0.0))).scale(0.75)
        '''
        self.play(ReplacementTransform(cal_text2, cal_text3), run_time=1)
        self.wait()
        '''

        res_text3 = Tex("15").next_to(equal2, np.array((1.0, 0.0, 0.0))).scale(0.75)

        self.play(FadeIn(cal_text3), run_time=0.5)
        self.wait()

        self.play(FadeIn(equal2), run_time=0.5)
        self.wait()

        self.play(FadeIn(res_text3), run_time=0.5)
        self.wait()

        self.play(res_text3.animate.set_color(BLUE_D), run_time=0.3)
        self.wait(1)

        self.play(FadeOut(cal_text3, equal2, res_text3), run_time=0.5)
        self.wait()


        '''
        input_4 = MathTable(
            [[3, 2, 4],
             [2, 1, 0],
             [5, 3, 6]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, 0.0, 0.0)))
        input_4.add_highlighted_cell((1, 1), color=BLUE_E)
        input_4.add_highlighted_cell((1, 2), color=BLUE_E)
        input_4.add_highlighted_cell((2, 1), color=BLUE_E)
        input_4.add_highlighted_cell((2, 2), color=BLUE_E)

        output_4 = MathTable(
            [[18, 17],
             [15, 7]],
            include_outer_lines=True).next_to(equal, np.array((0.25, 0.0, 0.0))).scale(0.5)
        output_4.add_highlighted_cell((1, 1), color=BLUE_E)

        self.play(ReplacementTransform(input_3, input_4), run_time=1, )
        self.wait()

        self.play(ReplacementTransform(output_3, output_4), run_time=1)
        self.wait()
        cal_text4 = Tex("(3*4)+(2*2)+(2*1)+(1*0)").next_to(kernel, np.array((0.0, -6.0, 0.0))).scale(0.75)
        self.play(ReplacementTransform(cal_text3, cal_text4), run_time=1)
        self.wait()

        res_text4 = Tex("18").next_to(equal2, np.array((1.0, 0.0, 0.0))).scale(0.75)
        self.play(FadeIn(equal2), run_time=0.5)
        self.wait()

        self.play(FadeIn(res_text4), run_time=0.5)
        self.wait()

        self.play(res_text4.animate.set_color(BLUE_D), run_time=0.3)
        self.wait(3)

        '''







