import re

text_filename = '''The Project Gutenberg eBook of
Heart of Darkness,
by Joseph Konrad'''

# slicing 31st to 48th character
print('text_filename[31:48] = ', text_filename[31:48])

# test if substring exists
if '.txt' not in text_filename:
	print("Appending txt file extension")
	text_filename += ".txt"

# find and replace
text_filename = text_filename.replace('\n', ' ')
text_filename = text_filename.replace("Konrad", "Conrad")

# RegEx
emails = 'aaa@gmail.com bbb@hotmail.com ccc@apple.com'
print(re.sub('[a-z]*@', 'name@', emails))
print(re.sub('[a-z]*@', 'name@', emails, 2))
t = re.subn('[a-z]*@', 'name@', emails)
print(t)
print(type(t))
print(t[0])
print(t[1])

# open text tile
with open(text_filename, 'r') as text_file:
	lines = text_file.read()

str_count1 = lines.count("Kurtz")  # counting the character “o” in the givenstring
print("The count of 'Kurtz' is", str_count1)