def read_file_into_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]  # Use strip() to remove the trailing newline characters

# Example usage
filename = 'new.txt'
lines = read_file_into_list(filename)
print(lines)
