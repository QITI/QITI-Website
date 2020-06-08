import sys
from crossref.restful import Works
works = Works()

overwrite = False
verbose = False

data = sys.stdin.read()
files = data.split('\n')
files = files[:-1]

for fileName in files:
    print(fileName)
    f = open(fileName, 'r')
    DOI = ""
    lines = f.readlines()
    f.close()
    index = 0
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
    info = works.doi(DOI)

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
    print()
    index = 0
    for line in lines:
        index += 1
        l = line.split(":")
        if l[0] == 'issue':
            print(line)
            lines[index] = 'issue: "{}"'.format(issue)
            print(lines[index])
            break
