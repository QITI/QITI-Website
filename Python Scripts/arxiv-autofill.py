import sys
import arxiv

print('start')
data = sys.stdin.read()
files = data.split('\n')
#files = [sys.argv[1] ]
for fileName in files:
    print(fileName)
    try:
        f = open(fileName, 'r')
        DOI = ""
        lines = f.readlines()
        index = 0
        for line in lines:
            index += 1
            l = line.split(":")
            if l[0] == 'arXiv':
                DOI = l[1].strip()
                DOI = DOI[1:-1]
                print(DOI)
                break

        f.close()
        if DOI == "":
            print(fileName)
            raise NameError("No DOI found in input file")

        print('arXiv: {}'.format(DOI))
        info = arxiv.query(id_list = [DOI])
        print(info)
        abstract = '\n' + info[0]['summary']

        print( 'abstract:\n{}'.format(abstract) )

        f = open(fileName, 'a')
        f.writelines(abstract)
        f.close()

    except:
        print('some error on file')
        print( fileName )
        pass
