def rewrite(file_name_from,file_name_to):
    try:
        with open(file_name_from,'r') as file:
            content = file.read()
        with open(file_name_to,'w') as file:
            file.write(content)
    except FileNotFoundError:
        return "file not found"
rewrite("zen.txt","toto.txt")