def reverse(string):
    result = ''
    for i in range(len(string)-1,-1,-1):
        result += string[i]
    return result


string = str(input("Введите x: "))
if reverse(string) == string:
    print(True)
else:
    print(False)