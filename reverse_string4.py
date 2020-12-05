def reverse(string):
    string = ''.join(reversed(string))
    return string


string = '123456'
print('The original string is :', string)
print('The reversed string is :', reverse(string))