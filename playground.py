import glob

my_files = glob.glob("file/*.txt")

my_files.sort()

for item in my_files:
    with open(item, "r") as files:
        print(files.read())

