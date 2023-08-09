from manim import *
import numpy as np
from PIL import Image
from manim_ml.neural_network import NeuralNetwork, Convolutional2DLayer, ImageLayer, MaxPooling2DLayer, FeedForwardLayer

# This changes the resolution of our rendered videos

config.frame_height = 9.0
config.frame_width = 12.0

# Here we define our CNN scene
class MNISTCNN(ThreeDScene):
    def construct(self):
        image = Image.open("digitX2.jpg")
        numpy_image = np.asarray(image)
        layers = [
            ImageLayer(numpy_image, height=1.5),
            Convolutional2DLayer(1, 14, filter_spacing=0.32),
            Convolutional2DLayer(3, 12, 3, filter_spacing=0.65),
            MaxPooling2DLayer(kernel_size=2, filter_spacing=0.45),
            Convolutional2DLayer(5, 4, 4, filter_spacing=0.18),
            MaxPooling2DLayer(kernel_size=2, filter_spacing=0.18),
            FeedForwardLayer(10, node_radius=0.08, node_stroke_width=1.75,
                             rectangle_color=BLACK, node_spacing=0.3)
            ]

        nn = NeuralNetwork(layers,
            layer_spacing=0.5,
        )

        # Center the neural network
        nn.move_to(np.array((-0.75, -1.0, 0.0)))

        self.add(nn)

        # Create text labels and brackets for each layer
        layer_names = ["Input", "Feature Maps", "Pooled Maps", "Output"]

        in_text = Tex(layer_names[0]).next_to(np.array((-1.5, -1.0, 0.0)), DOWN)
        in_text.scale(0.23)  # Decrease the font size by scaling
        self.play(FadeIn(in_text), run_time=1)
        self.wait()

        conv_text = Tex(layer_names[1]).next_to(np.array((-0.25, -1.0, 0.0)), DOWN)
        conv_text.scale(0.23)  # Decrease the font size by scaling
        self.play(FadeIn(conv_text), run_time=1)
        self.wait()

        pool_text = Tex(layer_names[2]).next_to(np.array((0.25, -1.0, 0.0)), DOWN)
        pool_text.scale(0.23)  # Decrease the font size by scaling
        self.play(FadeIn(pool_text), run_time=1)
        self.wait()

        conv_text = Tex(layer_names[1]).next_to(np.array((0.75, -1.0, 0.0)), DOWN)
        conv_text.scale(0.23)  # Decrease the font size by scaling
        self.play(FadeIn(conv_text), run_time=1)
        self.wait()

        pool_text = Tex(layer_names[2]).next_to(np.array((1.35, -1.0, 0.0)), DOWN)
        pool_text.scale(0.23)  # Decrease the font size by scaling
        self.play(FadeIn(pool_text), run_time=1)
        self.wait()

        feed_text = Tex(layer_names[3]).next_to(np.array((2.4, -1.0, 0.0)), DOWN)
        feed_text.scale(0.23)  # Decrease the font size by scaling
        self.play(FadeIn(feed_text), run_time=1)
        self.wait()



        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation()
        # Play animation
        self.play(forward_pass, run_time=50)
        self.wait(2)



