from tkinter import *
from tkinter import messagebox

def draw_text(canvas, x, y, text):
    font_size = 12
    if len(text) == 4:
        font_size = 8
    elif len(text) >= 5:
        font_size = 7

    inserted_text = canvas.create_text(x,y, font="Times " + str(font_size) + " bold", text=text)
    canvas.tag_raise(inserted_text)
    canvas.pack(fill=BOTH)

def draw_circle(canvas, x, y):
    canvas.create_oval(x - 15, y - 15, x + 15, y + 15, outline="black",
                       fill="lightblue", width=2)
    draw_text(canvas,x,y,"1")
    canvas.pack(fill=BOTH)

def draw_line(canvas, x_start, y_start, x_end, y_end):
    line = canvas.create_line(x_start, y_start,x_end, y_end, width=2)
    canvas.tag_lower(line)
    canvas.pack(fill=BOTH)


def insert_new_node():
    try:
        i = int(number_input.get())
        print(i)
    except:
        messagebox.showerror("Value error", "Please enter a number!")
    number_textbox.delete(0, 'end')

################################
#      MAIN to run GUI
################################

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

number_input = StringVar(top_frame)

number_textbox = Entry(top_frame, width=10, textvariable=number_input)
number_textbox.pack(side=LEFT, pady=4, padx=4)

insert_button = Button(top_frame, text="Insert", command= lambda: insert_new_node())
insert_button.pack(side=LEFT)

draw_circle(canvas, 700, 20)
draw_line(canvas, 700, 20, 770, 90)

root.mainloop()