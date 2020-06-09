import sys
from crossref.restful import Works
works = Works()

# control some script features
overwrite = False
verbose = False

# read in list of content files, indended for use with grep
# eg $grep -l 'DOI' ../content/publications/* | python crossref-edit.py
data = sys.stdin.read()
files = data.split('\n')
files = files[:-1]

# loop over the list of files provided by grep
for fileName in files:
    print(fileName)
    f = open(fileName, 'r')
    DOI = ""
    lines = f.readlines()
    f.close()
    index = 0
    # loop over the content of each file
    # checks if the DOI field has a value
    for line in lines:
        index += 1
        l = line.split(":")
        if l[0] == 'DOI':
            DOI = l[1].strip()
            print(DOI)
            break
    if DOI == "":
        print(fileName)
        print("No DOI found in input file")
        #raise NameError("No DOI found in input file")
        continue

    # given a DOI exists, get the info from crossref
    info = works.doi(DOI)

    # In here is the code that does the editing!
    try:
        print("AN: ", info['article-number'])
        issue = info['article-number']
    except:
        try:
            print("P: ", info['page'])
            issue = info['page']
        except:
            try:
                print("I: ", info['issue'])
                issue = info['issue']
            except:
                print("no AN, no page, no issue")
                continue

    index = 0
    for line in lines:
        l = line.split(":")
        if l[0] == 'issue':
            print(line[:-1], end=" ----> ")
            lines[index] = 'issue: "{}"\n'.format(issue)
            print(lines[index][:-1])
            break
        index += 1

    if overwrite:
        f = open(fileName, 'w')
        f.writelines(lines)
        f.close()
        print("Value Changed!")
    print()

