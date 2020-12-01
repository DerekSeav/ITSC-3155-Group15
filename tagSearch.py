import csv
import tkinter as tk

cattuple = (0,)
tagtuple = (0,)

win = tk.Tk()
win.minsize(300, 200)

#row 0
label = tk.Label(win, text="Search by name:").grid(row=0)
search = tk.Entry().grid(row=0, column=1)
subname = tk.Button(win, text="search").grid(row=0, column=2, padx=20, pady=10)

#row 1
txtor = tk.Label(win, text="OR Search by tags:").grid(row=1, column=1)

#ro2
catlab = tk.Label(win, text="Genre:").grid(row=2, column=0)
taglab = tk.Label(win, text="Tags:").grid(row=2, column=1)

#row 3
    #category listbox
category = tk.Listbox(win, height=7, width=13)
category.insert(1, "Action")
category.insert(2, "Strategy")
category.insert(3, "Casual")
category.insert(4, "RPG")
category.insert(5, "Simulation")
category.insert(6, "Sports")
category.insert(7, "Racing")
category.grid(row=3)

    #tags listbox
tags = tk.Listbox(win, height=7, width=13, xscrollcommand=True, selectmode=tk.MULTIPLE)
tags.insert(1, "2D")
tags.insert(2, "Adventure")
tags.insert(3, "Boardgame")
tags.insert(4, "Casual")
tags.insert(5, "competitive")
tags.insert(6, "Co-op")
tags.insert(7, "Destruction")
tags.insert(8, "FPS")
tags.insert(9, "Grand Strategy")
tags.insert(10, "Heist")
tags.insert(11, "Horror")
tags.insert(12, "Indie")
tags.insert(13, "Looter Shooter")
tags.insert(14, "Management")
tags.insert(15, "Multiplayer")
tags.insert(16, "Online Co-op")
tags.insert(17, "Open World")
tags.insert(18, "Physics")
tags.insert(19, "PvP")
tags.insert(20, "PvE")
tags.insert(21, "Rogue")
tags.insert(22, "Sandbox")
tags.insert(23, "Shooter")
tags.insert(24, "Single Player")
tags.insert(25, "Soccer")
tags.insert(26, "Space")
tags.insert(27, "Survival")
tags.insert(28, "Tabletop")
tags.insert(29, "Voxel")
tags.insert(30, "VR")
tags.insert(31, "War")
tags.grid(row=3, column=1, pady=10)

#row 4
result = tk.Label(win, text="Results:").grid(row=4)
output = tk.Text(win, height=10, width=13)
output.grid(row=4, column=1)

#function to update the output text box

def tagParse():
    #tagtuple = tags.get(tags.curselection())
    cattuple = category.get(category.curselection())
    search_val = cattuple[0]
    search_val = search_val.title()

    f = open('database.csv')
    csv_f = csv.reader(f)

    num_of_matches = 0
    matching_games = []

    # for row in csv_f:
    #     print(row[2])

    for row in csv_f:
        print(row[2])
        # if row[2] == search_val:
        #     print("hello")
        if search_val in row[2]:
            num_of_matches += 1
            matching_games.append(row[0])

    numMatch = 'Number of matches: ' + str(num_of_matches)
    print(numMatch)
    print(matching_games)



    output = tk.Text(win, height=10, width=20)
    output.insert(tk.END, numMatch)
    output.insert(tk.END, "Games: \n")
    for y in matching_games:
        game = y + "\n"
        output.insert(tk.END, game)
    output.grid(row=4, column=1)


    win.update()
    return 0


subtag = tk.Button(win, text="search", command=tagParse).grid(row=3, column=2)

win.mainloop()





