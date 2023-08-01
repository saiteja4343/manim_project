from manim import *

class IntroScene(Scene):
    def construct(self):
        title = Tex("Introduction to Neural Networks").scale(0.7)
        title.to_edge(UP)
        self.play(Write(title))

        myBaseTemplate = TexTemplate(
            documentclass="\documentclass[preview]{standalone}"
        )
        myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")

        # Machine Learning
        ml_text = Tex("\\justifying {Machine Learning is a type of artificial intelligence that allows computers to learn and make decisions without being explicitly programmed.}").scale(0.5)
        self.play(Write(ml_text))
        self.wait(2)
        self.play(FadeOut(ml_text))

        # Deep Learning
        dl_text = Tex("\\justifying {Deep Learning is a subset of Machine Learning that uses neural networks with many layers (deep neural networks).}").scale(0.5)
        self.play(Write(dl_text))
        self.wait(2)
        self.play(FadeOut(dl_text))

        # Neural Networks
        nn_text = Tex("\\justifying {Neural Networks are computing systems inspired by the human brain. They can learn to recognize patterns and make decisions.}").scale(0.5)
        self.play(Write(nn_text))
        self.wait(2)
        self.play(FadeOut(nn_text))

        # Neural Network Image
        nn_image = ImageMobject("dl.jpg")
        nn_image.scale(0.5)
        self.play(FadeIn(nn_image))
        self.wait(2)
        self.play(FadeOut(nn_image))

        self.play(FadeOut(title))

class DeepLearningExplanation(Scene):
    def construct(self):
        title = Text("What is Deep Learning?", color=BLUE)
        self.play(Write(title))
        self.wait(2)

        description = Text("Deep learning is a subset of machine learning that mimics the neural networks of the human brain to process data and create patterns for decision making. It's like having a team of experts, each specializing in a different aspect of the problem.", color=GREEN)
        description.next_to(title, DOWN)
        self.play(Write(description))
        self.wait(2)

        image = ImageMobject("deep_learn.png")
        image.scale(0.5)
        image.next_to(description, DOWN)
        self.play(FadeIn(image))
        self.wait(2)

class CNNExplanation(Scene):
    def construct(self):
        title = Text("What is a Convolutional Neural Network (CNN)?", color=BLUE)
        self.play(Write(title))
        self.wait(2)

        description = Text("A Convolutional Neural Network (CNN) is a type of deep learning algorithm that's excellent at processing visual data. It uses a process called convolution, which is like a filter that passes over an image and detects patterns.", color=GREEN)
        description.next_to(title, DOWN)
        self.play(Write(description))
        self.wait(2)

        image = ImageMobject("cnn.jpeg")
        image.scale(0.5)
        image.next_to(description, DOWN)
        self.play(FadeIn(image))
        self.wait(2)
