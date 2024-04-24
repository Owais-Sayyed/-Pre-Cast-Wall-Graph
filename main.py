import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

mydict = {"CONTOUR_": ["red", "green"], "OPENING": ["blue", "orange"], "LIFTING": ["purple", "yellow"]}


def open_file():
    filepath = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("All files", "*.*"), ("Text files", "*.txt")))
    if filepath:
            plot_lines_from_file(filepath, mydict)
            plt.legend()
            plt.show()
        # with open(filepath) as file:
            # plot_lines_from_file(file, mydict)


def plot_lines_from_file(filename, mydict):
    CONTOUR_cout = 0
    OPENING_count = 0
    LIFTING_ANCHOR_count = 0
    count=0
    loop_on = False
    colour = None

    with open(filename, 'r') as file:
        for line in file:
            words = line.split()

            if loop_on:
                if line.startswith("S"):
                    int_array = []
                    for text in line.split():
                        try:
                            int_array.append(int(text))
                        except ValueError:
                            pass
                    if len(int_array) > 0:
                        print(int_array)
                    x1, y1, x2, y2 = int_array[0], int_array[1], int_array[2], int_array[3]
                    plt.plot([x1, x2], [y1, y2], label=lab if count == 0 else '', color=colour)
                    count+=1
                    
                elif line.startswith("END"):
                    loop_on = False

            for word in words:
                if loop_on:
                    break
                else:
                    # Check in Dictionary
                    if word in mydict:
                        loop_on = True
                        count=0
                        if word == "CONTOUR_":
                            lab=word
                            colour = mydict["CONTOUR_"][CONTOUR_cout]
                            CONTOUR_cout += 1
                        elif word == "OPENING":
                            lab=word
                            colour = mydict["OPENING"][OPENING_count]
                            OPENING_count += 1
                        elif word == "LIFTING":
                            lab=word
                            colour = mydict["LIFTING"][LIFTING_ANCHOR_count]
                            LIFTING_ANCHOR_count += 1
root = tk.Tk()
root.title("File Reader")
# Set the size of the window
root.geometry("300x150")

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=(50,30))

root.mainloop()
