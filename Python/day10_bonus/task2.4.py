def count_lines(file_to_read):
    try:
        with open(file_to_read, "r") as file:
            content = file.readlines()
            return len(content)
    except FileNotFoundError:
        return "File Not Found"
    except PermissionError:
        return "Permission Denied"
    except UnicodeDecodeError:
        return "Unicode Error"

print(count_lines("zen.txt"))
