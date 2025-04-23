import re
text = 'The quick brown fox jumps over the lazy dog . Fox being fox'

match = re.search(r"fox", text)

if match:
    print("Found : ", match.group())

matches = re.findall(r"the", text ,re.IGNORECASE)
print(matches)

new_text = re.sub(r"fox", "cat", text)
print(new_text)