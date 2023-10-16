from manim import *


class MaxPool(Scene):
    def construct(self):
        input = MathTable(
            [[1, 3, 1],
             [6, 2, 3],
             [5, 2, 4]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, -0.5, 0.0)))
        input.add_highlighted_cell((1,1), color=BLUE_E)
        input.add_highlighted_cell((1, 2), color=BLUE_E)
        input.add_highlighted_cell((2, 1), color=BLUE_E)
        input.add_highlighted_cell((2, 2), color=BLUE_E)

        maxpool = VGroup()

        box = Rectangle(  # create a box
            height=2, width=3,
        )
        text = Tex("\\text {2 X 2 Max Pooling}").scale(0.5).move_to(box.get_center()).scale(1.25)  # create text
        maxpool.add(box, text).next_to(input, np.array((2.5, 0.0, 0.0)))

        output = MathTable(
            [[6, 3],
             [6, 4]],
            include_outer_lines=True).next_to(maxpool, np.array((0.25, 0.0, 0.0))).scale(0.5)
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

        self.play(FadeOut(input), run_time=0.1)
        input_g = MathTable(
            [[1, 3, 1],
             [6, 2, 3],
             [5, 2, 4]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, -0.5, 0.0)))
        input_g.add_highlighted_cell((1, 1), color=BLUE_E)
        input_g.add_highlighted_cell((1, 2), color=BLUE_E)
        input_g.add_highlighted_cell((2, 1), color=GREEN_E)
        input_g.add_highlighted_cell((2, 2), color=BLUE_E)

        self.play(ReplacementTransform(input, input_g), run_time=1, )
        self.wait()
        self.play(FadeIn(output.add_highlighted_cell((1, 1), color=GREEN_E)), run_time=1)
        self.wait()



        input2 = MathTable(
            [[2, 1, 4],
             [3, 6, 1],
             [7, 4, 8]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, -0.5, 0.0)))
        input2.add_highlighted_cell((1, 1), color=BLUE_E)
        input2.add_highlighted_cell((1, 2), color=BLUE_E)
        input2.add_highlighted_cell((2, 1), color=BLUE_E)
        input2.add_highlighted_cell((2, 2), color=BLUE_E)


        output2 = MathTable(
            [[6, 6],
             [7, 8]],
            include_outer_lines=True).next_to(maxpool, np.array((0.25, 0.0, 0.0))).scale(0.5)

        self.play(ReplacementTransform(input_g, input2), run_time=1, )
        self.wait()

        self.play(ReplacementTransform(output, output2), run_time=1, )
        self.wait()


        self.play(FadeOut(input2), run_time=0.1)
        input2_g =MathTable(
            [[2, 1, 4],
             [3, 6, 1],
             [7, 4, 8]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, -0.5, 0.0)))
        input2_g.add_highlighted_cell((1, 1), color=BLUE_E)
        input2_g.add_highlighted_cell((1, 2), color=BLUE_E)
        input2_g.add_highlighted_cell((2, 1), color=BLUE_E)
        input2_g.add_highlighted_cell((2, 2), color=GREEN_E)

        self.play(ReplacementTransform(input2, input2_g), run_time=1, )
        self.wait()
        self.play(FadeIn(output2.add_highlighted_cell((1, 1), color=GREEN_E)), run_time=1)
        self.wait()

        input3 = MathTable(
            [[1, 2, 5],
             [2, 3, 1],
             [6, 1, 4]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, -0.5, 0.0)))
        input3.add_highlighted_cell((1, 1), color=BLUE_E)
        input3.add_highlighted_cell((1, 2), color=BLUE_E)
        input3.add_highlighted_cell((2, 1), color=BLUE_E)
        input3.add_highlighted_cell((2, 2), color=BLUE_E)

        output3 = MathTable(
            [[3, 5],
             [6, 4]],
            include_outer_lines=True).next_to(maxpool, np.array((0.25, 0.0, 0.0))).scale(0.5)

        self.play(ReplacementTransform(input2_g, input3), run_time=1, )
        self.wait()

        self.play(ReplacementTransform(output2, output3), run_time=1, )
        self.wait()

        self.play(FadeOut(input3), run_time=0.1)
        input3_g = MathTable(
            [[1, 2, 5],
             [2, 3, 1],
             [6, 1, 4]],
            include_outer_lines=True).scale(0.5).move_to(np.array((-3.0, -0.5, 0.0)))
        input3_g.add_highlighted_cell((1, 1), color=BLUE_E)
        input3_g.add_highlighted_cell((1, 2), color=BLUE_E)
        input3_g.add_highlighted_cell((2, 1), color=BLUE_E)
        input3_g.add_highlighted_cell((2, 2), color=GREEN_E)

        self.play(ReplacementTransform(input3, input3_g), run_time=1, )
        self.wait()
        self.play(FadeIn(output3.add_highlighted_cell((1, 1), color=GREEN_E)), run_time=1)
        self.wait()








