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
        layer_names = ["Input\nLayer", "Hidden Layer ", "Output\nLayer"]
        layer_brackets = ["Convolution", "Max Pooling"]

        in_text = Tex(layer_names[0]).next_to(np.array((-3.5, -2.25, 0.0)), DOWN)
        in_text.scale(0.35)  # Decrease the font size by scaling
        self.play(FadeIn(in_text), run_time=0.5)

        conv_text1 = Tex(layer_names[1] + "1").next_to(np.array((-2.0, -2.25, 0.0)), DOWN)
        conv_text1.scale(0.30)  # Decrease the font size by scaling
        self.play(FadeIn(conv_text1), run_time=0.5)
        conv_brac1 = Tex("(Convolution 1)").next_to(conv_text1, np.array((0.0, -0.1, 0.0)))
        conv_brac1.scale(0.30)  # Decrease the font size by scaling
        self.play(FadeIn(conv_brac1), run_time=0.5)
        self.wait()

        pool_text1 = Tex(layer_names[1] + "2").next_to(np.array((0.25, -2.25, 0.0)), DOWN)
        pool_text1.scale(0.30)  # Decrease the font size by scaling
        self.play(FadeIn(pool_text1), run_time=1)
        pool_brac1 = Tex("(Max Pool 1)").next_to(pool_text1, np.array((0.0, -0.1, 0.0)))
        pool_brac1.scale(0.30)  # Decrease the font size by scaling
        self.play(FadeIn(pool_brac1), run_time=0.5)
        self.wait()
        self.wait()

        conv_text2 = Tex(layer_names[1] + "3").next_to(np.array((1.8, -2.25, 0.0)), DOWN)
        conv_text2.scale(0.30)  # Decrease the font size by scaling
        self.play(FadeIn(conv_text2), run_time=1)
        conv_brac2 = Tex("(Convolution 2)").next_to(conv_text2, np.array((0.0, -0.1, 0.0)))
        conv_brac2.scale(0.30)  # Decrease the font size by scaling
        self.play(FadeIn(conv_brac2), run_time=0.5)
        self.wait()
        self.wait()

        pool_text2 = Tex(layer_names[1] + "4").next_to(np.array((3.2, -2.25, 0.0)), DOWN)
        pool_text2.scale(0.30)  # Decrease the font size by scaling
        self.play(FadeIn(pool_text2), run_time=1)
        pool_brac2 = Tex("(Max Pool 2)").next_to(pool_text2, np.array((0.0, -0.1, 0.0)))
        pool_brac2.scale(0.30)  # Decrease the font size by scaling
        self.play(FadeIn(pool_brac2), run_time=0.5)
        self.wait()

        out_text = Tex(layer_names[2]).next_to(np.array((4.45, -2.25, 0.0)), DOWN)
        out_text.scale(0.35)  # Decrease the font size by scaling
        self.play(FadeIn(out_text), run_time=1)

        # Make a forward pass animation
        # forward_pass = nn.make_forward_pass_animation()
        # Play animation
        # self.play(forward_pass, run_time=100)
        self.wait(2)
