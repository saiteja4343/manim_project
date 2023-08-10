from manim import *
import numpy as np
class Output(Scene):
    def construct(self):
        # Create a list of numbers
        numbers = [Tex(str(i)) for i in range(0, 10)]

        # Create a vertical group (VGroup) from the numbers
        vertical_list = VGroup(*numbers).arrange(DOWN)

        # Change the color of the number 2 to blue
        vertical_list[2].set_color(BLUE)

        # Move the vertical list to the left edge of the screen
        vertical_list.to_edge(LEFT)



        # Create a small circle with a blue background
        circle = Circle(radius=0.8, fill_opacity=1, color=BLUE_E).next_to(vertical_list[2], np.array((15.0, 0.0, 0.0)))

        # Write "0.97" inside the circle
        text_in_circle = Tex("0.97")
        text_in_circle.next_to(circle, direction=ORIGIN, buff=0)

        # Group the circle and text together
        circle_with_text = VGroup(circle, text_in_circle)

        # Create an arrow pointing from the number 2 to the circle with text
        arrow = Arrow(start=vertical_list[2].get_right(),
                      end=circle_with_text.get_left(),
                      buff=0.1)
        prob_text1 = Tex("Probability of 2").next_to(circle_with_text, np.array((0.0, -3.0, 0.0)))
        prob_text2 = Tex("is 0.97").next_to(prob_text1, DOWN)
        # Add the vertical list to the scene
        self.play(FadeIn(vertical_list))
        self.play(FadeIn(arrow))
        self.play(FadeIn(circle_with_text))
        self.play(FadeIn(prob_text1, prob_text2))
        self.wait()


