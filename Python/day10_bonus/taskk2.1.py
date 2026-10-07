def read_file(file_to_read):
    try:
        with open(file_to_read, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except OSError as e:
        print("An error occurred:", e)

read_file("primes.txt")