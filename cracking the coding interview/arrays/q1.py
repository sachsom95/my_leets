def unique():
    data = input("Enter string:")
    lst = []
    for x in data:
        if x in lst:
            return "not unique"
        else:
            lst.append(x)

    return "unique"


print(unique())
