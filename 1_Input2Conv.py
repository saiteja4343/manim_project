from manim import *
import numpy as np
from PIL import Image
from manim_ml.neural_network import NeuralNetwork, Convolutional2DLayer, ImageLayer

# This changes the resolution of our rendered videos
config.pixel_height = 700
config.pixel_width = 1900
config.frame_height = 7.0
config.frame_width = 7.0

# Here we define our CNN scene
class Input2Conv(ThreeDScene):
    def construct(self):
        image = Image.open("digitX2.jpg")  # You will need to download an image of a digit.
        numpy_image = np.asarray(image)
        layers = [
            ImageLayer(numpy_image, height=1.5),
            Convolutional2DLayer(1, 7, 3, filter_spacing=0.32),
            Convolutional2DLayer(3, 5, 3, filter_spacing=0.32),
            Convolutional2DLayer(5, 3, 3, filter_spacing=0.18),

        ]

        nn = NeuralNetwork(layers,
            layer_spacing=0.5,
        )
        title = Text("Convolution using Image in CNN")
        title.next_to(np.array((0.0, 0.5, 0.0)), DOWN)
        title.scale(0.7)
        self.play(FadeIn(title), run_time=2)
        self.wait(1)
        self.play(title.animate.set_color(YELLOW_B))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)
        # Center the neural network
        nn.move_to(np.array((-1.0, 0.0, 0.0)))

        # Add the neural network to the scene
        self.add(nn)

        # Create text labels and brackets for each layer
        layer_names = ["Image Layer", "Feature Maps", "Pooled Feature Maps"]
        dir = [UP, DOWN]
        for i, layer in enumerate(layers):
            if i > 0:
                #layer_label = Text(layer_names[i]).next_to(layer, UP)
                #brace = Brace(layer, direction=UP)
                #brace.scale(0.5)
                b_text = Tex(layer_names[i-1]).next_to(layer, dir[i%2])
                b_text.scale(0.3)  # Decrease the font size by scaling
                self.play(FadeIn(b_text), run_time=2)
                self.wait()
                self.play(b_text.animate.set_color(BLUE_B))
                self.wait(1)
        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation()

        # Play animation
        self.play(forward_pass, run_time=100)
        self.wait(2)