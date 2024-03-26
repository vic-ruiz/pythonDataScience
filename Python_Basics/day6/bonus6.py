contents = ["aaaa",
            "bbbb",
            "cccc"]

filenames = ["doc.txt", "report.text", "presentation.txt"]

for i, filename in enumerate(filenames):
    path = f"../files/{filename}"
    file = open(path, "w")
    file.writelines(contents[i])
    file.close()

for content, filename in zip(contents, filenames):
    path = f"../files/{filename}"
    file = open(path, "w")
    file.writelines(content)
    file.close()

