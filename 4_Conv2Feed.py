from manim import *

from manim_ml.neural_network import NeuralNetwork, Convolutional2DLayer, ImageLayer, FeedForwardLayer, MaxPooling2DLayer
from manim_ml.neural_network.animations.dropout import make_neural_network_dropout_animation

# This changes the resolution of our rendered videos
config.pixel_height = 700
config.pixel_width = 1900
config.frame_height = 7.0
config.frame_width = 7.0

# Here we define our basic scene
class Conv2Max(ThreeDScene):

    # The code for generating our scene goes here
    def construct(self):
        # Make neural networks
        nn_feed = NeuralNetwork([
            FeedForwardLayer(3),
            FeedForwardLayer(5),
            FeedForwardLayer(4),
        ],
            layer_spacing=0.25,
        )
        nn = NeuralNetwork([

            Convolutional2DLayer(5, 2, 2),
            nn_feed
        ],
            layer_spacing=0.25,
        )
        # Center the nn
        nn.move_to(ORIGIN)
        self.add(nn)
        # Play animation
        forward_pass = nn.make_forward_pass_animation()
        self.wait(1)
        self.play(forward_pass,  make_neural_network_dropout_animation(
        nn, dropout_rate=0.25, do_forward_pass=True), run_time=30)