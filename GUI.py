from tkinter import *
from tkinter import messagebox


###############################
#   Global variables for GUI
###############################
x_gap_per_layer = [300, 140, 90, 50, 30, 20]
y_gap_per_layer = 100
starting_coordinates = [700, 20]


###############################
#   Function definitions
###############################
def draw_text(canvas, x, y, text):
    font_size = 12
    if len(text) == 4:
        font_size = 8
    elif len(text) >= 5:
        font_size = 7

    inserted_text = canvas.create_text(x,y, font="Times " + str(font_size) + " bold", text=text)
    canvas.tag_raise(inserted_text)
    canvas.pack(fill=BOTH)


def draw_circle(canvas, x, y, text):
    canvas.create_oval(x - 15, y - 15, x + 15, y + 15, outline="black",
                       fill="lightblue", width=2)
    draw_text(canvas, x, y, text)
    canvas.pack(fill=BOTH)


def draw_line(canvas, x_start, y_start, x_end, y_end):
    line = canvas.create_line(x_start, y_start,x_end, y_end, width=2)
    canvas.tag_lower(line)
    canvas.pack(fill=BOTH)


def insert_new_node():
    try:
        i = int(number_input.get())  # Gets number from input field
        # root_node = add_node(i)  # Adds the number to AVL-tree
        # clear canvas  # Clear canvas to start drawing again
        # draw_tree_recursion(canvas, root_node, starting_coordinates[0], starting_coordinates[1], 0)  # Start drawing
    except:
        messagebox.showerror("Value error", "Please enter a number!")
    number_textbox.delete(0, 'end')


def draw_example_tree_by_hand(canvas):
    # Node 1
    draw_circle(canvas, 700, 20, "10")
    draw_line(canvas, 700, 20, 1000, 90)
    draw_line(canvas, 700, 20, 400, 90)

    # Node 2
    draw_circle(canvas, 400, 90, "7")
    draw_line(canvas, 400, 90, 470, 160)
    draw_line(canvas, 400, 90, 330, 160)

    # Node 3
    draw_circle(canvas, 1000, 90, "12")
    draw_line(canvas, 1000, 90, 1070, 160)
    draw_line(canvas, 1000, 90, 930, 160)

    # Node 4
    draw_circle(canvas, 330, 160, "3")

    # Node 5
    draw_circle(canvas, 470, 160, "9")
    draw_line(canvas, 470, 160, 400, 230)

    # Node 6
    draw_circle(canvas, 400, 230, "8")

    # Node 7
    draw_circle(canvas, 1070, 160, "15")

    # Node 8
    draw_circle(canvas, 930, 160, "11")


def draw_tree_recursion(canvas, node, start_x, start_y, layer_nr):
    return

    # draw circle
    # draw_circle(canvas, start_x, start_y, str(node.value))

    # if not (node.left_child or node.right_child)
    #     return

    # draw left child and line
    # if is left child:
    #     draw_line(canvas, start_x, start_y, tart_x-x_gap_per_layer[layer_nr], start_y+y_gap_per_layer)
    #     draw_tree_recursion(canvas, node.left_child, start_x-x_gap_per_layer[layer_nr], start_y+y_gap_per_layer, layer_nr+1)

    # draw right child and line
    # if is right child:
    #     draw_line(canvas, start_x, start_y, tart_x+x_gap_per_layer[layer_nr], start_y+y_gap_per_layer)
    #     draw_tree_recursion(canvas, node.right_child, start_x+x_gap_per_layer[layer_nr], start_y+y_gap_per_layer, layer_nr+1)


def canvas_clear_all(canvas):
    canvas.delete('all')


################################
#      MAIN to run GUI
################################

# Constants
window_height = 900
window_width = 1400

# Initsialization
root = Tk()
root.geometry(str(window_width) + "x" + str(window_height) + "+300+300")
root.minsize(200, 200)
root.title("AVL-tree visualization")

top_frame = Frame(root)
top_frame.pack(side=TOP)
canvas = Canvas(root, width=window_width, height=window_height)

# User inputs
number_input = StringVar(top_frame)
number_textbox = Entry(top_frame, width=10, textvariable=number_input)
number_textbox.pack(side=LEFT, pady=4, padx=4)

insert_button = Button(top_frame, text="Insert", command= lambda: insert_new_node())
insert_button.pack(side=LEFT, padx=4)

clear_button = Button(top_frame, text="Clear", command= lambda: canvas_clear_all(canvas))
clear_button.pack(side=LEFT, padx=4)

example_button = Button(top_frame, text="Example", command= lambda: draw_example_tree_by_hand(canvas))
example_button.pack(side=LEFT, padx=4)

# Run GUI
root.mainloop()
