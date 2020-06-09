import sys

# control some script features
overwrite = False

# read in list of content files, indended for use with grep
# eg $grep -l 'DOI' ../content/publications/* | python crossref-edit.py
data = sys.stdin.read()
files = data.split('\n')
files = files[:-1]

# loop over the list of files provided by grep
for fileName in files:
    print(fileName)
    f = open(fileName, 'r')
    lines = f.readlines()
    f.close()

    index = 0
    for line in lines:
        l = line.split(":")
        if l[0] == 'datePublished':
            print(line[:-1], end=" ----> '' ")
            break
        index += 1
    lines.pop(index)

    if overwrite:
        f = open(fileName, 'w')
        f.writelines(lines)
        f.close()
        print("Value Changed!")
    print()

