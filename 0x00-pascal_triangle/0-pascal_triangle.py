
def pascal_triangle(n):
    pascal_triangle_list = []

    if n <= 0:
        return pascal_triangle_list

    for i in range(n):
        row = [1]
        for j in range(i - 1):
            row.append(pascal_triangle_list[i - 1][j] + pascal_triangle_list[i - 1][j + 1])
        # add 1 when required
        if i != 0:
            row.append(1)  # back of the row is always 1
        pascal_triangle_list.append(row)

    return pascal_triangle_list
