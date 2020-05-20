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
    index = 0
    for line in lines:
        index += 1
        l = line.split(":")
        if l[0] == 'DOI':
            DOI = l[1].strip()
            print(DOI)
            break

    f.close()
    if DOI == "":
        print(fileName)
        print("No DOI found in input file")
        #raise NameError("No DOI found in input file")
        continue

    info = works.doi(DOI)
    title = info['title'][0]
    URL = info['URL']
    journal = info['short-container-title'][0]
    volume = info['volume']
    issue = info['issue']
    authors = info['author']
    try:
        date = info['published-print']['date-parts'][0]
    except:
        try:
            date = info['published-online']['date-parts'][0]
        except:
            date = ""
    try:
        abstract = info['abstract']
    except:
        abstract = ""
        pass

    author_list = []
    for author in authors:
        tmp = author['given'].split()
        short_name = ""
        for i in tmp:
            short_name += i[0] + ". "
        short_name += author['family']
        author_list.append([short_name])

    niceDate = ""
    for i in date:
        niceDate += "{}-".format(i)
    niceDate = niceDate[:-1]    



    lines.insert( index-1, ( 'date: {}\n'.format(niceDate) ) )
    lines.insert( index-1, ( 'issue: "{}"\n'.format(issue) ) )
    lines.insert( index-1, ( 'volume: "{}"\n'.format(volume) ) )
    lines.insert( index-1, ( 'journal: "{}"\n'.format(journal) ) )
    lines.insert( index-1, ( 'link: "{}"\n'.format(URL) ) )
    lines.insert( index-1, ( 'authors: {}\n'.format(author_list) ) )
    lines.insert( index-1, ( 'title: "{}"\n'.format(title) ) )

    if verbose:
        print( 'title: "{}"'.format(title) )
        print( 'authors: "{}"'.format(author_list) )
        print( 'URL: "{}"'.format(URL) )
        print( 'journal: "{}"'.format(journal) )
        print( 'volume: "{}"'.format(volume) )
        print( 'issue: "{}"'.format(issue) )
        print( 'date: {}'.format(niceDate) )
        print( '\nabstract:\n{}'.format(abstract) )

    try:
        print("AN: ", info['article-number'])
    except:
        try:
            print("P: ", info['page'])
        except:
            try:
                print("I: ", info['issue'])
            except:
                print("no AN, no page, no issue")
    print()


    if overwrite:
        print("writing to files!")
        f = open(fileName, 'w')
        f.writelines(lines)
        f.close()
        if abstract != "":
            f = open(fileName, 'a')
            f.write("\n{}\n".format(abstract) )
            f.close()

