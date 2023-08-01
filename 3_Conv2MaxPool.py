from manim import *
import numpy as np
from PIL import Image
from manim_ml.neural_network import NeuralNetwork, Convolutional2DLayer, MaxPooling2DLayer, ImageLayer

# This changes the resolution of our rendered videos
config.pixel_height = 700
config.pixel_width = 1900
config.frame_height = 7.0
config.frame_width = 7.0

# Here we define our basic scene
class Conv2Max(ThreeDScene):

    # The code for generating our scene goes here
    def construct(self):
        image = Image.open("digitX2.jpg")  # You will need to download an image of a digit.
        numpy_image = np.asarray(image)
        # Make neural network
        nn = NeuralNetwork([
            ImageLayer(numpy_image, height=1.5),
            Convolutional2DLayer(1, 8,filter_spacing=0.32),
            Convolutional2DLayer(3, 6, 3 , filter_spacing=0.40),
            MaxPooling2DLayer(kernel_size=2, filter_spacing=0.32),
            Convolutional2DLayer(5, 2, 2 , filter_spacing=0.18),
        ],
            layer_spacing=0.5,
        )
        title = Text("Max Pooling in CNN")
        title.next_to(np.array((0.0, 0.5, 0.0)), DOWN)
        title.scale(0.7)
        self.play(FadeIn(title), run_time=2)
        self.wait(1)
        self.play(title.animate.set_color(YELLOW_B))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)
        # Center the nn
        nn.move_to(np.array((0.0, 0.0, 0.0)))
        self.add(nn)

        # Create text labels and brackets for each layer
        layer_names = ["Convolutional Layers", "Max Pooling"]

        conv_text = Tex(layer_names[0]).next_to(np.array((0.0, 1.5, 0.0)), DOWN)
        conv_text.scale(0.3)  # Decrease the font size by scaling
        self.play(FadeIn(conv_text), run_time=2)
        self.wait()
        self.play(conv_text.animate.set_color(BLUE_B))
        self.wait(1)

        pool_text = Tex(layer_names[1]).next_to(np.array((0.5, -0.75, 0.0)), DOWN)
        pool_text.scale(0.3)  # Decrease the font size by scaling
        self.play(FadeIn(pool_text), run_time=2)
        self.wait()
        self.play(pool_text.animate.set_color(ORANGE))
        self.wait(1)

        # Play animation
        forward_pass = nn.make_forward_pass_animation()

        self.play(forward_pass, run_time=30)
        self.wait(3)