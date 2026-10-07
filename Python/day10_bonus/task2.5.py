def create_file(directory):
    file_path = directory + "/toto.txt"
    try:
        with open("toto.txt", "w") as file:
            file.write("Hello!")
    except IOError:
        print("File cannot be opened")
    except FileExistsError:
        print("File already exists")

create_file("day10_bonus")
