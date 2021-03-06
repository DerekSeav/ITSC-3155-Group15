import tkinter as tk
import csv

win = tk.Tk()
win.minsize(450, 480)

# row 0
label = tk.Label(win, text="Search by name:").grid(row=0, padx=10)
search = tk.Entry().grid(row=0, column=1)
subname = tk.Button(win, text="search").grid(row=0, column=2, padx=20, pady=10)

# row 1
txtor = tk.Label(win, text="OR Search by tags:").grid(row=1, column=1, pady=20)

# row 2
# category label
catlab = tk.Label(win, text="Genre:").grid(row=2, column=0, pady=10)
# tag label
taglab = tk.Label(win, text="Tags:").grid(row=2, column=1)
# rating label
RatLab = tk.Label(win, text="ESRB Ratings:").grid(row=2, column=2)

# row 3
# category checkbox

Action = tk.IntVar()
Strategy = tk.IntVar()
Casual = tk.IntVar()
RPG = tk.IntVar()
Simulation = tk.IntVar()
Sports = tk.IntVar()
Racing = tk.IntVar()

c1 = tk.Checkbutton(win, text="Action", variable=Action).place(x=10, y=155)
c2 = tk.Checkbutton(win, text="Strategy", variable=Strategy).place(x=10, y=175)
c3 = tk.Checkbutton(win, text="Casual", variable=Casual).place(x=10, y=195)
c4 = tk.Checkbutton(win, text="RPG", variable=RPG).place(x=10, y=215)
c5 = tk.Checkbutton(win, text="Simulation", variable=Simulation).place(x=10, y=235)
c6 = tk.Checkbutton(win, text="Sports", variable=Sports).place(x=10, y=255)
c7 = tk.Checkbutton(win, text="Racing", variable=Racing).place(x=10, y=275)

# tags listbox
tags = tk.Listbox(win, height=9, xscrollcommand=True, selectmode=tk.MULTIPLE)
#puts all the tags into a list and adds them to the list box
allTags = ["2D","3D", "Adventure", "Artificial", "Boardgame", "Casual", "Competitive", "Co-op", "Crafting", "Destruction", "Exploration", "Fantasy", "First Person", "FPS", "Gore", "Grand Strategy", "Heist", "Horror", "Indie", "Intelligence", "Looter Shooter", "Magic", "Management", "Multiplayer", "Mystery", "Online Co-op", "Online PvP", "Open World", "Physics", "Platformer", "Puzzle", "PvP", "PvE", "Rogue", "Sandbox", "Science", "Shooter", "Simulation", "Single Player", "Soccer", "Space", "Survival", "Tabletop", "Tactical", "Tower Defense", "Voxel", "VR", "War"]
i = 0
for tag in allTags:
     tags.insert(i, tag)
     i += 1
tags.grid(row=3, column=1, pady=10, padx=10)

# ratings check boxes
A = tk.IntVar()
M = tk.IntVar()
T = tk.IntVar()
E10 = tk.IntVar()
E = tk.IntVar()
RP = tk.IntVar()

R1 = tk.Checkbutton(win, text="Adults only", variable=A).place(x=250, y=155)
R2 = tk.Checkbutton(win, text="M for Mature", variable=M).place(x=250, y=175)
R3 = tk.Checkbutton(win, text="T for Teen", variable=T).place(x=250, y=195)
R4 = tk.Checkbutton(win, text="E10 and up", variable=E10).place(x=250, y=215)
R5 = tk.Checkbutton(win, text="E for Everyone", variable=E).place(x=250, y=235)
R6 = tk.Checkbutton(win, text="Rating Pending", variable=RP).place(x=250, y=255)

# row 4
# tag search submission button

# function to update the output text box

def tagParse():
    # tags tuple
    tagtuple = tags.curselection()
    taglist = []
    for num in tagtuple:
        taglist.append(allTags[num])
    print(taglist)
    # rating list
    ratlist = []
    if A.get():
        ratlist.append("A")
    if M.get():
        ratlist.append("M")
    if T.get():
        ratlist.append("T")
    if E10.get():
        ratlist.append("10")
    if E.get():
        ratlist.append("E")
    if RP.get():
        ratlist.append("RP")

    # category list
    catlist = []
    if Action.get():
        catlist.append("Action")
    if Strategy.get():
        catlist.append("Strategy")
    if Casual.get():
        catlist.append("Casual")
    if RPG.get():
        catlist.append("RPG")
    if Simulation.get():
        catlist.append("Simulation")
    if Sports.get():
        catlist.append("Sports")
    if Racing.get():
        catlist.append("Racing")


    search_list = catlist
    search_ratlist = ratlist
    search_taglist = taglist
    # search_val = search_val.title()
    f = open('database.csv')
    csv_f = csv.reader(f)

    num_of_matches = 0
    matching_games = []

    for row in csv_f:
        if len(taglist) > 0:
            for tag in taglist:
                if len(search_list) > 0:
                    for value in search_list:
                        if len(search_ratlist) > 0:
                            for ratval in search_ratlist:
                                if ratval in row[3]:
                                    if value in row[2]:

                                        if tag in row[4] or tag in row[5] or tag in row[6] or tag in row[7] or tag in row[8]:
                                            num_of_matches += 1
                                            matching_games.append(row[0])
                        else:
                            if value in row[2]:
                                if tag in row[4] or tag in row[5] or tag in row[6] or tag in row[7] or tag in row[8]:
                                    num_of_matches += 1
                                    matching_games.append(row[0])
                else:
                    if len(search_ratlist) > 0:
                        for ratval in search_ratlist:
                            if ratval in row[3]:
                                if tag in row[4] or tag in row[5] or tag in row[6] or tag in row[7] or tag in row[8]:
                                    num_of_matches += 1
                                    matching_games.append(row[0])
                    else:
                        if tag in row[4] or tag in row[5] or tag in row[6] or tag in row[7] or tag in row[8]:
                            num_of_matches += 1
                            matching_games.append(row[0])
        else:
            if len(search_list) > 0:
                for value in search_list:
                    if len(search_ratlist) > 0:
                        for ratval in search_ratlist:
                            if ratval in row[3]:
                                if value in row[2]:
                                    num_of_matches += 1
                                    matching_games.append(row[0])
                    else:
                        if value in row[2]:
                            num_of_matches += 1
                            matching_games.append(row[0])
            else:
                for ratval in search_ratlist:
                    if ratval in row[3]:
                        num_of_matches += 1
                        matching_games.append(row[0])


    numMatch = 'Number of matches: ' + str(num_of_matches)
    print(numMatch)
    print(matching_games)

    output = tk.Text(win, height=10, width=40)
    output.insert(tk.END, numMatch)
    output.insert(tk.END, " Games: \n")
    for y in matching_games:
        game = y + "\n"
        output.insert(tk.END, game)
    output.place(x=100, y=310)

    win.update()


subtag = tk.Button(win, text="search", command=tagParse).grid(row=4, column=0)

win.mainloop()



