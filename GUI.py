from tkinter import *
from tkinter import messagebox
from projekt import *


###############################
#   Global variables for GUI
###############################
x_gap_per_layer = [300, 140, 80, 45, 30, 20, 10]
y_gap_per_layer = 100
starting_coordinates = [700, 20]

myTree = AVLTree()
root_node = None

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


def canvas_clear_all(canvas):
    global root_node
    root_node = None
    canvas.delete('all')


def insert_new_node(canvas):
    global root_node
    #try:
    i = int(number_input.get())  # Gets number from input field
    root_node = myTree.insert(root_node, i) # Adds the number to AVL-tree
    print(root_node.to_string())
    canvas.delete('all') # Clear canvas to start drawing again
    draw_tree_recursion(canvas, root_node, starting_coordinates[0], starting_coordinates[1], 0)  # Start drawing
    #except:
    #    messagebox.showerror("Value error", "Please enter a number!")
    number_textbox.delete(0, 'end')


def find_node():
    global root_node
    i = int(number_input.get())
    if (myTree.search(i)):
       messagebox.showinfo("Is {} in tree".format(i), "Yes!")
    else:
       messagebox.showinfo("Is {} in tree".format(i), "No!")
    number_textbox.delete(0, 'end')
    return


def delete_node(canvas):
    # global root_node
    # i = int(number_input.get())  # Gets number from input field
    # root_node = myTree.delete(root_node, i)  # Adds the number to AVL-tree
    # canvas.delete('all')  # Clear canvas to start drawing again
    # draw_tree_recursion(canvas, root_node, starting_coordinates[0], starting_coordinates[1], 0)  # Start drawing
    # number_textbox.delete(0, 'end')
    return


def draw_tree_recursion(canvas, node, start_x, start_y, layer_nr):
    # draw circle
    draw_circle(canvas, start_x, start_y, str(node.value))

    # draw left child and line
    if node.left != None:
         draw_line(canvas, start_x, start_y, start_x-x_gap_per_layer[min(layer_nr, len(x_gap_per_layer)-1)], start_y+y_gap_per_layer)
         draw_tree_recursion(canvas, node.left, start_x-x_gap_per_layer[min(layer_nr, len(x_gap_per_layer)-1)], start_y+y_gap_per_layer, layer_nr+1)

    # draw right child and line
    if node.right != None:
         draw_line(canvas, start_x, start_y, start_x+x_gap_per_layer[min(layer_nr, len(x_gap_per_layer)-1)], start_y+y_gap_per_layer)
         draw_tree_recursion(canvas, node.right, start_x+x_gap_per_layer[min(layer_nr, len(x_gap_per_layer)-1)], start_y+y_gap_per_layer, layer_nr+1)


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

insert_button = Button(top_frame, text="Insert", command= lambda: insert_new_node(canvas))
insert_button.pack(side=LEFT, padx=4)

find_button = Button(top_frame, text="Find", command= lambda: find_node())
find_button.pack(side=LEFT, padx=4)

del_button = Button(top_frame, text="Delete", command= lambda: delete_node(canvas))
del_button.pack(side=LEFT, padx=4)

clear_button = Button(top_frame, text="Clear", command= lambda: canvas_clear_all(canvas))
clear_button.pack(side=LEFT, padx=4)

# Run GUI
root.mainloop()
