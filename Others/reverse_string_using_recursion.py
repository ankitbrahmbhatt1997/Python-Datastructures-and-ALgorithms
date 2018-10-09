def reverse(str):
    if len(str) <= 1:
        return str

    return reverse(str[1:]) + str[0]


print(reverse("HelloWorld"))
