def read_line(file_to_read, num1, num2):
    with open(file_to_read, "r") as file:
        content = file.readlines()
        for i in range(num1, num2):
            if i < len(content):
                print(content[i], end="")

try:
    read_line("primes.txt", 12, 200)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except OSError as e:
    print("An error occurred:", e)