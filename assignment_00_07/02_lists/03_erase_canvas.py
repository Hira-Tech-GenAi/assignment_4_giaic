
import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser, eraser_x, eraser_y) -> None:
    #? Get eraser coordinates
    left_x = eraser_x
    top_y = eraser_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # ?Find overlapping items and set color to white
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    for item in overlapping_objects:
        if item != eraser:
            canvas.itemconfig(item, fill='white')

def main() -> None:
    root = tk.Tk()
    root.title("Eraser on Canvas")
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    #? Draw blue grid cells
    for row in range(num_rows):
        for col in range(num_cols):
            left_x: int = col * CELL_SIZE
            top_y: int = row * CELL_SIZE
            canvas.create_rectangle(left_x, top_y, left_x + CELL_SIZE, top_y + CELL_SIZE, fill="blue")

    #? Create eraser
    eraser: int = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

    #? Move the eraser with the mouse and erase touched items
    def on_mouse_move(event) -> None:
        canvas.moveto(eraser, event.x, event.y)
        erase_objects(canvas, eraser, event.x, event.y)

    # ?Bind mouse motion to eraser movement
    canvas.bind("<B1-Motion>", on_mouse_move)

    root.mainloop()

if __name__ == '__main__':
    main()
