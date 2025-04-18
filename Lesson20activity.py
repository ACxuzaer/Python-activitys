def mirrored_right_triangle(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * i
        print(spaces + stars)

# Example usage
rows = int(input("Enter number of rows: "))
mirrored_right_triangle(rows)
