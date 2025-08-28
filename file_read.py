with open("input.txt", "w") as f:
    f.write("Python is fun.\n")
    f.write("File handling is important.\n")
    f.write("We are learning OOP.\n")
    f.write("Practice makes perfect.\n")
    f.write("Keep coding every day.\n")

with open("input.txt", "r") as f:
    content = f.read()

word_count = len(content.split())
content_upper = content.upper()

with open("output.txt", "w") as f:
    f.write(content_upper)
    f.write(f"\n\nWORD COUNT: {word_count}\n")

print("output.txt has been created with processed content.")