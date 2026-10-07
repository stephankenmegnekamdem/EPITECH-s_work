def read_line(file_to_read):

        with open(file_to_read, "r") as file:
            for line in file:
             print(line, end="")

try:
    read_line("primes.txt")
except FileNotFoundError:
        print("File not found.")
except PermissionError:
        print("Permission denied.")
except OSError as e:
        print("An error occurred:", e)