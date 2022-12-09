number_grid = [[1, 2, 3], [-1, 0, 5], [8, -2, 4], [1.53]]
rows = 4
columns = 3
print(number_grid[3][0])
print(len(number_grid[3]))
print(number_grid)

for r in range(rows):
    print(number_grid[r])

# alternatively:
for i in number_grid:
    print(i)

# to print all elements wo brackets
for row in number_grid:
    for col in row:
        print(col)


# passing a single index in a 2d list is equivalent to interacting with each element, which
# itself is a list.
