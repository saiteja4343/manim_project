from manim import *
import numpy as np
from PIL import Image
from manim_ml.neural_network import NeuralNetwork, FeedForwardLayer, Convolutional2DLayer, ImageLayer

# Here we define our basic scene
class BasicScene(ThreeDScene):
    def construct(self):
        image = Image.open("digit.jpeg")  # You will need to download an image of a digit.
        numpy_image = np.asarray(image)

        nn = NeuralNetwork([
            ImageLayer(numpy_image, height=1.5),
            Convolutional2DLayer(1, 7, 3, filter_spacing=0.32),  # Note the default stride is 1.
            Convolutional2DLayer(3, 5, 3, filter_spacing=0.32),
            Convolutional2DLayer(5, 3, 3, filter_spacing=0.18),
            FeedForwardLayer(3),
            FeedForwardLayer(3),
        ],
            layer_spacing=0.25,
        )
        # Center the neural network
        nn.move_to(ORIGIN)
        self.add(nn)
        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation()
        # Play animation
        self.play(forward_pass)


