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

def print_array(array):
    for row in array:
        print(" ".join(map(str, row)))

def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

array = create_odd_value_array(rows, columns)

print("\nThe array filled with odd values:")
print_array(array)

del array
print("\nArray has been removed from memory.")

if __name__ == "__main__":
    main()
