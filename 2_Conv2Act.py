from manim import *
import numpy as np
from PIL import Image
from manim_ml.neural_network import NeuralNetwork, Convolutional2DLayer, ImageLayer, FeedForwardLayer, MaxPooling2DLayer

# This changes the resolution of our rendered videos
config.pixel_height = 700
config.pixel_width = 1900
config.frame_height = 7.0
config.frame_width = 7.0

# Here we define our basic scene
class Conv2Act(ThreeDScene):

    # The code for generating our scene goes here
    def construct(self):
        # Make nn
        image = Image.open("digitX2.jpg")  # You will need to download an image of a digit.
        numpy_image = np.asarray(image)
        layers = [
            ImageLayer(numpy_image, height=1.5),
            Convolutional2DLayer(1, 7, filter_spacing=0.32),
            Convolutional2DLayer(3, 5, 3, filter_spacing=0.32, activation_function="ReLU"),
            Convolutional2DLayer(5, 3, 3, filter_spacing=0.18, activation_function="ReLU"),
            FeedForwardLayer(5, activation_function="Sigmoid", node_radius=0.06, node_stroke_width=1.5,
                             rectangle_color=BLACK, node_spacing=0.2),
        ]
        nn = NeuralNetwork(layers,
            layer_spacing=0.5,
        )
        title = Text("Activation Function in CNN")
        title.next_to(np.array((0.0, 0.5, 0.0)), DOWN)
        title.scale(0.7)
        self.play(FadeIn(title), run_time=2)
        self.wait(1)
        self.play(title.animate.set_color(YELLOW_B))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        # Center the neural network
        nn.move_to(np.array((-0.5, 0.0, 0.0)))

        self.add(nn)

        # Create text labels and brackets for each layer
        layer_names = ["Convolutional Layers", "Feed Forward Layers"]

        conv_text = Tex(layer_names[0]).next_to(np.array((0.5, -0.75, 0.0)), DOWN)
        conv_text.scale(0.3)  # Decrease the font size by scaling
        self.play(FadeIn(conv_text), run_time=2)
        self.wait()

        feed_text = Tex(layer_names[1]).next_to(np.array((2.5, -0.75, 0.0)), DOWN)
        feed_text.scale(0.3)  # Decrease the font size by scaling
        self.play(FadeIn(feed_text), run_time=2)
        self.wait()

        # Play animation
        forward_pass = nn.make_forward_pass_animation()
        # Play animation
        self.play(forward_pass, run_time=30)
        self.wait(2)