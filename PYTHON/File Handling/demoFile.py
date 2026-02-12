import os
with open("DATA-ANALYST-ROADMAP/PYTHON/File Handling/file.txt") as f:
  for x in f:
    print(x)

with open("file.txt", "w") as f:
  f.write("Woops! I have deleted the content!")



if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

os.rmdir("myfolder")
