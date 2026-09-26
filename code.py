# Data annotations for characters and their positions Practice Code 1
characters = [
   (0,0,"█"),
   (0,1,"█"),
   (0,2,"█"), 
   (1,0,"▀"),
   (2,0,"▀"),
   (3,0,"▀"),
   (1,1,"▀"),
   (2,1,"▀")   
]

max_x = max([x for x, y, char in characters])
max_y = max([y for x, y, char in characters])

#for x, y, char in characters:
#  print(f"Character '{char}' at position ({x}, {y})")

grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]  

# print("Grid dimensions:", max_x + 1, "x", max_y + 1)

for x, y, char in characters:
    # print(f"Placing character '{char}' at position ({x}, {y})")
    grid[y][x] = char

for row in grid:
    print("".join(row))
