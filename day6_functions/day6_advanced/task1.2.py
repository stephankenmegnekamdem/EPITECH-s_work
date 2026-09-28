def reverse(string):
    n = len(string)

    if n <= 1:
        return string

    return string[n-1] + reverse(string[:n-1])


print(reverse("Epitech"))
