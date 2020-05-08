# coding: utf-8

f = open('news.txt', 'r')
lines = f.readlines()
f.close()
lightLines = list(filter(lambda a: a!='\n', lines))
comm = []
for line in lightLines:
    words = line.split(' – ')
    print(words[0])
    title = words[0].replace(' ', '-') + '.md'
    #words[1] = words[1].replace('"', "'")
    #comm.append( 'hugo new news/{}\n'.format( title ) )
    #comm.append( 'echo "{}" >> content/news/{}\n'.format( words[1][:-1], title) )
    f = open('content/news/{}'.format(title), 'a')
    f.writelines( words[1] )
    f.close()
    
#print(comm)
#comm.reverse()
#f = open('comm.txt', 'w')
#f.writelines(comm)
#f.close()
