import csv

print("You may search for: Action, Strategy, Casual, RPG, Simulation, Sports, or Racing")
search_val = input("Enter the category you wish to search for: ")
search_val = search_val.title()
print("Search value = ", search_val)

f = open('database.csv')
csv_f = csv.reader(f)

num_of_matches = 0
matching_games = []
for row in csv_f:
  print(row[2])
  if search_val in row[2]:
      num_of_matches += 1
      matching_games.append(row[0])


print(num_of_matches)
print(matching_games)



