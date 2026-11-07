import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import threading
import roulette_num_groups as r


# Functions
def get_data_type_percentage(data_list, data_type):
    # returns the perecentage of data in a data list matching the data type given
    num_of_match = 0
    num_of_data = len(data_list)
    if num_of_data == 0:
        return "NA"
    elif num_of_data > 0:
        for data in data_list:
            if data in data_type:
                num_of_match += 1
        percentage = num_of_match / num_of_data * 100
        return format(percentage, ".2f")

def get_2D_grid_positions_ordered_list(row_num, column_num, row_start=0, column_start=0, mode="left-down"):
    #returns a list of [row, column] positions of a 2D grid in an order dedicted by the mode
    #row/column_start indicates the lowest row/column index of the desired 2D grid
    #first direction in mode indicates going through that row/column first before starting again at the next column/row going by the second direction
    positions = []
    if mode == "left-down":
        for row in range(row_start, row_start+row_num):
            for column in range(column_start, column_start+column_num):
                positions.append([row,column])
    elif mode == "left-up":
        for row in range(row_start+row_num-1, row_start-1, -1):
            for column in range(column_start, column_start+column_num):
                positions.append([row,column])
    elif mode == "right-down":
        for row in range(row_start, row_start+row_num):
            for column in range(column_start+column_num-1, column_start-1, -1):
                positions.append([row,column])
    elif mode == "right-up":
        for row in range(row_start+row_num-1, row_start-1, -1):
            for column in range(column_start+column_num-1, column_start-1, -1):
                positions.append([row,column])
    elif mode == "down-left":
        for column in range(column_start, column_start+column_num):
            for row in range(row_start, row_start+row_num):
                positions.append([row,column])
    elif mode == "down-right":
        for column in range(column_start+column_num-1, column_start-1, -1):
            for row in range(row_start, row_start+row_num):
                positions.append([row,column])
    elif mode == "up-left":
        for column in range(column_start, column_start+column_num):
            for row in range(row_start+row_num-1, row_start-1, -1):
                positions.append([row,column])
    elif mode == "up-right":
        for column in range(column_start+column_num-1, column_start-1, -1):
            for row in range(row_start+row_num-1, row_start-1, -1):
                positions.append([row,column])
    else:
        print("Invalid mode input.")
    return positions

# Root
root = tk.Tk()
root.title("Roulette Predictor")
root.configure(bg="green")


# Global variables
data_list = []
probabilities = [get_data_type_percentage(data_list=data_list, data_type=data_type) for data_type in r.cabinets_mattroy_groups]
prob_texts = [f"{r.cabinets_mattroy_groups_names[i]}\n({probabilities[i]})" for i in range(0,4)]
prob_displays = []
for text in prob_texts:
    display = tk.StringVar()
    display.set(text)
    prob_displays.append(display)
def update_probabilities():
    global probabilities
    global prob_texts
    global prob_displays
    probabilities = [get_data_type_percentage(data_list=data_list, data_type=data_type) for data_type in r.cabinets_mattroy_groups]
    prob_texts = [f"{r.cabinets_mattroy_groups_names[i]}\n({probabilities[i]})" for i in range(0,4)]
    for i in range(0,4):
        prob_displays[i].set(prob_texts[i])
    return

# Data Display
data_locations = get_2D_grid_positions_ordered_list(4, 5)

def display_added_data(frame, locations):
    Data_Display_font = tkFont.Font(size=12)
    global data_list
    for index in range(0, len(data_list)):
        data = data_list[index]
        Data_Display_colour = r.get_number_colour(data)
        data_label = tk.Label(frame, text=f"{data}", font=Data_Display_font, bg=Data_Display_colour, fg="white", width=3)
        data_label.grid(row=locations[index][0], column=locations[index][1])
    return
def add_data(number, frame, locations):
    global data_list
    data_list.insert(0, number)
    while len(data_list) > 20:
        data_list.pop()
    display_added_data(frame, locations)
    update_probabilities()
    return
def clear_data_background(frame, bar):
    global data_list
    bar.start()
    frame.destroy()
    data_list.clear()
    frame = tk.Frame(root, bg="green", relief="ridge")
    frame.grid(row=1, column=0, padx=10, pady=10)
    update_probabilities()
    bar.stop()
    return
def clear_data(frame, bar): # Put task on separate thread so the progress bar actaully moves, still laggy so it might not move before task is done
    threading.Thread(target=clear_data_background, args=(frame, bar), daemon=True).start()
    return

Data_Display_title = tk.Label(root, text="Data", bg="green", fg="white")
Data_Display_title.grid(row=0, column=0)
Data_Display_frame = tk.Frame(root, bg="green", relief="ridge")
Data_Display_frame.grid(row=1, column=0, padx=10, pady=10)
clearing_progress_bar = ttk.Progressbar(root, orient="horizontal", length=50, mode='indeterminate')
clearing_progress_bar.grid(row=3, column=0, padx=10, pady=10)
Clear_Data_button = tk.Button(root, text="Clear Data", command=lambda: clear_data(Data_Display_frame, clearing_progress_bar))
Clear_Data_button.grid(row=2, column=0, padx=0, pady=0)


# Numbers Table
number_locations = get_2D_grid_positions_ordered_list(3, 12, column_start=1, mode="up-left")
Number_Button_width = 3
Number_Button_font = tkFont.Font(size=12)

def create_number_button(number, frame, font, width, locations):
    number_button = tk.Button(
        frame,
        text=f"{number}",
        bg=r.get_number_colour(number),
        fg='white', font=font,
        width=width,
        command=lambda: add_data(number, Data_Display_frame, data_locations)
    )
    number_button.grid(row=locations[number-1][0], column=locations[number-1][1])
    return

Numbers_Table_title = tk.Label(root, text="Numbers Table\n(Click to add data)", bg="green", fg="white")
Numbers_Table_title.grid(row=4, column=0, padx=0, pady=0)
Numbers_Table_frame = tk.Frame(root, bg="white", relief="ridge")
Numbers_Table_frame.grid(row=5, column=0, padx=10, pady=10)
Button_0 = tk.Button(Numbers_Table_frame,
    pady=33,
    text="0",
    bg="green",
    fg="white",
    font= Number_Button_font,
    width=Number_Button_width,
    command=lambda: add_data(0, Data_Display_frame, data_locations)
)
Button_0.grid(row=0, column=0, rowspan=3)
for number in range(1,37):
    create_number_button(number, Numbers_Table_frame, Number_Button_font, Number_Button_width, number_locations)


# Cabinets Mattroy Widgets

Cabinets_Mattroy_title = tk.Label(root, text="Cabinets Mattroy Display", bg="green", fg="white")
Cabinets_Mattroy_title.grid(row=6, column=0, padx=0, pady=0)
Cabinets_Mattroy_frame = tk.Frame(root, bg="green", relief="ridge")
Cabinets_Mattroy_frame.grid(row=7, column=0, padx=0, pady=0)

Cabinets_Mattroy_wheel_image = tk.PhotoImage(file="1024px-european_roulette_wheel.svg-3093964181.png")
Cabinets_Mattroy_wheel_widget = tk.Label(Cabinets_Mattroy_frame, image=Cabinets_Mattroy_wheel_image, bg="green")
Cabinets_Mattroy_wheel_widget.grid(row=0, column=0, rowspan=4)
Cabinets_Mattroy_wheel_widget.image = Cabinets_Mattroy_wheel_image # Prevents Python garbage collection, fixes display issue

Jeu_0_widget = tk.Label(Cabinets_Mattroy_frame, textvariable=prob_displays[0], bg="green", fg="white")
Jeu_0_widget.grid(row=0, column=1)

Voisins_du_Zero_widget = tk.Label(Cabinets_Mattroy_frame, textvariable=prob_displays[1], bg="green", fg="white")
Voisins_du_Zero_widget.grid(row=1, column=1)

Orphelins_widget = tk.Label(Cabinets_Mattroy_frame, textvariable=prob_displays[2], bg="green", fg="white")
Orphelins_widget.grid(row=2, column=1)

Tiers_du_Cylindre_widget = tk.Label(Cabinets_Mattroy_frame, textvariable=prob_displays[3], bg="green", fg="white")
Tiers_du_Cylindre_widget.grid(row=3, column=1)

# Running the program
root.mainloop()