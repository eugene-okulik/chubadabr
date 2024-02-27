words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
print(*[word * int(words[word]) for word in words], sep='\n')
