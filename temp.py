from manim import *

class ColorCell(Scene):
    def construct(self):
        # Create a 3x3 table
        table = MathTable(
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],
            include_outer_lines=True)

        # Color the part of the table
        for i in range(1, 3):
            for j in range(1, 3):
                table.get_entries()[i][j].set_color(YELLOW)

        self.play(Write(table))
        self.wait()
