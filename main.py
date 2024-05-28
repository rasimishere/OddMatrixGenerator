def create_odd_value_array(rows, columns):
    array = []
    odd_value = 1
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(odd_value)
            odd_value += 2
        array.append(row)
    return array
