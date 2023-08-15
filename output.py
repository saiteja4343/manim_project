from manim import *
import numpy as np
import random


class Output(Scene):


    def construct(self):
        # Create a list of numbers
        numbers = [Tex(str(i)) for i in range(0, 10)]

        # Create a vertical group (VGroup) from the numbers
        vertical_list = VGroup(*numbers).arrange(DOWN)



        # Move the vertical list to the left edge of the screen
        vertical_list.to_edge(np.array((-0.05, -1.0, 0.0)))

        # Add both lists to the scene
        self.play(FadeIn(vertical_list))


        # New list of random numbers
        prob_num = ["0.01", "0.02", "0.91", "0.03", "0.00", "0.02", "0.00", "0.01", "0.00", "0.00"]
        random_numbers = [Tex(str(num)) for num in prob_num]
        random_list = VGroup(*random_numbers).arrange(DOWN).next_to(vertical_list, np.array((3.0, 0.0, 0.0)))



        arrows = []

        # Create arrows pointing from each original number to the corresponding random number
        for orig, rand in zip(numbers, random_numbers):
            arrow = Arrow(orig.get_right(), rand.get_left(), buff=0.2)
            arrows.append(arrow)
            self.wait(0.5)
        prob = Tex("Probability").next_to(random_list[0], UP).scale(0.75)
        self.play(FadeIn(prob))
        self.play(FadeIn(random_list), FadeIn(VGroup(*arrows)))
        """
        self.play(random_list[2].animate.set_color(BLUE))
        self.play(vertical_list[2].animate.set_color(BLUE))
        self.play(FadeOut(VGroup(*arrows)))
        self.play(FadeOut(random_list))
        self.wait(2)

        # Create a small circle with a blue background
        circle = Circle(radius=0.5, fill_opacity=1, color=BLUE_E).next_to(vertical_list[2], np.array((3.0, 0.0, 0.0)))

        # Write "0.97" inside the circle
        text_in_circle = Tex("0.97").scale(0.75)
        text_in_circle.next_to(circle, direction=ORIGIN, buff=0)

        # Group the circle and text together
        circle_with_text = VGroup(circle, text_in_circle)

        # Create an arrow pointing from the number 2 to the circle with text
        arrow = Arrow(start=vertical_list[2].get_right(),
                      end=circle_with_text.get_left(),
                      buff=0.1)
        prob_text1 = MathTex(r"Prob(2) = 97 \%").next_to(circle_with_text, np.array((0.0, -1.0, 0.0))).scale(0.6)
        #prob_text2 = Tex("is 0.97").next_to(prob_text1, DOWN)
        # Add the vertical list to the scene
        self.play(FadeIn(arrow))
        self.play(FadeIn(circle_with_text))
        self.play(FadeIn(prob_text1))
        self.wait()
        """
        rect = SurroundingRectangle(random_list[2], fill_opacity=1, fill_color=BLUE_E, stroke_color=BLUE)
        text = Tex("0.97").next_to(rect, direction=ORIGIN, buff=0)
        rect_with_text = VGroup(rect, text)
        self.play(FadeIn(rect_with_text))
        self.wait(5)


