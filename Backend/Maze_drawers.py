import svgwrite

OFFSET = 5
POS_X = 0
POS_Y = 0   

class Drawer:
    @staticmethod
    def draw(maze, path=None, vis = None, output_file = None):  
        """Draws the maze as an svg.

        Args:
            maze (Grid): The maze to be drawn.
            path (list, optional): The path to the solution.  If None, solution path won't be drawn. Defaults to None.
            vis (list, optional): The cells visited when finding solution.  If None, visited cells won't be marked. Defaults to None.
            output_file (string, optional): The path to the output file.  If None, it won't be saved. Defaults to None.

        Returns:
            svgwrite.Drawing
        """
        
        if output_file:
            OUTPUT_FILE = output_file
        else:
            OUTPUT_FILE = "#"
        
        canvas = svgwrite.Drawing(OUTPUT_FILE, size=("100%", "100%"), profile="tiny")

        canvas.add(
            canvas.rect(
                (POS_X, POS_Y),
                (POS_X + (OFFSET * maze.width), POS_Y + (OFFSET * maze.height)),
                fill="white",
                stroke_width=0,
            )
        )
        
        for i in  range(maze.height):
            for j in range(maze.width):
                y = i + OFFSET + POS_Y
                x = j + OFFSET + POS_X
                if maze.get_cell((i, j)).right:
                    canvas.add(
                        canvas.line(
                            (x + OFFSET, y),
                            (x + OFFSET, y + OFFSET),
                            stroke="black",
                            stroke_width=0.5,
                        )
                    )
                if maze.get_cell((i, j)).down:
                    canvas.add(
                        #Change it later 
                        canvas.line(
                            (x, y +  OFFSET),
                            (x + OFFSET, y + OFFSET),
                            stroke="black",
                            stroke_width=0.5,
                        )
                    )        
                    
            if vis:
                for cell in vis:
                    x, y = cell
                    x = (x * OFFSET) + POS_X
                    
                    
            