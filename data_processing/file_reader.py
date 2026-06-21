with open("data.txt", "r") as f:
    content = f.readlines()
print(content)


with open("data.txt", "r") as f:
    contents = f.readlines()
for i, contents in enumerate(contents):
    contents[i] = contents.strip()
print(contents)
stripped = [contents.strip() for contents in contents]

print(stripped)


