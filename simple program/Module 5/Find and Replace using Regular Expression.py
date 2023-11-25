import re

string_to_modify = "xyz-abc:pqr"
modified_string = re.sub(r'[-:]', ' ', string_to_modify)
print("Modified String:", modified_string)
