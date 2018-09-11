long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])

print(long_string[:4] + ' Be there')

print('%c is my %s letter and mu number %d number is %.5f' % ('X', 'favorite', 1, .14))


print(long_string.capitalize())

print(long_string.find('Floor'))

print(long_string.isalpha())

print(long_string.isalnum())

print(len(long_string))

print(long_string.replace('Floor', 'Ground'))

print(long_string.strip())

quote_list = long_string.split(' ')
print(quote_list)
