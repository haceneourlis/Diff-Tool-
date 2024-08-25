import sys

from diff import diff

def read_file_into_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]  # Use strip() to remove the trailing newline characters

def print_lines(lines):
    for line in lines:
        print(line)
        
def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py file1 file2")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    lines1 = read_file_into_list(file1)
    lines2 = read_file_into_list(file2)

    tableau = diff(lines1,lines2)

    print_lines(tableau)
   

if __name__ == "__main__":
    main()
