from manim import *
import itertools as it

class MyNeuralNetwork(Scene):
    def construct(self):
        myNN = NeuralNetworkMobject([784, 5, 1])
        myNN.scale(0.75)

        self.play(Create(myNN))
        self.wait()

        myNN.label_inputs("x")
        myNN.label_outputs(r"\hat{y}")
        myNN.label_outputs_text("Predicts the digit")
        myNN.label_hidden_layers("a")

        self.wait()

# A customizable Sequential Neural Network
class NeuralNetworkMobject(VGroup):
    def __init__(self, neural_network, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layer_sizes = neural_network
        self.neuron_radius = 0.15
        self.neuron_to_neuron_buff = MED_SMALL_BUFF
        self.layer_to_layer_buff = LARGE_BUFF
        self.output_neuron_color = WHITE
        self.input_neuron_color = WHITE
        self.hidden_layer_neuron_color = WHITE
        self.neuron_stroke_width = 2
        self.neuron_fill_color = GREEN
        self.edge_color = LIGHT_GREY
        self.edge_stroke_width = 2
        self.edge_propagation_color = YELLOW
        self.edge_propagation_time = 1
        self.max_shown_neurons = 16
        self.brace_for_large_layers = True
        self.average_shown_activation_of_large_layer = True
        self.include_output_labels = False
        self.arrow = False
        self.arrow_tip_size = 0.1
        self.left_size = 1
        self.neuron_fill_opacity = 1

        self.add_neurons()
        self.add_edges()
        self.add_to_back(self.layers)

    def add_neurons(self):
        self.layers = VGroup()
        for index, size in enumerate(self.layer_sizes):
            layer = self.get_layer(size, index)
            self.layers.add(layer)
        self.layers.arrange(RIGHT, buff=self.layer_to_layer_buff)
        if self.include_output_labels:
            self.label_outputs_text()

    def get_layer(self, size, index=-1):
        layer = VGroup()
        n_neurons = size
        if n_neurons > self.max_shown_neurons:
            n_neurons = self.max_shown_neurons
        neurons = VGroup()
        for x in range(n_neurons):
            neuron = Circle(
                radius=self.neuron_radius,
                stroke_color=self.get_nn_fill_color(index),
                stroke_width=self.neuron_stroke_width,
                fill_color=BLACK,
                fill_opacity=self.neuron_fill_opacity,
            )
            neurons.add(neuron)
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()
        neurons.arrange(DOWN, buff=self.neuron_to_neuron_buff)
        layer.neurons = neurons
        layer.add(neurons)

        if size > n_neurons:
            dots = Tex("\\vdots")
            dots.next_to(neurons, DOWN, MED_SMALL_BUFF)
            layer.dots = dots
            layer.add(dots)
            if self.brace_for_large_layers:
                brace = Brace(layer, LEFT)
                brace_label = brace.get_tex(str(size))
                layer.brace = brace
                layer.brace_label = brace_label
                layer.add(brace, brace_label)

        return layer

    def get_nn_fill_color(self, index):
        if index == -1 or index == len(self.layer_sizes) - 1:
            return self.output_neuron_color
        elif index == 0:
            return self.input_neuron_color
        else:
            return self.hidden_layer_neuron_color

    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)

    def get_edge(self, neuron1, neuron2):
        if self.arrow:
            return Arrow(
                neuron1.get_center(),
                neuron2.get_center(),
                buff=self.neuron_radius,
                stroke_color=self.edge_color,
                stroke_width=self.edge_stroke_width,
                tip_length=self.arrow_tip_size
            )
        else:
            return Line(
                neuron1.get_center(),
                neuron2.get_center(),
                buff=self.neuron_radius,
                stroke_color=self.edge_color,
                stroke_width=self.edge_stroke_width,
            )

    def label_inputs(self, l):
        self.output_labels = VGroup()
        input_layer = self.layers[0]
        for n, neuron in enumerate(input_layer.neurons):
            label = MathTex(f"{l}_{{{n + 1}}}")
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def label_outputs(self, l):
        self.output_labels = VGroup()
        output_layer = self.layers[-1]
        for n, neuron in enumerate(output_layer.neurons):
            label = MathTex(f"{l}_{{{n + 1}}}")
            label.set_height(0.4 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def label_outputs_text(self, outputs):
        self.output_labels = VGroup()
        output_layer = self.layers[-1]
        for n, neuron in enumerate(output_layer.neurons):
            label = MathTex(outputs[n])
            label.set_height(0.75 * neuron.get_height())
            label.move_to(neuron)
            label.shift((neuron.get_width() + label.get_width() / 2) * RIGHT)
            self.output_labels.add(label)
        self.add(self.output_labels)

    def label_hidden_layers(self, l):
        self.output_labels = VGroup()
        hidden_layers = self.layers[1:-1]
        for layer in hidden_layers:
            for n, neuron in enumerate(layer.neurons):
                label = MathTex(f"{l}_{{{n + 1}}}")
                label.set_height(0.4 * neuron.get_height())
                label.move_to(neuron)
                self.output_labels.add(label)
        self.add(self.output_labels)
