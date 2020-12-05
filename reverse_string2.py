def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = '123'
print('The original string is :', end=' ')
print(s)

print('The reversed string (using loop) is :', end=' ')
print(reverse(s))
if s == reverse(s):
    print('So it is a palindrome')
