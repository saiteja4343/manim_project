from manim import *
import numpy as np
import random


class Output(Scene):

    def generate_numbers(self):
        # Set the third number to 0.97
        numbers = [0] * 10
        numbers[2] = 0.97

        # Distribute the remaining 0.3 among the other 9 numbers
        remaining_sum = 0.03
        for i in range(10):
            if i != 2:
                # Randomly allocate a portion of the remaining sum to this number
                allocation = random.uniform(0, remaining_sum)
                numbers[i] = round(allocation, 2)
                remaining_sum -= allocation

        # Adjust for any rounding errors to ensure the sum is exactly 0.3
        error = sum(numbers) - 1.27  # 0.97 + 0.3
        if error != 0:
            index = 0 if error < 0 else 2  # Adjust the first or third number based on the error
            numbers[index] = round(numbers[index] - error, 2)

        return numbers
    def construct(self):
        # Create a list of numbers
        numbers = [Tex(str(i)) for i in range(0, 10)]

        # Create a vertical group (VGroup) from the numbers
        vertical_list = VGroup(*numbers).arrange(DOWN)



        # Move the vertical list to the left edge of the screen
        vertical_list.to_edge(np.array((-0.05, 0.0, 0.0)))



        # New list of random numbers
        random_numbers = [Tex(str(num)) for num in self.generate_numbers()]
        random_list = VGroup(*random_numbers).arrange(DOWN).next_to(vertical_list, np.array((3.0, 0.0, 0.0)))

        # Add both lists to the scene
        self.play(FadeIn(vertical_list), FadeIn(random_list))
        self.wait(1)

        arrows = []

        # Create arrows pointing from each original number to the corresponding random number
        for orig, rand in zip(numbers, random_numbers):
            arrow = Arrow(orig.get_right(), rand.get_left(), buff=0.2)
            arrows.append(arrow)
            self.play(GrowArrow(arrow))
            self.wait(0.5)

        # Fade out all arrows
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


