import re

text = 'example program exercise'
matches = re.findall(r'ex', text)
print("Occurrences of 'ex':", matches)
