def write_to_file(file_name):
    try:
        with open(file_name, 'r+') as f:
            f.write("I'm a new line\n")
    except IOError:
        return "InputOutput Error"

write_to_file("toto.txt")