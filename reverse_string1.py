def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str


s = 'HASNAT OSMAN'
print('The original string is :', end=' ')
print(s)

print('The reversed string (using loop) is :', end=' ')
print(reverse(s))
