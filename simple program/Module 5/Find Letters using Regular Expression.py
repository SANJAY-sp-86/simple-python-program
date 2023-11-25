import re

input_text = '12Hello32hai'
letters = re.findall(r'[a-zA-Z]', input_text)
print("Letters in the input:", letters)
